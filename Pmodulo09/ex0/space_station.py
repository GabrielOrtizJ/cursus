from pydantic import BaseModel, Field, ValidationError
from typing import Annotated
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(ge=1, le=20)]
    power_level: Annotated[float, Field(ge=0, le=100)]
    oxygen_level: Annotated[float, Field(ge=0, le=100)]
    last_maintenance: datetime
    is_operational: bool = True
    notes: Annotated[str | None, Field(max_length=200)] = None


def main():
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 5, 20),
        is_operational=True,
        notes="All correct"
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Maintenance"
    print(f"Status: {status}")
    print()
    print("========================================")
    print("Expected validation error:")

    try:
        fail_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=60,  # INVALID
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 20),
            is_operational=True,
            notes="All correct"
        )
        print(fail_station.station_id)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
