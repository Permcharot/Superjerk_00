# -*- coding: utf-8 -*-
"""Copy of Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZWlk2HcDbA4DNpiFGA-NGbt_dEuYa3zZ
"""

import streamlit as st
import random

st.set_page_config(layout="wide")
st.title('Test Streamlit')

col1, col1_2 = st.columns(2)
with col1:
    st.header("AAAAAA")
with col1_2:
    st.header("BBBBBB")

col2_1, col2_2 = st.columns([3, 1], border=True)
col2_1.header("CCCCCC")
col2_2.header("DDDDDD")