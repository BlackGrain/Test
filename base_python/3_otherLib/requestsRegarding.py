import requests
# r = requests.get("http://www.baidu.com")
# print(r.encoding)
# print(r.text)
# r.encoding = "utf-8"
# print(r.text)

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.text)


