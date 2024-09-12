import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import base64
import os

# 保存先ディレクトリのパスを指定（なければ作成）
save_directory = "uploaded_pdfs"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# ファイルアップロードウィジェットを作成
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # ファイル名を取得して保存パスを設定
    file_path = os.path.join(save_directory, uploaded_file.name)

    # PDFファイルを読み込む
    base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')

    # PDFをiframeで表示
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.components.v1.html(pdf_display)

    # バイナリモードでファイルを保存
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 保存成功メッセージ
    st.success(f"File saved successfully to {file_path}")

    # 保存したファイルの確認
    st.write(f"Saved file path: {file_path}")
