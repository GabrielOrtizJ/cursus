from enum import Enum
from datetime import datetime
from typing import Annotated, List
from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=2, max_length=50)]
    rank: Rank
    age: Annotated[int, Field(ge=18, le=80)]
    specialization: Annotated[str, Field(min_length=3, max_length=30)]
    years_experience: Annotated[int, Field(ge=0, le=50)]
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: Annotated[str, Field(min_length=5, max_length=15)]
    mission_name: Annotated[str, Field(min_length=3, max_length=100)]
    destination: Annotated[str, Field(min_length=3, max_length=50)]
    launch_date: datetime
    duration_days: Annotated[int, Field(ge=1, le=3650)]
    crew: List[CrewMember]
    mission_status: str = "planned"
    budget_millions: Annotated[float, Field(ge=1, le=10000)]

    @model_validator(mode="after")
    def mission_validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leader = any(
            member.rank in (Rank.captain, Rank.commander)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        experienced = [
            m for m in self.crew if m.years_experience >= 5
        ]
        if (
            self.duration_days > 365
            and len(experienced) / len(self.crew) < 0.5
        ):
            raise ValueError(
                "Long missions (>365 days) need 50% experienced crew (5+ years)"
            )

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self

def main():
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        crew = [
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=42,
                specialization="Mission Command",
                years_experience=15,
                is_active=True,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=6,
                is_active=True,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=5,
                is_active=True,
            ),
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 1),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0,
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} "
                f"({member.rank.value}) - {member.specialization}"
            )

    except ValueError as e:
        print("Unexpected error:", e)

    print("=========================================")
    print("Expected validation error:")

    try:
        crew_fail = [
            CrewMember(
                member_id="C010",
                name="Tom Hardy",
                rank=Rank.officer,
                age=38,
                specialization="Engineering",
                years_experience=10,
                is_active=True,
            )
        ]

        fail_mission = SpaceMission(
            mission_id="M_FAIL",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime(2024, 6, 1),
            duration_days=30,
            crew=crew_fail,
            budget_millions=500.0,
        )

        print(fail_mission)

    except ValueError as e:
        print(e)
