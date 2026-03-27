from abc import ABC, abstractmethod
from typing import Any


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

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, list):
                [int(n) for n in data]
            else:
                int(data)
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid numeric data")

        numbers = [int(n) for n in data]
        total = sum(numbers)
        avg = total / len(numbers)

        result = (
            f"Processed {len(numbers)} numbers | sum={total}, avg={avg:.2f}")
        return self.format_output(result)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            stripped = data.strip()
            return stripped != ""
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid text data")

        text = data.strip()
        words = len(text.split())
        chars = len(text)

        result = f"Text contains {chars} characters and {words} words"
        return self.format_output(result)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            stripped = data.strip()
            return (stripped.startswith("ERROR:") or
                    stripped.startswith("INFO:"))
        except Exception:
            return False

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


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors = [
        NumericProcessor([1, 2, 3, 4, 5]),
        TextProcessor("Hello Nexus World"),
        LogProcessor("ERROR: Connection timeout"),
        LogProcessor("INFO: System ready"),
    ]

    for processor in processors:
        processor.process()
        print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    demo_processors = [
        NumericProcessor([1, 2, 3]),
        TextProcessor("Hello World"),
        LogProcessor("INFO: System ready"),
    ]

    index = 1
    for processor in demo_processors:
        print(f"Result {index}: ", end="")
        processor.process()
        index += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
