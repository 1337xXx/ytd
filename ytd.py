import youtube_dl
import ffmpeg

ydl_opts={}

def dwl_vid(): 
	try:
    			with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        			ydl.download([a])
	except Exception as e:
				print("\n---------------------------------------------F A I L E D---------------------------------------------\n ")
				print(e)
ch=1
while(ch==int(1)):
	print("---------------------------------------------YOUTUBE DOWNLOADER v2.3.31--------------------------------------------- \n.What do you want?\n1.Video\n2.Audio\n")
	ho=int(input())
	if(ho==1):
		print("---------------------------------------------VIDEO MODE---------------------------------------------\n1.Good Quality\n2.Data Saver\nEnter your choice: ")
		yo=int(input())
		print("\nEnter download location(enter the drive)\n")
		d=input()
		ydl_opts['outtmpl']=d+":\%(title)s.%(ext)s"
		if(yo==1):
			ydl_opts['format']='bestvideo+bestaudio'
		else:
			ydl_opts['format']='best'
	if(ho==2):
		print("---------------------------------------------AUDIO MODE---------------------------------------------\n")
		print("\nEnter download location enter the drive)\n")
		e=input()
		ydl_opts['outtmpl']=e+":\%(title)s.%(ext)s"
		ydl_opts['format']='bestaudio[ext=m4a]'
		ydl_opts['postprocessors']=[{
					'key': 'FFmpegExtractAudio',
        					'preferredcodec': 'mp3',
        					'preferredquality': '192',
        				        }]
	link=input("Link:?")
	a=link.strip()
	dwl_vid()
	
	ch=int(input("\nIf you want to download more files press 1 \nTo exit press 0"))
