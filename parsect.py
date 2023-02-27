import requests
import csv
import time
import random

t = time.localtime()
current_time = time.strftime("%H_%M_%S", t)


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


# URL to make request
urls = [
    'https://api.casinoscores.com/svc-evolution-game-events/api/lightningroulette/latest',
    'https://api.casinoscores.com/svc-evolution-game-events/api/crazytime/latest',
    'https://api.casinoscores.com/svc-evolution-game-events/api/monopoly/latest'
   ]


# File path to write results to
csv_files = [
    f"lightningroulette_{current_time}.csv",
    f"crazytime_{current_time}.csv",
    f"monopoly_{current_time}.csv"
    ]

prew_lightning = ''
prew_crazy = ''
prew_mono = ''

# Make requests and write results to CSV file every 30 seconds
while True:
    for url, output_file in zip(urls, csv_files):
        headers = get_random_user_agent()
        if url == urls[0]:
            response = requests.get(url, headers=headers)
            res_json = response.json()
            cur_id = res_json["id"]
            if prew_lightning == cur_id:
                continue
            else:
                prew_lightning = cur_id
                number = res_json["data"]["result"]["outcome"]["number"]
                print(f"lightning_{number}")

                # Write results to CSV file
                with open("result/" + output_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([number])
        elif url == urls[1]:
            response = requests.get(url, headers=headers)
            res_json = response.json()
            cur_id = res_json["id"]
            if prew_crazy == cur_id:
                continue
            else:
                prew_crazy = cur_id
                number = res_json["data"]["result"]["outcome"]["wheelResult"]["wheelSector"]
                print(f"Crazy_{number}")

                # Write results to CSV file
                with open("result/" + output_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([number])
        elif url == urls[2]:
            response = requests.get(url, headers=headers)
            res_json = response.json()
            cur_id = res_json["id"]
            if prew_mono == cur_id:
                continue
            else:
                prew_mono = cur_id
                number = res_json["data"]["result"]["outcome"]["wheelResult"]
                print(f"Mono_{number}")

                # Write results to CSV file
                with open("result/" + output_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([number])

    # Wait for 30 seconds before making the next request
    time.sleep(30)
