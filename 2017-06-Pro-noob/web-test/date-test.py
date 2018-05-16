import requests
import json

from datetime import datetime

def upload_data(temp, hum):

        url = 'http://192.168.10.13:8080/web-test/date-test.php'

        date_test = {'recorded_at':datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'temp':temp, 'hum':hum}

        json_str = json.dumps(date_test)
        print(json_str)

        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(date_test), headers=headers, verify=False)

        print(res)
        pass

def main():
        upload_data(5.2, 42.1)

if __name__ == '__main__':
        main()
