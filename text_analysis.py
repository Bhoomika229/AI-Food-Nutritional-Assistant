def analyze_question(question):

    question = question.lower()

    if "healthy" in question:
        return "health"

    elif "protein" in question:
        return "protein"

    elif "calorie" in question:
        return "calories"

    elif "carb" in question:
        return "carbs"

    elif "fat" in question:
        return "fat"

    elif "weight loss" in question or "diet" in question:
        return "weight_loss"

    else:
        return "general"