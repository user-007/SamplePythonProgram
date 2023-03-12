import pytube
video_url = "https://www.youtube.com/watch?v=uAHFNuDlcRw&ab_channel=IBMTechnology"
yt = pytube.YouTube(video_url)
stream = yt.streams.first()
stream.download()

