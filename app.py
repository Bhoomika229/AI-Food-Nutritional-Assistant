from image_analysis import analyze_image
from text_analysis import analyze_question
from nutrition_data import nutrition_db


image_path = input("Enter image path: ")

question = input("Ask a question about the food image: ")

food = analyze_image(image_path)
food = food.strip().lower().replace(" ", "_")
print("detected food:", food)

matched_food = None

# try direct match
if food in nutrition_db:
    matched_food = food

else:
    # try partial match
    for item in nutrition_db:

        if food in item:
            matched_food = item
            break

        if item in food:
            matched_food = item
            break

result = analyze_question(question)

if matched_food:

    data = nutrition_db[matched_food]

    calories = float(data["calories"])
    carbs = float(data["carbs"])
    fat = float(data["fat"])
    protein = float(data["protein"])

    print("\nDetected food:", food)

    if result == "health":

        print("\nNutrition Information:")
        print("Calories:", calories, "kcal")
        print("Carbs:", carbs, "g")
        print("Fat:", fat, "g")
        print("Protein:", protein, "g")

        if calories > 300:
            print("\nHealth Advice: High calorie food. Eat in moderation.")

        elif fat > 15:
            print("\nHealth Advice: High fat content. Occasional consumption recommended.")

        elif carbs > 40:
            print("\nHealth Advice: High carbohydrate food. Not ideal for low-carb diets.")

        elif protein > 15:
            print("\nHealth Advice: Good protein source and relatively healthy.")

        else:
            print("\nHealth Advice: Balanced nutrition, generally healthy.")

    elif result == "protein":

        print("\nProtein Content:", protein, "g")

    elif result == "calories":

        print("\nTotal Calories:", calories, "kcal")

    elif result == "carbs":

        print("\nCarbohydrates:", carbs, "g")

    elif result == "fat":

        print("\nFat Content:", fat, "g")

    elif result == "weight_loss":

        if calories < 200:
            print("\nGood option for weight loss.")

        else:
            print("\nNot ideal for weight loss due to high calories.")

    else:

        print("\nI can answer questions about health, calories, protein, carbs, fat, and diet.")

else:

    print("\nFood not found in nutrition database.")