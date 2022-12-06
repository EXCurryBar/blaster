import requests
from time import sleep
from faker import Faker
from random import randint, choice
from threading import Thread

fake = Faker("zh_CN")
bank_lst = open("./bank.txt", 'r', encoding="UTF-8").read().split("\n")

def func():
    payload = {
        "seller_code":"6380fed3ebe7a",
        "username": fake.name(),
        "phone" : "09"+str(randint(0,99999999)).zfill(8),
        "content" : choice(bank_lst) + " 02" + str(randint(22000000,99999999)) 
    }
    req = requests.post("https://shopee.tw-opee0.vip/index/index/leaveMsg", data=payload)
    # print(req.json()["msg"], payload)
    print(req.status_code)

while (True):
    t = Thread(target=func, args=())
    t.start()
    sleep(0.05)
