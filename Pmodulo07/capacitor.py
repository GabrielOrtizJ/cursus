from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main():
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()

    print(" base:")
    base = healing_factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal(None))

    print(" evolved:")
    evolved = healing_factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal(None))

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()

    print(" base:")
    base_t = transform_factory.create_base()
    print(base_t.describe())
    print(base_t.attack())
    print(base_t.transform())
    print(base_t.attack())
    print(base_t.revert())

    print(" evolved:")
    evolved_t = transform_factory.create_evolved()
    print(evolved_t.describe())
    print(evolved_t.attack())
    print(evolved_t.transform())
    print(evolved_t.attack())
    print(evolved_t.revert())


if __name__ == "__main__":
    main()
