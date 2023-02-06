import base64
from tqdm import tqdm
import time


def d_e_f(n):
    p_bar()
    with open(n, "r") as f:
        for l in f:
            b = l[::-1]
            a = base64.b64decode(b).decode()
            print(a,  end = '')
    print("\n")


def p_bar():
    for i in tqdm(range(100),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)
    print("\n\033[92m.................... Secrets have been exposed .....................\033[0m")


def f_n():
    print("Filename?: ", end = '')
    n = input()
    return n


if __name__ == '__main__':
    m = f_n()
    d_e_f(m)
