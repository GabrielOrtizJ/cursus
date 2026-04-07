from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple, Union, Protocol


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
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if isinstance(data, dict):
            return is_log_entry(data)
        if isinstance(data, list):
            return all(is_log_entry(d) for d in data)
        return False

    def ingest(
        self,
        data: Union[Dict[str, str], List[Dict[str, str]]],
    ) -> None:
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


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        if not data:
            return
        values = [v for _, v in data]
        line = ",".join(values)
        print("CSV Output:")
        print(line)


class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        if not data:
            return
        parts: List[str] = []
        for rank, value in data:
            parts.append(f"\"item_{rank}\": \"{value}\"")
        json_str = "{" + ", ".join(parts) + "}"
        print("JSON Output:")
        print(json_str)


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
                            print(
                                "DataStream error - Can't "
                                f"process element in stream: {element}"
                            )
                            handled = True
                        break
                except Exception:
                    continue
            if not handled:
                print(
                    "DataStream error - Can't "
                    f"process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {proc.total_processed} items "
                f"processed, remaining {proc.remaining()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        # Para cada procesador, consumimos hasta nb elementos
        for proc in self.processors:
            batch: List[Tuple[int, str]] = []
            for _ in range(nb):
                try:
                    rank, val = proc.output()
                    batch.append((rank, val))
                except IndexError:
                    break
            if batch:
                plugin.process_output(batch)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print("Registering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    print("Send first batch of data on stream:", batch1)
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send another batch of data:", batch2)
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()
