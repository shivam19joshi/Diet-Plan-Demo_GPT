import streamlit as st

# --- Function to calculate BMI ---
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# --- Function to get BMI Category ---
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# --- Function to get diet plan ---
def get_diet_plan(category):
    plans = {
        "Underweight": {
            "Breakfast": "Peanut butter toast + Banana + Milkshake",
            "Lunch": "Rice + Paneer curry + Dal + Ghee + Salad",
            "Snacks": "Dry fruits + Cheese sandwich"

        },
        "Normal weight": {
            "Breakfast": "Oats + Fruits + Boiled egg / Milk",
            "Lunch": "Roti/Rice + Veg/Dal + Salad",
            "Snacks": "Fruit bowl or nuts",
            "Dinner": "Soup + Roti + Sabzi + Curd"
        },
        "Overweight": {
            "Breakfast": "Green tea + Upma / Poha / Fruits",
            "Lunch": "Grilled Paneer/Chicken + Salad + 1 Roti",
            "Snacks": "Buttermilk + Nuts",
            "Dinner": "Stir fry veggies + Soup + 1 Roti"
        },
        "Obese": {
            "Breakfast": "Warm water + Boiled eggs / Fruits",
            "Lunch": "Salad + Grilled vegetables + Quinoa",
            "Snacks": "Cucumber / Carrot sticks",
            "Dinner": "Vegetable soup + Grilled tofu/paneer"
        }
    }
    return plans.get(category, {})

# --- Streamlit UI ---
st.title("☠️Personalized Diet Planner")

st.write("Enter your details to get a personalized diet suggestion.")

# Input fields
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120)
height = st.number_input("Height (in cm)", min_value=50, max_value=250)
weight = st.number_input("Weight (in kg)", min_value=10, max_value=300)

if st.button("Get Diet Plan"):
    if name and height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        diet = get_diet_plan(category)

        st.success(f"Hi {name}, your BMI is **{bmi}** which is considered **{category}**.")
        st.header("🍽️ Your Suggested Diet Plan")

        for meal, items in diet.items():
            st.subheader(meal)
            st.write(items)
    else:
        st.warning("Please fill all the fields correctly.")
