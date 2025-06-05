import streamlit as st
import pandas as pd
import numpy as np

# Simulated contact form handler (placeholder for real email integration)
def process_contact_form(name, email, message):
    st.success(f"Thank you, {name}. Your message has been sent!")

# ROI calculator function
# Calculates annual return on investment based on purchase price, monthly income, and expenses
def calculate_roi(purchase_price, rental_income, expenses):
    annual_income = rental_income * 12
    annual_expenses = expenses * 12
    roi = ((annual_income - annual_expenses) / purchase_price) * 100
    return roi

# Main app logic
# Handles UI layout and tabbed interface
def main():
    st.set_page_config(page_title="Jarvis2 Real Estate Agent", layout="wide")

    # Main UI
    st.title("🤖 Welcome to Jarvis2")
    st.subheader("Explore properties, calculate returns, and connect with us.")

    # Define three tabs for different features
    tab1, tab2, tab3 = st.tabs(["🏠 Property Search", "📊 ROI Calculator", "📩 Contact Jarvis2"])

    # ----- Tab 1: Property Search -----
    with tab1:
        st.header("Property Search")
        try:
            # Load property data from a CSV file
            df = pd.read_csv("properties.csv")
            st.dataframe(df)  # Display full data before filtering

            # Filter by city
            city_filter = st.selectbox("Select City", options=["All"] + df["City"].unique().tolist())
            if city_filter != "All":
                df = df[df["City"] == city_filter]

            # Filter by price range using a slider
            price_range = st.slider(
                "Price Range",
                min_value=int(df["Price"].min()),
                max_value=int(df["Price"].max()),
                value=(int(df["Price"].min()), int(df["Price"].max()))
            )
            df_filtered = df[(df["Price"] >= price_range[0]) & (df["Price"] <= price_range[1])]
            st.dataframe(df_filtered)  # Display filtered data

        except FileNotFoundError:
            # Inform user if CSV file is missing
            st.warning("Property CSV file not found. Please upload 'properties.csv' to view property listings.")

    # ----- Tab 2: ROI Calculator -----
    with tab2:
        st.header("Investment ROI Calculator")

        # Input fields for investment values
        price = st.number_input("Purchase Price ($)", min_value=10000.0, step=1000.0)
        income = st.number_input("Monthly Rental Income ($)", min_value=0.0, step=100.0)
        expenses = st.number_input("Monthly Expenses ($)", min_value=0.0, step=100.0)

        # Calculate ROI on button click
        if st.button("Calculate ROI"):
            roi = calculate_roi(price, income, expenses)
            st.success(f"Estimated ROI: {roi:.2f}%")

    # ----- Tab 3: Contact Form -----
    with tab3:
        st.header("Contact Jarvis2")
        with st.form("contact_form"):
            # Form fields for contacting
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")

            # Simulate sending form
            if submitted:
                process_contact_form(name, email, message)

# Run the app
if __name__ == "__main__":
    main()
