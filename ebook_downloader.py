import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# 定义可用的下载格式
FORMAT_OPTIONS = {
    '1': ('Compatible epub', 'epub'),
    '2': ('AZW3', 'azw3'),
    '3': ('Kepub', 'kepub'),
    '4': ('Advanced epub', 'advanced-epub')
}

def get_format_choice():
    while True:
        print("\n请选择下载格式：")
        for key, (name, _) in FORMAT_OPTIONS.items():
            print(f"{key}. {name}")
        
        choice = input("\n请输入选项编号 (1-4): ").strip()
        
        if choice in FORMAT_OPTIONS:
            return FORMAT_OPTIONS[choice][1]
        else:
            print("无效的选择，请重试。")

def setup_chrome_driver():
    # 设置Chrome选项
    chrome_options = Options()
    
    # 设置下载路径
    download_path = os.path.abspath("downloaded_ebooks")
    os.makedirs(download_path, exist_ok=True)
    
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # 创建Chrome驱动（使用webdriver_manager自动管理）
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def download_ebooks():
    driver = None
    try:
        # 获取用户选择的格式
        format_type = get_format_choice()
        print(f"\n已选择格式: {format_type}")
        
        # 读取CSV文件
        df = pd.read_csv('standard_ebooks_links.csv')
        total_books = len(df['url'])
        print(f"开始下载，共有 {total_books} 本书")
        
        # 设置浏览器
        driver = setup_chrome_driver()
        
        # 处理每个链接
        for index, url in enumerate(df['url'], 1):
            try:
                # 构建下载链接
                download_url = f"https://standardebooks.org{url}/download?format={format_type}"
                print(f"\n正在处理第 {index}/{total_books} 本书")
                print(f"下载链接: {download_url}")
                
                # 访问下载链接
                driver.get(download_url)
                
                # 等待一段时间确保下载开始
                time.sleep(3)
                
                print(f"已触发下载")
                
            except Exception as e:
                print(f"下载失败: {str(e)}")
            
            # 在下载之间添加延时
            time.sleep(2)
        
        # 最后等待一段时间确保所有下载完成
        print("\n等待最后的下载完成...")
        time.sleep(10)
        
    except Exception as e:
        print(f"发生错误: {str(e)}")
    
    finally:
        # 安全关闭浏览器
        if driver:
            driver.quit()

if __name__ == "__main__":
    download_ebooks() 