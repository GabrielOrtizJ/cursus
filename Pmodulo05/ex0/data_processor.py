from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple, Union


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        """
        Extract the oldest stored item and return (rank, data_as_str).
        Raises IndexError if no data is available.
        """
        if not hasattr(self, "_queue") or not self._queue:
            raise IndexError("No data")
        rank, data_str = self._queue.pop(0)
        return rank, data_str


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self._queue: List[Tuple[int, str]] = []
        self._next_rank = 0

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, (int, float)):
                return True
            if isinstance(data, list):
                return all(isinstance(x, (int, float)) for x in data)
            return False
        except Exception:
            return False

    def ingest(
            self, data: Union[
                int, float, List[Union[int, float]]]) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: List[Union[int, float]]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._queue.append((self._next_rank, str(item)))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self._queue: List[Tuple[int, str]] = []
        self._next_rank = 0

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, str):
                return data.strip() != ""
            if isinstance(data, list):
                return all(
                    isinstance(s, str) and s.strip() != "" for s in data)
            return False
        except Exception:
            return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: List[str]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._queue.append((self._next_rank, item))
            self._next_rank += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self._queue: List[Tuple[int, str]] = []
        self._next_rank = 0

    def validate(self, data: Any) -> bool:
        try:
            def is_log_entry(d: Any) -> bool:
                if not isinstance(d, dict):
                    return False
                return all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items())

            if isinstance(data, dict):
                return is_log_entry(data)
            if isinstance(data, list):
                return all(is_log_entry(d) for d in data)
            return False
        except Exception:
            return False

    def ingest(
            self, data: Union[
                Dict[str, str],
                List[Dict[str, str]]]
                ) -> None:

        if not self.validate(data):
            raise ValueError("Improper log data")
        items: List[Dict[str, str]]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for entry in items:
            if "log_level" in entry and "log_message" in entry:
                text = f"{entry['log_level']}: {entry['log_message']}"
            else:
                parts = [f"{k}: {v}" for k, v in entry.items()]
                text = " | ".join(parts)
            self._queue.append((self._next_rank, text))
            self._next_rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    np = NumericProcessor()
    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", np.validate(42))
    print("Trying to validate input 'Hello':", np.validate('Hello'))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except Exception as e:
        print("Got exception:", e)

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])

    extracted = []
    try:
        while True:
            rank, val = np.output()
            extracted.append((rank, val))
    except IndexError:
        pass
    print(f"Extracting {len(extracted)} values...")
    for i, (_, v) in enumerate(extracted):
        print(f"Numeric value {i}: {v}")

    tp = TextProcessor()
    print("Testing Text Processor...")
    print("Trying to validate input '42':", tp.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    extracted = []
    try:
        while True:
            rank, val = tp.output()
            extracted.append((rank, val))
    except IndexError:
        pass
    print(f"Extracting {len(extracted)} value(s)...")
    for i, (_, v) in enumerate(extracted):
        print(f"Text value {i}: {v}")

    lp = LogProcessor()
    print("Testing Log Processor...")
    print("Trying to validate input 'Hello':", lp.validate("Hello"))
    logs = [
        {"log_level": "NOTICE",
         "log_message": "Connection to server"},
        {"log_level": "ERROR",
         "log_message": "Unauthorized access!!"}
    ]
    print("Processing data:", logs)
    lp.ingest(logs)
    extracted = []
    try:
        while True:
            rank, val = lp.output()
            extracted.append((rank, val))
    except IndexError:
        pass
    print(f"Extracting {len(extracted)} values...")
    for i, (_, v) in enumerate(extracted):
        print(f"Log entry {i}: {v}")
