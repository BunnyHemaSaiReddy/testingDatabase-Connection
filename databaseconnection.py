import streamlit as st
db_config = st.secrets["mysql"]
con = st.connection('mysql', type='sql')
