from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from collections import Counter


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.total_batches = 0
        self.total_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "batches_processed": self.total_batches,
            "items_processed": self.total_items,
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings = [float(x) for x in data_batch]
        except Exception:
            return f"[{self.stream_id}] Invalid sensor batch"

        self.total_batches += 1
        self.total_items += len(readings)

        if any(r > 80 or r < -20 for r in readings):
            return (f"Sensor analysis: {len(readings)} readings processed "
                    f"(ALERT: extreme values detected)")

        avg_temp = sum(readings) / len(readings) if readings else 0.0

        return (f"Sensor analysis: {len(readings)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [x for x in data_batch
                    if isinstance(x, (int, float)) and x > 50]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            ops = []
            for item in data_batch:
                op, val = item.split(":")
                ops.append((op, int(val)))
        except Exception:
            return f"[{self.stream_id}] Invalid transaction batch"

        self.total_batches += 1
        self.total_items += len(ops)

        net = sum(v if op == "buy" else -v for op, v in ops)

        return (f"Transaction analysis: {len(ops)} operations, "
                f"net flow: {net:+d} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            return [x for x in data_batch
                    if ":" in x and abs(int(x.split(":")[1])) > 100]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        if not all(isinstance(x, str) for x in data_batch):
            return f"[{self.stream_id}] Invalid event batch"

        self.total_batches += 1
        self.total_items += len(data_batch)

        counts = Counter(x.lower() for x in data_batch)
        errors = counts.get("error", 0)

        return (f"Event analysis: {len(data_batch)} events, "
                f"{errors} error detected")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            return [x for x in data_batch if x.lower() == "error"]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def run_batch(self, stream: DataStream,
                  data_batch: List[Any],
                  criteria: Optional[str] = None) -> str:

        try:
            filtered = stream.filter_data(data_batch, criteria)
            return stream.process_batch(filtered)
        except Exception as e:
            return f"[{stream.stream_id}] Processing error: {e}"


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.get_stats()['type']}")
    print(sensor.process_batch([22.5, 65, 1013]), "\n")

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.get_stats()['type']}")
    print(trans.process_batch(["buy:100", "sell:150", "buy:75"]), "\n")

    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.get_stats()['type']}")
    print(event.process_batch(["login", "error", "logout"]), "\n")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    batches = [
        [20, 55],
        ["buy:200", "sell:50", "buy:300", "sell:150"],
        ["login", "error", "logout"],
    ]

    for stream, batch in zip(processor.streams, batches):
        print(processor.run_batch(stream, batch))

    print("\nStream filtering active: High-priority data only")

    print(processor.run_batch(sensor, [10, 80, 120], criteria="high"))
    print(processor.run_batch(trans, ["buy:50", "sell:200"], criteria="large"))
    print(processor.run_batch(event, ["login", "error"], criteria="critical"))

    print("\nAll streams processed successfully. Nexus throughput optimal.")
