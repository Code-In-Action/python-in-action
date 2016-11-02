import urllib.request
def download(url, num_retries = 2):
    """Download function that also retries 5XX errors"""
    print('Downloading:'+ url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('Download error:'+ e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download(url, num_retries - 1)
    return html


download('http://baidu.com')