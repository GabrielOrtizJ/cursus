#!/usr/bin/env python3

def show_inventory(players, name):
    print(f"=== {name.capitalize()}'s Inventory ===")

    pdata = players['players'].get(name)
    if pdata is None:
        print("Player not found\n")
        return

    items = pdata['items']
    catalog = players['catalog']

    total_value = 0
    total_units = 0
    categories = dict()

    for item, units in items.items():
        info = catalog.get(item)
        itype = info.get('type')
        rarity = info.get('rarity')
        value = info.get('value')

        item_total = units * value
        total_value += item_total
        total_units += units

        categories[itype] = categories.get(itype, 0) + units

        print(f"{item} ({itype}, {rarity}): {units}x @"
              f" {value} gold each = {item_total} gold")

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_units} items")

    print("Categories:", end=" ")
    first = True
    for c, n in categories.items():
        if not first:
            print(", ", end="")
        print(f"{c}({n})", end="")
        first = False
    print("\n")


def transaction(players, giver, receiver, item, amount):
    print(f"=== Transaction: {giver.capitalize()} gives"
          f" {receiver.capitalize()} {amount} {item}s ===")

    pdata = players['players']

    giver_items = pdata.get(giver, {}).get('items')
    receiver_items = pdata.get(receiver, {}).get('items')

    if giver_items is None or receiver_items is None:
        print("Transaction failed: invalid player\n")
        return

    if giver_items.get(item, 0) < amount:
        print("Transaction failed: not enough items\n")
        return

    # Update giver
    giver_items.update({item: giver_items.get(item) - amount})
    if giver_items.get(item) == 0:
        del giver_items[item]

    # Update receiver
    receiver_items.update({item: receiver_items.get(item, 0) + amount})

    print("Transaction successful!\n")


def inventory_analytics(players):
    print("=== Inventory Analytics ===")

    pdata = players['players']
    catalog = players['catalog']

    richest = None
    richest_value = -1

    most_items = None
    most_count = -1

    # Para rare items: contar jugadores, no unidades
    item_owner_count = dict()

    for name, info in pdata.items():
        items = info['items']

        total_value = 0
        total_units = 0

        for item, units in items.items():
            if units > 0:
                value = catalog[item]['value']
                total_value += units * value
                total_units += units

                # Contar cuántos jugadores tienen este ítem
                item_owner_count[item] = item_owner_count.get(item, 0) + 1

        if total_value > richest_value:
            richest_value = total_value
            richest = name

        if total_units > most_count:
            most_count = total_units
            most_items = name

    # Ítems que solo un jugador posee
    rare_items = [item for item, owners in item_owner_count.items() if owners == 1]

    print(f"Most valuable player: {richest.capitalize()} ({richest_value} gold)")
    print(f"Most items: {most_items.capitalize()} ({most_count} items)")
    print(f"Rarest items: {', '.join(rare_items) if rare_items else 'None'}\n")


def inventory_system():
    print("=== Player Inventory System ===\n")

    players = {
        'players': {
            'alice': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1,
                    'health_byte': 1,
                    'quantum_ring': 3
                },
                'total_value': 1875,
                'item_count': 6
            },
            'bob': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 2
                },
                'total_value': 900,
                'item_count': 5
            },
            'charlie': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1
                },
                'total_value': 350,
                'item_count': 2
            },
            'diana': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 3,
                    'health_byte': 3,
                    'data_crystal': 3
                },
                'total_value': 4125,
                'item_count': 12
            }
        },
        'catalog': {
            'pixel_sword': {'type': 'weapon', 'value': 150, 'rarity': 'common'},
            'quantum_ring': {'type': 'accessory', 'value': 500, 'rarity': 'rare'},
            'health_byte': {'type': 'consumable', 'value': 25, 'rarity': 'common'},
            'data_crystal': {'type': 'material', 'value': 1000, 'rarity': 'legendary'},
            'code_bow': {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}
        }
    }

    show_inventory(players, 'alice')
    transaction(players, 'alice', 'bob', 'pixel_sword', 1)
    inventory_analytics(players)


if __name__ == "__main__":
    inventory_system()
