import pandas as pd

# Load our custom nutrition dataset
data = pd.read_csv("multimodal_ai/nutrition_dataset.csv")

nutrition_db = {}

for _, row in data.iterrows():

    food = str(row["food"]).lower()

    nutrition_db[food] = {
        "calories": row["calories"],
        "carbs": row["carbs"],
        "fat": row["fat"],
        "protein": row["protein"]
    }

print("Nutrition database loaded with", len(nutrition_db), "foods")