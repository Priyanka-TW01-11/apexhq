

On Fri, Jun 26, 2026 at 4:00 PM priyanka j <techwriterp@gmail.com> wrote:
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# --- PREMIUM STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #FFFFFF; }
    .stMetric { background-color: #111111; padding: 20px; border-radius: 12px; border: 1px solid #333; }
    h1, h2 { color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)

st.title("APEX // Executive")

# --- LOGIC: COMPOSITE HEALTH SCORE ---
def get_health_score(revenue, people_metric):
    # Mock algorithm: Weighted average of business performance
    return int((revenue * 0.6) + (people_metric * 0.4))

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["KPI", "Wealth", "Market", "Analytics"])

with tab1:
    st.subheader("Business Health Score")
    health = get_health_score(85, 92)
    st.metric("Composite Health", f"{health}/100", delta="+2 pts")
    st.write("Real-time tracking of revenue, profit, and department health.")

with tab2:
    st.subheader("Financial Analytics")
    st.write("P&L Summary: ₹480 Cr Revenue | ₹85 Cr EBITDA")
    st.progress(85) # Cash flow tracking visual

with tab3:
    st.subheader("Market Intelligence")
    st.info("Competitor 'X' market share dipped 2% this week.")
    st.write("Benchmark: APEX leads in 4/6 industry categories.")

with tab4:
    st.subheader("AI Insights & Alerts")
    st.warning("⚠️ Anomaly: Sales velocity in 'Unit B' is 15% below forecast.")
    if st.button("Export Full Report (PDF/Excel)"):
        st.success("Report generated and sent to your secure email.")

# --- PERSISTENT FOOTER ---
st.markdown("---")
st.caption("APEX v1.0 // Encrypted Access // Last Sync: 15:58 IST")
