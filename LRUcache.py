import time
from functools import lru_cache


# @lru_cache(maxsize=3)
# def printn(n):
#     time.sleep(n)
#     print(n)  # n is not printed after caching


@lru_cache(maxsize=3)
def printn(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("calling first time...")
    printn(3)
    print("calling second time...")
    printn(3)
