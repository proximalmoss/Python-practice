import argparse
import requests
def download_file(url, local_file):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open (local_file,'wb') as f: 
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return local_file 

parser=argparse.ArgumentParser()
parser.add_argument('url', help='Url of the file to be downloaded')
parser.add_argument('output', help='by which name do you want to save')

args=parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url,args.output)