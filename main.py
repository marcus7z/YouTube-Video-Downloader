from pytube import YouTube
from tqdm import tqdm
import threading
  
def DownloadFromYT(stream): 
    stream.download()

def DownloadProcess(size):
    length = size
    generator = (3 * n for n in range(length))  
    for n in tqdm(generator, total=length):
        pass
    
link = str(input("Enter Your Link: "))
 
 
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
file_name = yt.title
filesize = yt.streams.get_highest_resolution().filesize  

t1 = threading.Thread(target=DownloadFromYT, args=(stream,))
t2 = threading.Thread(target=DownloadProcess,args=(filesize,))
  
t1.start() 
t2.start()
  
t1.join() 
t2.join()

print("DOWNLOADED !! %s" % file_name)