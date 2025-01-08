# Standard-Ebooks-Downloader
这是一个用于批量下载 [Standard Ebooks](https://standardebooks.org/) 电子书的 Python 项目。项目包含两个主要脚本：一个用于抓取电子书链接，另一个用于自动下载电子书。

## 脚本说明

### web_scraper.py
- 爬取 Standard Ebooks 网站上的所有电子书链接
- 自动处理分页
- 去除重复链接
- 将结果保存为 CSV 文件

### ebook_downloader.py
- 选择下载格式
- 读取 CSV 文件中的链接
- 使用 Selenium 模拟浏览器下载
- 自动处理下载过程
- 支持断点续传
- 显示下载进度和状态
- 执行ebook_downloader(epub).py文件直接下载epub格式文件

## 注意事项

- 请遵守 Standard Ebooks 的使用条款和服务协议
- 下载的电子书仅供个人使用
- 建议使用稳定的网络连接
- 确保磁盘有足够的存储空间这是一个用于批量下载 [Standard Ebooks](https://standardebooks.org/) 电子书的 Python 项目。
