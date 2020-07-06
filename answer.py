import requests
import json

headers = {'key': 'Hop4EEoIaQkI5tL0g*i33A((', 'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
page_num = 1
last_page = False
final_result = None
has_more = True
first_page = True
alist = []
while not last_page:
    url = f'https://stacko.cisco.com/api/2.2/answers?page={page_num}&pagesize=200&order=desc&sort=activity&filter=!6JEiSzM26Iuxi&key=Hop4EEoIaQkI5tL0g*i33A(('
    answerid = requests.get(url.format(page_num=page_num), headers=headers)
    a2=answerid.json()
    if first_page:
        final_result = a2['items']
        first_page = False
    has_more = a2['has_more']
    if not has_more:
        last_page = True
    final_result = final_result + a2['items']  
    page_num = page_num + 1
    print(has_more)
a2=answerid.json()
