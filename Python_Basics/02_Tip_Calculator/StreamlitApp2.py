import streamlit as st

# Title of the app
st.title("Tip Calculator")
st.write("Welcome to the tip calculator!")

# User inputs
bill = st.number_input("What was the total bill? $", min_value=0.01, step=0.01)
tip = st.number_input("How much tip would you like to give? (10, 12, or 15)", step=1)
spliting = st.number_input("How many people to split the bill? (at least 1)", min_value=1, step=1)

# Tip calculation function
def tip_calculator():
    total_bill_with_tip = bill + (bill * (tip / 100))
    amount_per_person = total_bill_with_tip / spliting
    return total_bill_with_tip, amount_per_person

# Display the results
if bill > 0 and spliting >= 1:
    total_bill_with_tip, amount_per_person = tip_calculator()
    st.write(f"**Total Bill with Tip:** ${total_bill_with_tip:.2f}")
    st.write(f"**Each person should pay:** ${amount_per_person:.2f}")
