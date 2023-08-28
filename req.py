import requests

link = 'http://127.0.0.1:8000/healthcheck/'
r = requests.get(link)
print(r.text)


link_2 = 'http://127.0.0.1:8000/sumofnumbers/?num1=5&num2=10'
r_2 = requests.get(link_2)
print(r_2.text)
