from typing import Dict, List


def artifact_sorter(artifacts: Dict):
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: Dict, min_power: int):
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: List):
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages):
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages),
            2
        )
    }


def main():

    artifacts = [
        {'name': 'Crystal Orb', 'power': 72, 'type': 'relic'},
        {'name': 'Earth Shield', 'power': 69, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 72, 'type': 'armor'},
        {'name': 'Ice Wand', 'power': 108, 'type': 'relic'}
        ]

    mages = [
        {'name': 'Casey', 'power': 10, 'element': 'earth'},
        {'name': 'Sage', 'power': 20, 'element': 'water'},
        {'name': 'Kai', 'power': 31, 'element': 'ice'}
        ]

    spells = ['lightning', 'meteor', 'heal', 'freeze']

    print("=== Lambda Sanctum ===\n")

    print(f"artifact_sorter >> {artifact_sorter(artifacts)}\n")
    print(f"power_filter with 80 power>> {power_filter(mages, 80)}\n")
    print(f"spell_transformer >> {spell_transformer(spells)}\n")
    print(f"mage_stats >> {mage_stats(mages)}")


if __name__ == "__main__":
    main()
