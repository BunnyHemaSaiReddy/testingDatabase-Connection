import streamlit as st
from streamlit.connections import SQLConnection
conn = st.connection("my_sql", type=SQLConnection)

