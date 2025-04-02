#Multi threading is used used to run multiple functions or threads at the same time
#This is applied by importing the threading module
#This is most commonly used for I/O bound tasks and not CPU bound tasks
#useful for downloading

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def function(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
#normal exceution of this code with calculating the execution time
time1=time.perf_counter()
func1=function(4)
func2=function(2)
func3=function(1)
time2=time.perf_counter()
print(time2-time1)
#now we use threading and also give the time
time3=time.perf_counter()
t1=threading.Thread(target=function,args=[4])
t2=threading.Thread(target=function,args=[2])
t3=threading.Thread(target=function,args=[1])
#to start the exceution
t1.start()
t2.start()
t3.start()

time4=time.perf_counter()
print(time4-time3)

#now let's say i want to wait 4 seconds and then all of it gets excuted together and the time of exceution should be 4 seconds or the max time given
time5=time.perf_counter()

t4=threading.Thread(target=function,args=[4])
t5=threading.Thread(target=function,args=[2])
t6=threading.Thread(target=function,args=[1])

t4.start()
t5.start()
t6.start()

t4.join()
t5.join()
t6.join()

time6=time.perf_counter()
print(time6-time5)

#now there is another way called thread pool executor
def PoolDemo():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(function,4)
        future2=executor.submit(function,3)
        future3=executor.submit(function,6)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        #now in real world cases we use a list so here let's use a list for all the seconds
        #we use map to apply the fucnction to the list
        l=[5,1,4,3]
        results=executor.map(function,l)
        for result in results:
            print(result)

PoolDemo()