import streamlit as st
from streamlit.connections import SQLConnection
st.write('''conn = st.connection("my_sql", type=SQLConnection)''')
st.connection
