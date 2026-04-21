from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Annotated
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: Annotated[str, Field(min_length=5, max_length=15)]
    timestamp: datetime
    location: Annotated[str, Field(min_length=3, max_length=100)]
    contact_type: ContactType
    signal_strength: Annotated[float, Field(ge=0, le=10)]
    duration_minutes: Annotated[int, Field(ge=1, le=1440)]
    witness_count: Annotated[int, Field(ge=1, le=100)]
    message_received: Annotated[str | None, Field(max_length=500)] = None
    is_verified: bool = False

    @model_validator(mode="after")
    def business_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.telepathic
           and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals should include received messages"
            )

        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")

    alien = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 6, 10),
        location="Area 52, Nevada",
        contact_type="radio",
        signal_strength=9.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )

    print("Valid contact report:")
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witness: {alien.witness_count}")
    print(f"Message: {alien.message_received}")
    print()
    print("======================================")
    print("Expected validation error:")

    try:
        fail_alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 10),
            location="Area 52, Nevada",
            contact_type="telepathic",
            signal_strength=9.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
        print(fail_alien.contact_id)
    except ValidationError as e:
        for error in e.errors():
            msg = error["msg"]
            if msg.startswith("Value error, "):
                msg = msg.replace("Value error, ", "")
            print(msg)


if __name__ == "__main__":
    main()
