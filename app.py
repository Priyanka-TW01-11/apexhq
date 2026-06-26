import streamlit as st

# Force mobile-friendly view
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# --- CUSTOM CSS FOR "MOBILE APP" FEEL ---
st.markdown("""
    <style>
    /* Remove default padding */
    .stApp { background-color: #050505; color: #FFFFFF; }
    
    /* Bottom Navigation Bar */
    .nav-bar {
        position: fixed; bottom: 0; width: 100%; height: 60px;
        background: #111111; display: flex; justify-content: space-around;
        align-items: center; border-top: 1px solid #333;
    }
    .nav-item { color: #888; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

st.title("APEX")
st.write("Welcome, Founder.")

# Create the "App" Navigation
tab1, tab2, tab3 = st.tabs(["Command", "Wealth", "Network"])

with tab1:
    st.subheader("Business KPIs")
    st.metric("Daily Run-rate", "₹4.2L")

with tab2:
    st.subheader("Wealth Cockpit")
    st.write("Equity: ₹450 Cr | Liquid: ₹50 Cr")

with tab3:
    st.subheader("Network")
    st.write("Encrypted CRM")

