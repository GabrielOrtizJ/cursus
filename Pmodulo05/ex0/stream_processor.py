from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"[RESULT] {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid numeric data")

        numbers = list(map(int, data))
        total = sum(numbers)
        avg = total / len(numbers)

        result = (f"Processed {len(numbers)} numbers |"
                  f"sum={total}, avg={avg:.2f}")

        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        try:
            for n in data:
                int(n)
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid text data")

        text = data.strip()
        words = len(text.split())
        chars = len(text)

        result = f"Text contains {chars} characters and {words} words"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and data.strip() != ""


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid log entry")

        level, message = data.split(":", maxsplit=1)
        message = message.strip()

        if level == "ERROR":
            result = f"[ALERT] {level}: {message}"
        else:
            result = f"[INFO] {level}: {message}"

        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False

        data = data.strip()
        return data.startswith("ERROR:") or data.startswith("INFO:")


if __name__ == "__main__":
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    inputs = [
        [1, 2, 3, 4],
        "Hello Nexus World",
        "INFO: Connection timeout",
    ]

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")

    for processor, data in zip(processors, inputs):
        print(f"Processing data: {data}")
        if processor.validate(data):
            print("Numeric data verified")
        else:
            print("Numeric data not verified")
        print(processor.process(data))
        print()

    print("=== Polymorphic Processing Demo ===\n")
