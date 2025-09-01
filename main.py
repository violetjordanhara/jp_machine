from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper 

# url = "https://www.youtube.com/watch?v=tE9tSv6Lo-I"

# yt = YouTube(url, on_progress_callback=on_progress)
# print(yt.title)

# ys = yt.streams.get_audio_only()
# ys.download()


model = whisper.load_model("base")
result = model.transcribe("「母、駅そばっ」第595話 | あたしンち | [ENG sub].m4a", language="japanese",fp16=False)
print(result["text"])
# looks through a video link you send it to create a transcript, then teases out useful vocab and grammar for everyday speech
