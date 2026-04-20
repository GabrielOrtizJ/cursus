from enum import Enum
from datetime import datetime
from typing import List

try:
    from pydantic import BaseModel, model_validator, Field
except ModuleNotFoundError:
    print("Error: la librería 'pydantic' no está instalada.")
    print("Instálala con: pip install pydantic")
    exit(1)


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(le=datetime.today())
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def mission_validation_rules(self):
        if self.mission_id[:1] != "M":
            raise ValueError('Mission ID must start with "M"')
        leader = any(
            m.rank in [Rank.captain, Rank.commander] for m in self.crew)
        if not leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        len_crew = len(self.crew)
        most_experience = [
            member.years_experience for member in self.crew
            if member.years_experience >= 5]
        percent_experience_member = len(most_experience) / len_crew
        if self.duration_days > 365 and percent_experience_member < 0.5:
            raise ValueError(
                "Long missions (>365 days)"
                "need 50% experienced crew (5+ years)"
                )
        for members in self.crew:
            if members.is_active is False:
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
                is_active=True
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=6,
                is_active=True
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=5,
                is_active=True
            ),
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 1),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
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
                f"({member.rank.value}) - {member.specialization}")

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
                is_active=True
            )
        ]

        fail_mission = SpaceMission(
            mission_id="M_FAIL",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime(2024, 6, 1),
            duration_days=30,
            crew=crew_fail,
            budget_millions=500.0
        )
        print(fail_mission)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
