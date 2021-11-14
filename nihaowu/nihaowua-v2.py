import requests
import random

import time
from lxml import etree
# from fake_useragent import UserAgent

# def get_random_ua(): #随机UA
#     ua = UserAgent()
#     return ua.random
#
# headers = {
#     'User-Agent': get_random_ua()
# }
headers = {
  'authority': 'www.nihaowua.com',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'referer': 'https://qq52o.me/',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'cookie': '_ga=GA1.2.1985649463.1636819525; _gid=GA1.2.36351260.1636819525; Hm_lvt_376df9816305cee7cb5035a2c5a81a8c=1636819525,1636819614; Hm_lpvt_376df9816305cee7cb5035a2c5a81a8c=1636819614'
}

url = 'https://www.nihaowua.com/'

def main(): #写入txt文本程序
    count = 0
    # with open("NiHaoWu1.txt", "a") as f:
    #         while True:
    #             res = requests.get(url=url, headers=headers,timeout=10)
    #             res.encoding = 'utf-8'
    #             selector = etree.HTML(res.text)
    #             xpath_reg = "//section/div/*/text()"
    #             results = selector.xpath(xpath_reg)
    #             content = results[0]
    #             f.write(content + '\n')
    #             count += 1
    #             print('********正在爬取中，这是第{}次爬取********'.format(count))
    while True:
        with open("NiHaoWu2.txt", "a") as f:
                sleep_time=random.random()*2
                time.sleep(sleep_time)
                res = requests.get(url=url, headers=headers,timeout=10)
                res.encoding = 'utf-8'
                selector = etree.HTML(res.text)
                xpath_reg = "//section/div/*/text()"
                results = selector.xpath(xpath_reg)
                content = results[0]
                f.write(content + '\n')
                count += 1
                print('********正在爬取中，这是第{}次爬取********'.format(count))
if __name__ == '__main__':
	main()