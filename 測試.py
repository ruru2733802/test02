requirements.txt
streamlit
yfinance
pandas
# ==========================================
# 1. 系統環境設定 (處理 Matplotlib 中文亂碼問題)
# ==========================================
def set_chinese_font():
    """根據作業系統設定合適的中文字體"""
    system = platform.system()
    if system == 'Windows':
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 微軟正黑體
    elif system == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']    # macOS 預設中文字體
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei'] # Linux 常見開源字體
    
    plt.rcParams['axes.unicode_minus'] = False  # 正常顯示負號

# ==========================================
# 2. 日期格式驗證
# ==========================================
def get_valid_date(prompt):
    """確保使用者輸入正確的 YYYY-MM-DD 格式"""
    while True:
        date_str = input(prompt)
        try:
            # 嘗試解析日期，確認格式正確
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ 格式錯誤！請使用 YYYY-MM-DD 格式 (例如: 2023-05-01)。")

# ==========================================
# 3. 主程式邏輯
# ==========================================
def main():
    print("="*40)
    print(" 📈 台積電 (2330.TW) 歷史股價查詢系統 ")
    print("="*40)
    
    set_chinese_font()
    
    # 取得使用者輸入
    start_date = get_valid_date("請輸入起始日期 (YYYY-MM-DD): ")
    end_date = get_valid_date("請輸入結束日期 (YYYY-MM-DD): ")
    
    print(f"\n⏳ 正在連線抓取 {start_date} 至 {end_date} 的資料，請稍候...\n")
    
    try:
        # 使用 yfinance 抓取台積電(台灣上市代號 2330.TW) 的歷史資料
        # 若你要看美股 ADR，可將 '2330.TW' 改為 'TSM'
        ticker = "2330.TW"
        df = yf.download(ticker, start=start_date, end=end_date)
        
        # 檢查是否有抓到資料 (可能輸入到未來的日期或全為週末)
        if df.empty:
            print("⚠️ 找不到這段期間的交易資料，請確認日期是否包含台股交易日。")
            return
            
        # 繪製長條圖
        plt.figure(figsize=(12, 6)) # 設定畫布大小
        
        # 提取收盤價 (Close) 並畫成長條圖
        dates = df.index
        closes = df['Close'].values.flatten() # 確保資料維度正確
        
        plt.bar(dates, closes, color='#1f77b4', edgecolor='black', alpha=0.8)
        
        # 圖表美化
        plt.title(f'台積電 (2330) 收盤價長條圖\n({start_date} ~ {end_date})', fontsize=16, fontweight='bold')
        plt.xlabel('交易日期', fontsize=12)
        plt.ylabel('股價 (新台幣 TWD)', fontsize=12)
        
        # 針對 X 軸日期文字做 45 度旋轉，避免字擠在一起
        plt.xticks(rotation=45) 
        
        # 加上 Y 軸的水平格線，方便對照價格
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # 自動調整版面配置，確保標籤不會被裁切
        plt.tight_layout()
        
        # 顯示圖表
        print("✅ 繪製完成！請查看彈出的圖表視窗。")
        plt.show()
        
    except Exception as e:
        print(f"❌ 發生未知的錯誤: {e}")

if __name__ == "__main__":
    main()


