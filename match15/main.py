import time
import math
import pywasm
import random
import requests


def main():
    sums = 0
    headers = {
        "User-Agent": "yuanrenxue.project",
        "Cookie": "sessionid=dvzouncpyjxwjfstvji8bw4taorpa4kl"
    }
    t = int(time.time())
    t1 = int(t / 2)
    t2 = int(t / 2 - math.floor(random.random() * 50 + 1))
    vm = pywasm.load("./main.wasm")
    r = vm.exec("encode", [t1, t2])
    m = f"{r}|{t1}|{t2}"
    for i in range(1, 6):
        params = {
            "m": m,
            "page": i,
        }
        response = requests.get(url="https://match.yuanrenxue.com/api/match/15", params=params, headers=headers).json()
        for each in response["data"]:
            print(each["value"])
            sums += each["value"]
    print(sums)


if __name__ == '__main__':
    main()
