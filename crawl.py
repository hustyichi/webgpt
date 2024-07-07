from firecrawl import FirecrawlApp

API_KEY = ""

app = FirecrawlApp(api_key=API_KEY)

url = "https://docs.dify.ai/v/zh-hans"

crawl_result = app.crawl_url(
    url,
)

# Get the markdown
for idx, result in enumerate(crawl_result):
    print(f"Crawl {idx}st page")
    page_data = result["markdown"]
    # 将 page_data 保存到本地, 以 idx 为文件名
    with open(f"data/page_{idx}.md", "w") as f:
        f.write(page_data)
