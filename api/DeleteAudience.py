import json

import requests
import urllib3


def deleteSegmentation():
    env = "https://vmqa-segmentation.audiencecuration.ai"
    path = "/audience/deleteAudience"
    url = env + path

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "X-XSRF-TOKEN": "FtfogpUv-eZlUdHl6T1QOl1dUcIkTbS354d4",
        "Cookie":"dispatchMarkPoint=https%3A%2F%2Fvmqa-portal.audiencecuration.ai; _csrf=yJ7S06sgeob3lkGB6PNyFFuC; NSESSIONID=s%3AdvENajnUavt_9lRanKMUHK483_EvDvG3.NVYnwC4xRHSxFNOK555AKBRS03yyQy%2Fl9UKZAn24OUo; XSRF-TOKEN=FtfogpUv-eZlUdHl6T1QOl1dUcIkTbS354d4"

    }

    requestBody = {
        "folderIdList": [

        ],
        "audienceIdList": [
            "309989","310010"
        ]
    }
    data = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
    requests.packages.urllib3.disable_warnings()
    s = requests.post(url, headers=headers, data=data, verify=False)
    print(type(s))
    # js = s.json()
    print(s.text)

    # if str(js['statusCode']) == "200":
    #     return "演出的评论获取成功"
    # else:
    #     return "演出的评论获取失败"



if __name__ == "__main__":
    aaa = deleteSegmentation()
    print(aaa)
