from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper 
import fugashi
# from jisho_api import word
from jisho_api.word import Word

# url = "https://www.youtube.com/watch?v=tE9tSv6Lo-I"

# yt = YouTube(url, on_progress_callback=on_progress)
# print(yt.title)

# ys = yt.streams.get_audio_only()
# ys.download()

tagger = fugashi.Tagger()
# model = whisper.load_model("tiny")
# result = model.transcribe("「母、駅そばっ」第595話 | あたしンち | [ENG sub].m4a", language="japanese",fp16=False)
# # print(result["text"])
# fulltext = tagger(result["text"])

testsentence = '昨日、東京は曇りでしたか。'
tokenisedtext = tagger(testsentence)
# print(tokenisedtext)

for token in tokenisedtext:
   
    r = Word.request(token.surface)
    print(r.data[0].senses[0].english_definitions)
#     # print(f"Surface: {word.surface}")
#     # print(f"Features: {word.feature.lemma}")
#     r = word.request(text)
#     print(r)
    # if hasattr(word, 'part_of_speech'):
    #     print(f"Part of speech: {word.part_of_speech}")
    # else:
    #     print("Part of speech: N/A")
    # print("---")
# looks through a video link you send it to create a transcript, then teases out useful vocab and grammar for everyday speech

