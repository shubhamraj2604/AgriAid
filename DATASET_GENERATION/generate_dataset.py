import random
import csv
from knowledge import CROP_RULES, NPK

def generate_row():
    crop = random.choice(list(CROP_RULES.keys()))
    rules = CROP_RULES[crop]

    return {
        "Location": "Ranchi",
        "Crop": crop,
        "Soil_Type": random.choice(rules["soil"]),
        "pH": round(random.uniform(*rules["ph"]), 2),
        "Nitrogen": random.choice(NPK),
        "Phosphorus": random.choice(NPK),
        "Potassium": random.choice(NPK),
        "Rainfall_mm": random.randint(*rules["rainfall"]),
        "Temperature_C": random.randint(*rules["temp"]),
        "Expected_Yield_ton_per_hectare": round(
            random.uniform(*rules["yield"]), 2
        )
    }


def generate_dataset(n=10000):
    return [generate_row() for _ in range(n)]


def save_csv(data, filename="crop_dataset.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    data = generate_dataset(10000)
    save_csv(data)
