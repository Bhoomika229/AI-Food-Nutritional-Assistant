import streamlit as st
from image_analysis import analyze_image
from text_analysis import analyze_question
from nutrition_data import nutrition_db
from PIL import Image
import tempfile

st.title("🍔 AI Food Nutrition Assistant")

st.write("Upload a food image and ask a question about its nutrition.")

uploaded_file = st.file_uploader("Upload Food Image", type=["jpg","png","jpeg"])

question = st.text_input("Ask a question about the food")

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        image.save(temp.name)
        image_path = temp.name

    food = analyze_image(image_path)
    # Correct similar food labels
food_map = {
    "potpie": "pizza",
    "quiche": "pizza",
    "sandwich": "burger",
    "hotdog": "burger",
    "plate": "pizza"
}

if food in food_map:
    food = food_map[food]

    st.write("### Detected Food:", food)

    if question:

        result = analyze_question(question)

        if food in nutrition_db:

            data = nutrition_db[food]

            calories = float(data["calories"])
            carbs = float(data["carbs"])
            fat = float(data["fat"])
            protein = float(data["protein"])

            if result == "health":

                st.write("### Nutrition Information")
                st.write("Calories:", calories, "kcal")
                st.write("Carbs:", carbs, "g")
                st.write("Fat:", fat, "g")
                st.write("Protein:", protein, "g")

                if calories > 300:
                    st.warning("High calorie food. Eat in moderation.")
                elif fat > 15:
                    st.warning("High fat content. Occasional consumption recommended.")
                elif carbs > 40:
                    st.warning("High carbohydrate food. Not ideal for low-carb diets.")
                elif protein > 15:
                    st.success("Good protein source and relatively healthy.")
                else:
                    st.success("Balanced nutrition, generally healthy.")

            elif result == "protein":
                st.write("Protein Content:", protein, "g")

            elif result == "calories":
                st.write("Total Calories:", calories, "kcal")

            elif result == "carbs":
                st.write("Carbohydrates:", carbs, "g")

            elif result == "fat":
                st.write("Fat Content:", fat, "g")

            elif result == "weight_loss":
                if calories < 200:
                    st.success("Good option for weight loss.")
                else:
                    st.warning("Not ideal for weight loss due to high calories.")

            else:
                st.info("I can answer questions about health, calories, protein, carbs, fat, and diet.")

        else:
            st.error("Food not found in nutrition database.")