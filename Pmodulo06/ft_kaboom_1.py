print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

try:
    # El import debe estar DENTRO del try
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    # Si por algún milagro no explota, lo usamos
    dark_spell_record("Forbidden Spell", "arsenic and frogs")

except Exception as e:
    print("Explosion detected:", e)
    raise
