# -*- coding: utf-8 -*-

import urllib.request
import re


# 下载网页
def download(url, user_agent='wswp', num_retries = 2):
    """Download function that also retries 5XX errors"""
    print('Downloading:'+ url)
    headers = {'User-agent': user_agent}
    # 设置代理
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.request.URLError as e:
        print('Download error:'+ e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download(url,user_agent, num_retries - 1)
    return html

# 网站地图爬虫
def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for links in links:
        html = download(links)
if __name__ == '__main__':
    print(download('http://www.v2ex.com/go/qna'))
    print(crawl_sitemap('http://example.webscraping.com/sitemap.xml'))