import streamlit as st

# Page Configuration
st.set_page_config(page_title="Jarvis – Real Estate Investment Agent", layout="centered")

# Header
st.title("🤖 Meet Jarvis")
st.subheader("Your Smart Real Estate Investment Agent")

# Introduction Section
st.markdown("""
Jarvis is an intelligent digital agent designed to **search**, **analyze**, and **manage real estate investments** on your behalf.

Whether you're a seasoned investor or just getting started, Jarvis helps you make smarter decisions and grow your portfolio — all while saving you time and effort.
""")

# Features
st.header("🛠️ What Jarvis Can Do")

features = {
    "🏡 Property Search": "Finds the best investment opportunities based on your goals and filters.",
    "📈 Investment Analysis": "Evaluates properties for ROI, cap rate, cash flow, and risk profile.",
    "💼 Fund Management": "Manages investor capital with transparency and performance tracking.",
    "🧾 Reporting": "Generates regular updates on property performance and portfolio health.",
    "💰 Fees": "Works for a small percentage of the profits – no hidden costs."
}

for title, description in features.items():
    st.markdown(f"**{title}** – {description}")

# Call to Action
st.header("🚀 Ready to Grow Your Real Estate Portfolio?")
st.markdown("Let Jarvis help you make smarter, data-driven investment decisions.")

if st.button("📩 Contact Jarvis"):
    st.success("An agent will reach out to you shortly!")

# Footer
st.markdown("---")
st.caption("© 2025 Jarvis Investment Agent – Built to maximize your real estate potential.")
