from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: List[Tuple[int, str]] = []
        self._next_rank = 0
        self.total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._queue:
            raise IndexError("No data")
        rank, data_str = self._queue.pop(0)
        return rank, data_str

    def remaining(self) -> int:
        return len(self._queue)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
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
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: List[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._queue.append((self._next_rank, item))
            self._next_rank += 1
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log_entry(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return all(isinstance(k, str) and
                       isinstance(v, str) for k, v in d.items())

        if isinstance(data, dict):
            return is_log_entry(data)
        if isinstance(data, list):
            return all(is_log_entry(d) for d in data)
        return False

    def ingest(
            self, data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items: List[
            Dict[str, str]] = data if isinstance(data, list) else [data]
        for entry in items:
            if "log_level" in entry and "log_message" in entry:
                text = f"{entry['log_level']}: {entry['log_message']}"
            else:
                parts = [f"{k}: {v}" for k, v in entry.items()]
                text = " | ".join(parts)
            self._queue.append((self._next_rank, text))
            self._next_rank += 1
            self.total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                try:
                    if proc.validate(element):
                        try:
                            proc.ingest(element)
                            handled = True
                        except Exception:
                            print(f"DataStream error - Can't "
                                  f"process element in stream: {element}")
                            handled = True
                        break
                except Exception:
                    continue
            if not handled:
                print(f"DataStream error - Can't "
                      f"process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.total_processed} items processed,"
                  f" remaining {proc.remaining()} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)

    print("Send first batch of data on stream:", batch)
    ds.process_stream(batch)

    ds.print_processors_stats()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    print("Send the same batch again")
    ds.process_stream(batch)

    ds.print_processors_stats()

    print("Consume some elements from the data "
          "processors: Numeric 3, Text 2, Log 1")
    # consume numeric 3
    for _ in range(3):
        try:
            num_proc.output()
        except IndexError:
            break
    # consume text 2
    for _ in range(2):
        try:
            text_proc.output()
        except IndexError:
            break
    # consume log 1
    try:
        log_proc.output()
    except IndexError:
        pass

    ds.print_processors_stats()
