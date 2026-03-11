import streamlit as st
import yfinance as yf

# 1. 網頁基本設定
st.set_page_config(page_title="台積電股價查詢", layout="centered")
st.title("📈 台積電 (2330.TW) 歷史股價查詢")

# 2. 選擇日期
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("起始日期")
with col2:
    end_date = st.date_input("結束日期")

# 3. 按鈕觸發
if st.button("📊 執行查詢"):
    with st.spinner("資料抓取中..."):
        df = yf.download("2330.TW", start=start_date, end=end_date)
        if df.empty:
            st.warning("⚠️ 此區間查無資料。")
        else:
            st.success("成功取得資料！")
            # 畫圖
            st.bar_chart(df['Close'])
