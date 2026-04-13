from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = light_spell_allowed_ingredients()
    ing_lower = ingredients.lower()

    if any(a in ing_lower for a in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
