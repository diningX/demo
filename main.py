import pandas as pd
import streamlit as st
import numpy as np

if "file_list" not in st.session_state:
    st.session_state["file_list"] = []

file_name = st.text_input('name')
button = st.button('go')
button_open = st.button('show file')
if button:
    st.session_state["file_list"].append(file_name+'.csv')
    pd.DataFrame(data=np.random.randint(10, size=(5, 5))).to_csv(file_name+'.csv')


if button_open:
    for f in st.session_state["file_list"]:
        st.write(f)
        st.dataframe(pd.read_csv(f))