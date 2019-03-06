import requests
import json
class RunMethod:
    def post_main(self,url,data,header = None):
        res = None
        if header != None:
            res = requests.post(url = url,data = data,header = header)
        else:
            res = requests.post(url = url,data = data)
        return res.json()
    def get_mian(self,url,data = None,header = None):
        res = None
        if header != None:
            res = requests.get(url=url,data = data,header = header,verify = False)
        else:
            res = requests.get(url=url, data=data,verify=False)
        return res

    def run_main(self,method,url,data = None,header = None):
        res  =None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_mian(url,data,header)
        return res.status_code

