import requests
import json


def send(data):
    obj = str(data)
    requests.post('http://127.0.0.1:5000/api/main', json=obj)


probe = {"fullname":"George","characteristics":{"sex":"male","age":27},"skills":["smart","strong"],"experience":[{"position":"developer","workplace":"netflix","salary":"7000"},{"position":"engineer","workplace":"facebook","id_card":56117,"Country":"Scotland"}]}
send(probe)