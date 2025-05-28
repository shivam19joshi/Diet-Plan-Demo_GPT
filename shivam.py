import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to get diet plan based on BMI
def get_diet_plan(bmi):
    if bmi < 18.5:
        category = "Underweight"
        plan = [
            "🟢 High-calorie diet with 5-6 meals a day",
            "🥑 Include nuts, dairy, avocado, and healthy oils",
            "💪 Strength training to gain muscle mass"
        ]
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        plan = [
            "🟢 Balanced diet: carbs, protein, and fat",
            "🥦 Include fruits, vegetables, whole grains, and lean protein",
            "🚶‍♂️ Moderate exercise (30 mins/day)"
        ]
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        plan = [
            "🟠 Calorie deficit with portion control",
            "🥗 Focus on fiber-rich and protein-rich meals",
            "🏃‍♂️ Cardio + strength training 4-5 times/week"
        ]
    else:
        category = "Obese"
        plan = [
            "🔴 Low-calorie diet with professional supervision",
            "🥣 Avoid sugar, processed food, and high-fat meals",
            "🚴 Daily exercise + regular health monitoring"
        ]
    return category, plan

# Streamlit UI
st.set_page_config(page_title="Diet Planner", page_icon="🍽️")

st.title("🥗 Personalized Diet Planner")

# Input Section
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120)
height = st.number_input("Enter your height (in cm)", min_value=50.0, max_value=250.0)
weight = st.number_input("Enter your weight (in kg)", min_value=10.0, max_value=300.0)

# Output Section
if st.button("Generate Diet Plan"):
    if name and age and height and weight:
        bmi = calculate_bmi(weight, height)
        category, plan = get_diet_plan(bmi)

        st.success(f"Hello {name}! 👋")
        st.write(f"**Your BMI is:** {bmi} ({category})")

        st.subheader("💡 Recommended Diet Plan:")
        for item in plan:
            st.write(f"- {item}")
    else:
        st.warning("Please fill in all the details to generate your diet plan.")
