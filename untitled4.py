# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QgAmZshyfBuA1hHONPN6ksVo0vPpY3pf
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.set_page_config(layout="wide")
st.title("Test Streamlit")

st.write("Hello World!")

st.write("1 + 1 = ", 2)

st.write(df)