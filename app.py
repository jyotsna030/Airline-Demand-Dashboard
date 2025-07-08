import streamlit as st
import pandas as pd
import plotly.express as px
from process_data import fetch_flight_data, clean_data
from ai_insights import generate_ai_summary, answer_user_question

# Page config
st.set_page_config(page_title="✈️ Airline Demand Trends", layout="wide")
st.markdown("<h1 style='text-align: center;'>✈️ Airline Booking Demand Dashboard</h1>", unsafe_allow_html=True)

# Search input
with st.container():
    st.subheader("🔍 Search Flights")
    col1, col2 = st.columns(2)
    with col1:
        airport_code = st.text_input("Enter Departure Airport Code", "SYD")
    with col2:
        limit = st.slider("Number of Flights to Fetch", 10, 100, 50)

# Handle Get Flight Data click
if st.button("📡 Get Flight Data"):
    with st.spinner("Fetching live flight data..."):
        try:
            raw_df = fetch_flight_data(dep_iata=airport_code, limit=limit)
            df = clean_data(raw_df)
            st.session_state["flight_df"] = df
            st.session_state.pop("ai_response", None)
            st.success("✅ Data fetched successfully!")
        except Exception as e:
            st.error(f"🚨 Something went wrong: {e}")

# If data exists, render it + visuals + AI
if "flight_df" in st.session_state:
    df = st.session_state["flight_df"]

    st.subheader("📄 Flight Data")
    st.dataframe(df, use_container_width=True)

    # Charts in two columns
    st.subheader("📊 Insights")
    col1, col2 = st.columns(2)

    with col1:
        route_counts = df.groupby(['Departure Airport', 'Arrival Airport']).size().reset_index(name='Flights')
        top_routes = route_counts.sort_values("Flights", ascending=False).head(10)
        fig1 = px.bar(top_routes, x='Flights', y='Arrival Airport',
                      orientation='h', color='Flights',
                      title=f"Top 10 Arrival Airports from {airport_code}")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        airline_counts = df['Airline'].value_counts().reset_index()
        airline_counts.columns = ['Airline', 'Flights']
        fig2 = px.pie(airline_counts.head(5), names='Airline', values='Flights', title="Top 5 Airlines")
        st.plotly_chart(fig2, use_container_width=True)

    # AI Summary (run once)
    if "ai_summary" not in st.session_state:
        st.session_state["ai_summary"] = generate_ai_summary(df)

    st.subheader("🧠 AI Summary")
    st.info(st.session_state["ai_summary"])

    # Ask AI a question
    st.subheader("💬 Ask AI About This Flight Data")
    user_question = st.text_input("Type your question", key="user_q")

    if st.button("🤖 Get AI Answer"):
        with st.spinner("AI is thinking..."):
            st.session_state["ai_response"] = answer_user_question(df, st.session_state["user_q"])

    if "ai_response" in st.session_state:
        st.success(st.session_state["ai_response"])
