import pandas as pd

print("Loading USDA files...")

food = pd.read_csv("multimodal_ai/food.csv")
food_nutrient = pd.read_csv("multimodal_ai/food_nutrient.csv", low_memory=False)
nutrient = pd.read_csv("multimodal_ai/nutrient.csv")

print("Selecting important nutrients...")

important_nutrients = nutrient[
    nutrient["name"].isin([
        "Energy",
        "Protein",
        "Total lipid (fat)",
        "Carbohydrate, by difference"
    ])
]

important_ids = important_nutrients["id"].tolist()

filtered = food_nutrient[
    food_nutrient["nutrient_id"].isin(important_ids)
]

print("Merging food and nutrient data...")

merged = filtered.merge(
    food,
    on="fdc_id"
)

print("Creating final nutrition table...")

final = merged.pivot_table(
    index="description",
    columns="nutrient_id",
    values="amount"
)

final.to_csv("multimodal_ai/clean_nutrition_dataset.csv")

print(" Nutrition dataset created successfully!")