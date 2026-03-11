import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date, timedelta

# 設定網頁標題與寬度
st.set_page_config(page_title="台積電股價查詢", layout="centered")

st.title("📈 台積電 (2330.TW) 歷史股價查詢系統")
st.markdown("這是一個使用 Streamlit 打造的簡單股價查詢工具。")

# 使用 Streamlit 的左右排版與日期選擇器
col1, col2 = st.columns(2)
with col1:
    # 預設起始日期為 30 天前
    default_start = date.today() - timedelta(days=30)
    start_date = st.date_input("請選擇起始日期", default_start)
with col2:
    # 預設結束日期為今天
    end_date = st.date_input("請選擇結束日期", date.today())

# 當使用者點擊按鈕時才執行抓取資料
if st.button("📊 產生長條圖"):
    if start_date > end_date:
        st.error("❌ 起始日期不能晚於結束日期喔！")
    else:
        # 顯示載入中的動畫
        with st.spinner(f"正在連線抓取 {start_date} 至 {end_date} 的資料..."):
            ticker = "2330.TW"
            df = yf.download(ticker, start=start_date, end=end_date)
            
            if df.empty:
                st.warning("⚠️ 找不到這段期間的交易資料，可能是假日或未來日期。")
            else:
                # 為了避免多重欄位 (MultiIndex) 造成圖表錯誤，我們只取 Close 並轉成單純的 Series
                close_prices = df['Close'].squeeze()
                
                st.success("✅ 繪製完成！")
                # 使用 Streamlit 內建的互動式長條圖，自帶滑鼠 hover 效果
                st.bar_chart(close_prices)import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date, timedelta

# 設定網頁標題與寬度
st.set_page_config(page_title="台積電股價查詢", layout="centered")

st.title("📈 台積電 (2330.TW) 歷史股價查詢系統")
st.markdown("這是一個使用 Streamlit 打造的簡單股價查詢工具。")

# 使用 Streamlit 的左右排版與日期選擇器
col1, col2 = st.columns(2)
with col1:
    # 預設起始日期為 30 天前
    default_start = date.today() - timedelta(days=30)
    start_date = st.date_input("請選擇起始日期", default_start)
with col2:
    # 預設結束日期為今天
    end_date = st.date_input("請選擇結束日期", date.today())

# 當使用者點擊按鈕時才執行抓取資料
if st.button("📊 產生長條圖"):
    if start_date > end_date:
        st.error("❌ 起始日期不能晚於結束日期喔！")
    else:
        # 顯示載入中的動畫
        with st.spinner(f"正在連線抓取 {start_date} 至 {end_date} 的資料..."):
            ticker = "2330.TW"
            df = yf.download(ticker, start=start_date, end=end_date)
            
            if df.empty:
                st.warning("⚠️ 找不到這段期間的交易資料，可能是假日或未來日期。")
            else:
                # 為了避免多重欄位 (MultiIndex) 造成圖表錯誤，我們只取 Close 並轉成單純的 Series
                close_prices = df['Close'].squeeze()
                
                st.success("✅ 繪製完成！")
                # 使用 Streamlit 內建的互動式長條圖，自帶滑鼠 hover 效果
                st.bar_chart(close_prices)