import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 作成')

st.write("Dataframe")

img = Image.open("スクリーンショット 2024-06-01 194029.png")
st.image(img,caption = "man image",use_column_width = True)
