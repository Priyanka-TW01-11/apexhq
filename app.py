import streamlit as st
> st.set_page_config(layout="centered", initial_sidebar_state="collapsed")
>
> # --- PROFESSIONAL LIGHT THEME CSS ---
> st.markdown("""
>     <style>
>     /* Light professional background */
>     .stApp { background-color: #F8F9FA; color: #1E293B; }
>    
>     /* White cards for metrics */
>     .stMetric {
>         background-color: #FFFFFF;
>         padding: 20px;
>         border-radius: 12px;
>         border: 1px solid #E2E8F0;
>         box-shadow: 0 2px 4px rgba(0,0,0,0.05);
>     }
>    
>     /* Headers and font */
>     h1, h2, h3 { color: #0F172A; font-family: sans-serif; }
>    
>     /* Tab Styling */
>     div[data-baseweb="tab-list"] { background-color: #F8F9FA; }
>     </style>
> """, unsafe_allow_html=True)
>
> st.title("APEX // Executive")
>
> # 4-Tab Navigation
> tab1, tab2, tab3, tab4 = st.tabs(["KPI", "Wealth", "Market", "Analytics"])
>
> with tab1:
>     st.subheader("Business Health Score")
>     st.metric("Composite Health", "87/100", delta="+2 pts")
>     st.write("Real-time tracking of revenue, profit, and department health.")
>
> with tab2:
>     st.subheader("Wealth Cockpit")
>     st.write("Consolidated Assets: ₹642 Cr")
>
> with tab3:
>     st.subheader("Market Intelligence")
>     st.write("Tracking competitor benchmarks and industry trends.")

> with tab4:
>     st.subheader("AI Insights")
>     st.warning("⚠️ Anomaly: Unit B sales velocity is 15% below target.")
