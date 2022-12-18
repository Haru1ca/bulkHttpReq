import ctypes, threading, time, re, os, sys
import multiprocessing.dummy as ThreadPool
import requests, socks
from random import choice
import json, fake_useragent
from urllib3 import disable_warnings
from colorama import Fore, init
from time import gmtime, sleep, time, strftime
import random
disable_warnings()
proxies_json = {}

def bulkHttpReq(proxies, type):

    class stats:
        invalid = 0
        working = 0

    def check(x):
        titlebar_changer()
        ua = fake_useragent.UserAgent().random
        header = {'User-Agent': ua}
        proxy = proxies[x].strip()
        if proxy.count(':') == 3:
            spl = proxy.split(':')
            proxy = f"{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}"
        elif type == 'http' or type == 'https':
            proxy_dict = {'http':f"http://{proxy}",  'https':f"https://{proxy}"}
        else:
            proxy_dict = {'http':f"{type}://{proxy}",  'https':f"{type}://{proxy}"}
        try:
            tmp = ''.join(random.sample(string.ascii_letters, 16)).lower()
            r = requests.get(url='url', proxies=proxy_dict, headers=header, timeout=8, verify=False)
            if r.status_code == 200:
                stats.working += 1
                print(f"{Fore.GREEN}[Working]{proxy}")
            else:
                stats.invalid += 1
                print(f"{Fore.RED}[Failed]{proxy}")
        except Exception as e:
            try:
                stats.invalid += 1
                print(f"{Fore.RED}[Failed]{proxy}")
            finally:
                e = None
                del e

        titlebar_changer()

    running = True

    def titlebar_changer():
        ctypes.windll.kernel32.SetConsoleTitleW('bulkHttpReq | (1t) Done/Left: ' + str(stats.invalid + stats.working) + '/' + str(len(proxies) - (stats.invalid + stats.working)) + ' | Working: ' + str(stats.working) + ' | Bad: ' + str(stats.invalid))

    def thread_starter(numbers, threads=threads):
        pool = ThreadPool(threads)
        results = pool.map(check, [numbers])
        pool.close()
        pool.join()
        return results

    thread_number_list = []
    for x in range(0, len(proxies)):
        thread_number_list.append(int(x))

    the_focking_threads = thread_starter(thread_number_list, threads)


def apiproxy():
    while True:
        try:
            type = choice(['socks4', 'socks5', 'http'])
            proxysourcelist = sourcechoice(type)
            text = requests.get(url=(choice(proxysourcelist)), verify=False, headers={'User-Agent': fake_useragent.UserAgent().random}).text
            text = text.replace('\r', '')
            raw_proxies = text.split('\n')
            bulkHttpReq(raw_proxies, type.lower())
        except Exception as e:
            try:
                print(f"{Fore.RED}ApiProxy Failed. Retrying...")
            finally:
                e = None
                del e


def sourcechoice(type):
    if type == 'socks4':
        return [
         'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4',
         'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
         'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
         'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
         'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
         'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
         'https://www.proxy-list.download/api/v1/get?type=socks4',
         'https://www.proxyscan.io/download?type=socks4']
    if type == 'socks5':
        return [
         'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5',
         'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
         'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
         'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
         'https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-socks5.txt',
         'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
         'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
         'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
         'https://www.proxy-list.download/api/v1/get?type=socks5',
         'https://www.proxyscan.io/download?type=socks5']
    return ['https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
     'https://raw.githubusercontent.com/chipsed/proxies/main/proxies.txt',
     'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
     'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt',
     'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt',
     'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
     'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
     'https://raw.githubusercontent.com/proxiesmaster/Free-Proxy-List/main/proxies.txt',
     'https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-http.txt',
     'https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-https.txt',
     'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
     'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
     'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
     'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
     'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
     'https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt',
     'https://www.proxy-list.download/api/v1/get?type=http',
     'https://www.proxy-list.download/api/v1/get?type=https',
     'https://www.proxyscan.io/download?type=http']


if __name__ == '__main__':
    ctypes.windll.kernel32.SetConsoleTitleW('bulkHttpReq V1')
    init()
    t = f"{Fore.LIGHTBLUE_EX}  \n  bulkHttpReq \n{Fore.RESET}"
    print(t)
    threads = int(input('Please input threadsnum\n    >>>') or '2800')
    apiproxy()
