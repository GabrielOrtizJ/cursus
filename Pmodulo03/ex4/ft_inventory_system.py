#!/usr/bin/env python3

def show_inventory(players, name):
    """
    Print a formatted inventory for a given player.
    """
    print(f"=== {name}'s Inventory ===")
    inventory = players.get(name, {})

    total_value = 0
    total_items = 0
    categories = {}

    for item, data in inventory.items():
        units = int(data.get('units'))
        value = int(data.get('value'))
        item_type = data.get('type')
        rare = data.get('rare')

        item_total = units * value
        total_value += item_total
        total_items += units

        categories[item_type] = categories.get(item_type, 0) + units

        print(f"{item} ({item_type}, {rare}): {units}x @ {value} gold each ="
              f" {item_total} gold")

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print("Categories:", end=" ")

    first = True
    for c, n in categories.items():
        if not first:
            print(", ", end="")
        print(f"{c}({n})", end="")
        first = False
    print("\n")


def transaction(players, giver, receiver, item, amount):
    """
    Transfer items between players if possible.
    """
    print(f"=== Transaction: {giver} gives {receiver} {amount} {item}s ===")

    giver_inv = players.get(giver)
    receiver_inv = players.get(receiver)

    if giver_inv is None or receiver_inv is None:
        print("Transaction failed: invalid player")
        return

    if item not in giver_inv:
        print("Transaction failed: giver does not have the item")
        return

    giver_units = int(giver_inv[item].get('units'))

    if giver_units < amount:
        print("Transaction failed: not enough units")
        return

    # update giver
    giver_inv[item].update({'units': str(giver_units - amount)})

    # update receiver
    receiver_units = int(receiver_inv.get(item, {}).get('units', '0'))
    if item not in receiver_inv:
        receiver_inv[item] = dict(giver_inv[item])  # copy structure
    receiver_inv[item].update({'units': str(receiver_units + amount)})

    print("Transaction successful!\n")


def inventory_analytics(players):
    """
    Compute inventory statistics across all players.
    """
    print("=== Inventory Analytics ===")

    # Most valuable player
    max_value = -1
    richest = None

    # Most items
    max_items = -1
    most_items_player = None

    # Rare items
    item_counts = {}

    for name, inv in players.items():
        total_value = 0
        total_units = 0

        for item, data in inv.items():
            units = int(data.get('units'))
            value = int(data.get('value'))

            total_value += units * value
            total_units += units

            item_counts[item] = item_counts.get(item, 0) + units

        if total_value > max_value:
            max_value = total_value
            richest = name

        if total_units > max_items:
            max_items = total_units
            most_items_player = name

    rare_items = [item for item, count in item_counts.items() if count == 1]

    print(f"Most valuable player: {richest} ({max_value} gold)")
    print(f"Most items: {most_items_player} ({max_items} items)")
    print(f"Rarest items: {', '.join(rare_items)}\n")


def inventory_system():
    print("=== Player Inventory System ===")

    players = {
        'Alice': {
            'sword': {'type': 'weapon',
                      'rare': 'rare',
                      'value': '500',
                      'units': '1'},
            'potion': {'type': 'consumable',
                       'rare': 'common',
                       'value': '50',
                       'units': '5'},
            'shield': {'type': 'armor',
                       'rare': 'uncommon',
                       'value': '200',
                       'units': '1'},
            'magic_ring': {'type': 'accessories',
                           'rare': 'mitical',
                           'value': '1000',
                           'units': '1'}
        },
        'Bob': {
            'sword': {'type': 'weapon',
                      'rare': 'rare',
                      'value': '350',
                      'units': '1'},
            'potion': {'type': 'consumable',
                       'rare': 'common',
                       'value': '50',
                       'units': '0'},
            'shield': {'type': 'armor',
                       'rare': 'uncommon',
                       'value': '150',
                       'units': '1'}
        }
    }

    show_inventory(players, 'Alice')
    transaction(players, 'Alice', 'Bob', 'potion', 2)
    print("=== Updated Inventories ===")
    print("Alice potions:", players['Alice']['potion']['units'])
    print("Bob potions:", players['Bob']['potion']['units'])
    inventory_analytics(players)


if __name__ == "__main__":
    inventory_system()
