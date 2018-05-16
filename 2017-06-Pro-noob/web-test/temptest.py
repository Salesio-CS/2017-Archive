import requests
import json

from datetime import datetime

def uploadtempraa(temp, hum):

        url = 'http://localhost/tempra_get.php'

        tempraa = {'time':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'temp':temp,'hum':hum}

        json_str = json.dumps(tempraa)
        print(json_str)

        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(tempraa), headers=headers, verify=False)

        print(res)
        pass

def main():
        uploadtempraa(21.8, 39.1)

if __name__ == '__main__':
        main()
