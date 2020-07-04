import requests
import logging
import json
import re
# -----------------------------------------------------------------------------
# 데이터 전송
cookie = input("cookie")
# cookie
url = input("url:")
# url
data = input("payload:")
# payload
headers = {'Content-Type' : 'text/xml',
          'Cookie' : cookie
          }
# headers / cookie
# -----------------------------------------------------------------------------

responseText = (requests.post(url, headers=headers, data=data)).text