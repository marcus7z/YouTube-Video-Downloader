from pytube import YouTube
link = str(input("Enter Your Link: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()

from tqdm import tqdm
 
 
for i in tqdm(range(int(9e6))):
    pass


print("DOWNLOADED !!!!")