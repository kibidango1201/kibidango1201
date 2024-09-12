import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit as st
import base64
pdf_file_path = "sample.pdf"

# PDFファイルの内容を読み込む
with open(pdf_file_path, "rb") as pdf_file:
    pdf_data = pdf_file.read()

# ダウンロードボタンを作成
st.download_button(
    label="Download PDF",
    data=pdf_data,
    file_name="sample.pdf",
    mime="application/pdf"
)

# ファイルアップロードウィジェットを作成
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # PDFファイルを読み込む
    base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')

    # PDFをiframeで表示
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.components.v1.html(pdf_display)

"""
# Title

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
