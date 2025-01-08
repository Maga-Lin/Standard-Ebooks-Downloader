import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_standard_ebooks():
    # 存储所有找到的链接
    all_links = set()
    base_url = "https://standardebooks.org/ebooks"
    
    # 遍历24页
    for page in range(1, 25):
        # 构建URL
        url = f"{base_url}?page={page}&per-page=48&sort=author-alpha&view=list"
        
        try:
            # 发送请求
            response = requests.get(url)
            response.raise_for_status()
            
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 查找所有带有property="schema:url"属性的链接
            links = soup.find_all('a', attrs={'property': 'schema:url'})
            
            # 提取href属性并添加到集合中
            for link in links:
                all_links.add(link['href'])
            
            print(f"已完成第 {page} 页的爬取")
            
            # 添加延时以避免请求过快
            time.sleep(1)
            
        except Exception as e:
            print(f"爬取第 {page} 页时出错: {str(e)}")
    
    # 将链接转换为DataFrame
    df = pd.DataFrame(list(all_links), columns=['url'])
    
    # 保存为CSV文件
    df.to_csv('standard_ebooks_links.csv', index=False)
    print(f"共爬取到 {len(all_links)} 个唯一链接，已保存到 standard_ebooks_links.csv")

if __name__ == "__main__":
    scrape_standard_ebooks() 