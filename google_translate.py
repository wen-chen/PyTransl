import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        print("Get HTML Text Failed!")
        return 0


def google_translate(to_translate, from_language="en", to_language="ch-CN"):
    #根据参数生成提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)
    
    #获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")
    
    #解析网页得到翻译结果    
    try:
        result = soup.find_all("div", {"class":"t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""
        
    return result

if __name__ == '__main__':
    print(google_translate("Hello World!"))

#你好，世界！