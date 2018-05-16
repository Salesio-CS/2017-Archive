import requests
import json

from datetime import datetime

def uploadtest01(name, price):

        url = 'http://localhost:8080/web/test1.php'

        test01 = {'name':name,'price':price}

        json_str = json.dumps(test01)
        print(json_str)

        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(test01), headers=headers, verify=False)

        print(res)
        pass

def main():
        uploadtest01("OnoderaR", 20)

if __name__ == '__main__':
        main()
