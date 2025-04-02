import multiprocessing
import concurrent.futures
import requests
def download_file(url,name):
    print(f"started downloading {name}")
    response=requests.get(url)
    with open(f"file{name}.jpg","wb")as f:
        f.write(response.content)
    return f"finished downloading {name}"

url="https://picsum.photos/2000/3000"

#usual method that takes time
#for i in range(3):
#   download_file(url,i)

#now we use multiprocessing
if __name__=="__main__": #required for windows multiprocessing
    pros=[]
    for i in range(3):
        p=multiprocessing.Process(target=download_file,args=[url,i])
        p.start()
        pros.append(p)
    for p in pros:
        p.join()

#just like we have threadpool executor we have processpool executor as well
if __name__=="__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(5)]
        l2=[i for i in range(5)]
        results=executor.map(download_file,l1,l2)
        for r in results:
            print(r)