import random
from knowledge import CROP_RULES, NPK_LEVELS

def sample_valid_record():
    crop = random.choice(list(CROP_RULES.keys()))
    rules = CROP_RULES[crop]

    record = {
        "Location": "Ranchi",
        "Crop": crop,
        "Soil_Type": random.choice(rules["soil"]),
        "pH": round(random.uniform(*rules["ph"]), 2),
        "Nitrogen": random.choice(NPK_LEVELS),
        "Phosphorus": random.choice(NPK_LEVELS),
        "Potassium": random.choice(NPK_LEVELS),
        "Rainfall_mm": random.randint(*rules["rainfall"]),
        "Temperature_C": random.randint(*rules["temp"]),
        "Expected_Yield_ton_per_hectare": round(
            random.uniform(*rules["yield"]), 2
        )
    }

    return record
