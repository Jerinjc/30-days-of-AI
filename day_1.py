import streamlit as st

st.title(":material/vpn_key: Day 1: Connect to Snowflake")

# Auto-detect environment and connect
try:
    # Works in Streamlit in Snowflake(Sis)
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Query Snowflake version
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]

# Display results
st.success(f"Successfully connected! Snowflake version: {version}")