import requests
from bs4 import BeautifulSoup
import re
import random
from urllib.parse import quote
from tqdm import tqdm
import csv
from selenium import webdriver
from datetime import date
import os, os.path

browser = webdriver.Chrome('./chromedriver')


def get_todate():
    return date.today()


def selenium_get_Code_104(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    driver.get(url)
    save = driver.page_source
    soup = BeautifulSoup(save, "html.parser")
    page = soup.select('.page-select.js-paging-select.gtm-paging-top')[0].find_all('option')[-1].get('value')
    return page


def read_url(url):
    USER_AGENT_LIST = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
    USER_AGENT = random.choice(USER_AGENT_LIST)
    headers = {'user-agent': USER_AGENT}
    s = requests.Session()
    req = s.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup


def csv_column_104(path_csv, key_txt):
    with open(path_csv + '.csv', mode='a+', newline='', encoding='utf-8-sig') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['日期', '工作名稱', '公司名稱', '公司地址', '薪資', '工作內容', '地區', '經歷', '學歷', '公司人數', '文章編號', '工作網址'])


def find_title_104(key_txt):
    today = get_todate()
    path_csv = "%s" % os.getcwd() + '/' + 'jobs_csv/' + str(today) + key_txt + '_104人力銀行'
    if not os.path.isdir('jobs_csv'):
        os.mkdir('jobs_csv')
        print('建立jobs_csv資料夾完成')
    csv_column_104(path_csv, key_txt)  # 建立行標題
    csv_save = ""
    key = quote(key_txt)
    find_page_url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={0}&order=15&asc=0&page=1&mode=s&jobsource=2018indexpoc&searchTempExclude=2'.format(
        key)
    get_sum_page = int(selenium_get_Code_104(find_page_url))
    print('共有：' + str(get_sum_page) + ' 頁')
    for i in tqdm(range(1, get_sum_page + 1)):  # 讀取進度條
        url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={0}&order=15&asc=0&page={1}&mode=s&jobsource=2018indexpoc&searchTempExclude=2'.format(
            key, i)
        # 隨機等待
        soup = read_url(url)  # 讀取網頁
        print('目前爬取頁面是：' + url)
        for title_1 in soup.select('.b-block__left'):
            if title_1.select('.b-list-inline.b-clearfix.job-list-item__company') != soup.select('.b-block__left')[
                0].select('.b-list-inline.b-clearfix.job-list-item__company'):
                # 日期
                try:
                    # 正常代表找到 讚 廣告 (業主買廣告)，發生異常代表找不到 讚，執行except找日期
                    date_match__ = title_1.select('.b-icon--gray.b-icon--w18')[0].select('use')[0]
                    date = '廣告'
                except:
                    date = title_1.select('.b-tit__date')[0].get_text().replace('\n', '').replace(' ', '')

                # 地區
                area = title_1.select('.b-list-inline.b-clearfix.job-list-intro.b-content')[0].find('li').get_text()
                # 經歷
                experience = title_1.select('.b-list-inline.b-clearfix.job-list-intro.b-content')[0].find_all('li')[
                    1].get_text()
                try:  # 業者沒有輸入學歷，遇到錯誤處理
                    # 學歷
                    education = title_1.select('.b-list-inline.b-clearfix.job-list-intro.b-content')[0].find_all('li')[
                        2].get_text()
                except:
                    education = ""
                # 工作網址
                title_url = title_1.select('.js-job-link')[0].get('href')[2:]
                # 文章編號
                title_str = title_url.split('?')[0].split('/')[-1]  # get 文章編號
                # 標題名稱
                title = title_1.select('.js-job-link')[0].get_text()  # get title
                # print(title + title_url + area)
                # 公司名
                company_name = title_1.select('li')[1].find('a').get('title').split('\n')[0][4:]
                try:
                    # 公司地址
                    company_address = title_1.select('li')[1].find('a').get('title').split('\n')[1][5:]
                except:
                    company_address = ""
                try:
                    # 簡介
                    introduction = title_1.select('.job-list-item__info.b-clearfix.b-content')[0].get_text()
                    # 處理string \r \n5 \n轉成''
                    introduction = introduction.replace('\r', '').replace('\n5', '').replace('\n', '')
                except:
                    introduction = ""
                # 薪資
                try:
                    salary = title_1.select('.b-tag--default')[0].get_text()
                except:
                    salary = 0  # 沒有寫薪資或待遇面議，設定 0

                if salary == '待遇面議':
                    salary = "待遇面議"
                else:  # 數字處理 25000~35000 取25000最低薪資為主要，三位數 = 日薪，四位數 = 論件計酬
                    try:
                        salary = re.search('\d+.\d+', salary).group()
                    except:
                        salary = 0
                # 員工人數
                try:
                    people = title_1.select('.b-tag--default')[1].get_text()
                except:
                    people = ""
                # clear_output() # 清除輸出 用於清除進度讀，註解#不使用：用來檢查出錯的網址
                with open(path_csv + '.csv', mode='a+', newline='', encoding='utf-8') as employee_file:  # w
                    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    employee_writer.writerow(
                        [date, title, company_name, company_address, salary, introduction, area, experience, education,
                         people, title_str, title_url])
            else:
                continue
    return print('爬取104完成：請開啟csv檔案')


sel = input('請問是否需要爬取104人力銀行:')

while True:
    if sel == '是':
        input_str = input('請輸入要搜尋的關鍵字，取消請輸入否：')
        if input_str == '否':
            print('已經取消')
            break
        find_title_104(input_str)
        break
    elif sel == '否':
        print('已經取消')
        break
    elif sel == '2':
        input_str = input('請輸入要搜尋的關鍵字，取消請輸入0：')
        if input_str == '否':
            print('已經取消')
            break
        print('爬取104')
        find_title_104(input_str)
        break
    else:
        print('請輸入正確的選項：輸入 是或否')
        sel = input('請問是否需要爬取104人力銀行')

os.system('taskkill /im chromedriver.exe /F')
os.system('taskkill /im chrome.exe /F')
