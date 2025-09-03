from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper 
import fugashi

# url = "https://www.youtube.com/watch?v=tE9tSv6Lo-I"

# yt = YouTube(url, on_progress_callback=on_progress)
# print(yt.title)

# ys = yt.streams.get_audio_only()
# ys.download()

tagger = fugashi.Tagger()
model = whisper.load_model("tiny")
result = model.transcribe("「母、駅そばっ」第595話 | あたしンち | [ENG sub].m4a", language="japanese",fp16=False)
# print(result["text"])
words = tagger(result["text"])
for word in words:
    print(f"Surface: {word.surface}")
    print(f"Features: {word.feature}")
    print(f"Part of speech: {word.part_of_speech}")
# looks through a video link you send it to create a transcript, then teases out useful vocab and grammar for everyday speech
