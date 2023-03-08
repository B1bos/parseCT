import requests
import csv
import time
import random

t = time.localtime()
current_time = time.strftime("%H_%M_%S", t)


proxies_list = [
    "89.43.31.134:3128",
    "89.232.123.2:3128",
    "88.99.234.110:2021",
    "78.189.172.112:3128",
    "47.254.90.125:8000",
    "43.153.194.76:8001",
    "3.109.238.5:8080",
    "24.230.33.96:3128",
    "23.95.94.41:3128",
    "20.24.43.214:8123",
    "20.210.113.32:8123",
    "20.210.113.32:80",
    "20.206.106.192:8123",
    "20.206.106.192:80",
    "20.205.61.143:8123",
    "20.111.54.16:8123",
    "20.111.54.16:80",
    "195.181.152.71:3128",
    "185.189.14.28:3002",
    "185.15.172.212:3128",
    "169.55.89.6:8123",
    "169.55.89.6:80",
    "167.172.226.251:443",
    "165.227.81.188:9999",
    "165.227.81.188:9982",
    "165.227.81.188:9957",
    "159.203.84.241:3128",
    "158.69.52.218:9300",
    "157.245.27.9:3128",
    "154.85.55.174:3128",
    "144.217.7.157:9300",
    "138.185.46.22:3128",
    "132.226.251.74:8443",
    "128.1.133.69:3128",
    "104.223.135.178:10000",
    "125.17.80.229:8080",
    "129.154.56.212:8088",
    "125.17.80.226:8080",
    "65.108.230.239:42899",
    "201.17.26.54:80",
    "45.84.241.250:3128",
    "130.41.109.158:8080",
    "64.225.4.17:9979",
    "40.119.247.185:80",
    "81.4.125.75:3128",
    "51.79.50.22:9300",
    "187.130.139.197:8080",
    "5.189.184.6:80",
    "13.75.216.118:3128",
    "172.104.117.89:80",
    "103.119.230.60:80",
    "115.96.208.124:8080",
    "20.99.187.69:8443",
    "125.17.80.228:8080",
    "36.92.85.66:8080",
    "125.17.80.227:8080",
    "158.51.121.230:8881",
    "8.219.97.248:80",
    "154.236.179.226:1981",
    "178.216.24.80:55443",
    "212.159.75.75:8118",
    "115.144.102.39:10080",
    "103.245.164.78:3128",
    "103.245.164.79:3128",
    "103.28.224.123:8080",
    "110.145.200.50:10000",
    "117.102.114.130:8080",
    "134.73.184.238:25283",
    "139.255.67.51:3888",
    "154.64.211.145:999",
    "162.250.112.65:8282",
    "163.172.57.246:3128",
    "165.22.3.209:3128",
    "176.9.220.108:8080",
    "186.67.192.246:8080",
    "188.166.175.116:5843",
    "189.90.118.238:3128",
    "198.24.187.93:8001",
    "212.156.123.218:8080",
    "213.32.253.99:8080",
    "51.38.93.100:3128",
    "74.143.86.243:3128",
    "79.110.40.129:8080",
    "95.213.135.148:3128",
    "109.194.101.128:3128",
    "116.203.36.228:8080",
    "165.227.81.188:9985",
    "167.235.154.203:8080",
    "198.27.74.6:9300",
    "20.24.43.214:80",
    "212.129.54.138:3128",
    "218.7.171.91:3128",
    "41.186.44.106:3128",
    "43.229.135.183:8118",
    "43.229.135.25:8080",
    "46.101.13.77:80",
    "5.75.190.15:8080",
    "5.9.139.204:60083",
    "5.9.139.204:60073",
    "5.9.139.204:60029",
    "51.79.50.31:9300",
    "64.225.4.17:9999",
    "64.56.150.102:3128",
    "65.0.160.35:8080",
    "82.66.75.98:49400",
    "87.250.63.172:8118",
    "95.56.254.139:3128",
]


prew_lightning = ''
prew_crazy = ''
prew_mono = ''
prew_proxy = {}


def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 '
        'Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 '
        'Safari/537.36 OPR/45.0.2552.888',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 '
        'Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 '
        'Safari/537.36'
    ]
    return {'User-Agent': random.choice(user_agents)}


def make_request_with_proxy(url, proxy_list, prev_proxy, timeout=4):
    headers = get_random_user_agent()
    response = requests.get(url, headers=headers, proxies=prev_proxy, timeout=timeout)
    if response.status_code == 200:
        return response
    for proxy in proxy_list:
        headers = get_random_user_agent()
        try:
            proxies = {'https': f"{proxy}"}
            response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
            if response.status_code == 200:
                global prew_proxy
                prew_proxy = proxy
                return response

        except requests.exceptions.RequestException as e:
            print(f"Request error with proxy {proxies}: {e}")
    response = requests.get(url, headers=headers)
    return response


def lightning_req():
    global prew_lightning
    url = 'https://api.casinoscores.com/svc-evolution-game-events/api/lightningroulette/latest'
    output_file = f"lightningroulette_{current_time}.csv"
    response = make_request_with_proxy(url, proxies_list, prew_proxy)
    res_json = response.json()
    cur_id = res_json["id"]
    if prew_lightning == cur_id:
        pass
    else:
        prew_lightning = cur_id
        number = res_json["data"]["result"]["outcome"]["number"]
        print(f"lightning_{number}")
        with open("result/" + output_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([number])


def crazytime_req():
    url = "https://api.casinoscores.com/svc-evolution-game-events/api/crazytime/latest"
    output_file = f"crazytime_{current_time}.csv"
    global prew_crazy
    response = make_request_with_proxy(url, proxies_list, prew_proxy)
    res_json = response.json()
    cur_id = res_json["id"]
    if prew_crazy == cur_id:
        pass
    else:
        prew_crazy = cur_id
        number = res_json["data"]["result"]["outcome"]["wheelResult"]["wheelSector"]
        print(f"Crazy_{number}")

        # Write results to CSV file
        with open("result/" + output_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([number])


def monopoli_req():
    global prew_mono
    url = "https://api.casinoscores.com/svc-evolution-game-events/api/monopoly/latest"
    output_file = f"monopoly_{current_time}.csv"
    response = make_request_with_proxy(url, proxies_list, prew_proxy)
    res_json = response.json()
    cur_id = res_json["id"]
    if prew_mono == cur_id:
        pass
    else:
        prew_mono = cur_id
        number = res_json["data"]["result"]["outcome"]["wheelResult"]
        print(f"Mono_{number}")

        # Write results to CSV file
        with open("result/" + output_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([number])


while True:
    lightning_req()
    monopoli_req()
    crazytime_req()
    time.sleep(30)

