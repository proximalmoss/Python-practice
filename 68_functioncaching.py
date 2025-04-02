#this is used when the computation is expensive and the result is stored in cache once and it is not computed agaim
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
#this is run after interval of 5 secs
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(5))
print("done for 5")
#this is run instantly since values are fetched form cache
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(5))
print("done for 5")
#note:the cache is maintained in only one program run