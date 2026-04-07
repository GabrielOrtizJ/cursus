from alchemy.elements import create_fire, create_earth

fire = create_fire()
earth = create_earth()


def lead_to_gold() -> str:
    return f"Lead transmuted to gold using {fire}"


def stone_to_gem() -> str:
    return f"Stone transmuted to gem using {earth}"
