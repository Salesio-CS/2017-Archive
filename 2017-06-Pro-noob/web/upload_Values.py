import requests
import json

from datetime import datetime

def upload_data(temp, hum):

        url = 'http://192.168.10.13:8080/web/all_Values.php'

        sensorValues = {'recorded_at':datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'temp':temp, 'hum':hum}

        json_str = json.dumps(sensorValues)
        print(json_str)

        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(sensorValues), headers=headers, verify=False)

        print(res)
        pass

def main():
    upload_data(0);
    
if __name__ == '__main__':
        main()
