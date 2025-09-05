from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper 
import fugashi
# from jisho_api import word
from jisho_api.word import Word

# url = "https://www.youtube.com/watch?v=FWqxBg0N738"

# yt = YouTube(url, on_progress_callback=on_progress)
# print(yt.title)

# ys = yt.streams.get_audio_only()
# ys.download()

tagger = fugashi.Tagger()
model = whisper.load_model("tiny")
result = model.transcribe("日本人がよく使う「遠慮」の使い方３つ.m4a", language="japanese",fp16=False)
# print(result["text"])
tokenisedtext = tagger(result["text"])
# print(fulltext)
# testsentence = '昨日、東京は曇りでしたか。'
# tokenisedtext = tagger(fulltext)
# # print(tokenisedtext)

for token in tokenisedtext:
   pos = token.pos.split(',')[0]
   skip_pos = ['助動詞', '助詞', '記号', '補助記号']
   allowed_pos = ['動詞', '名詞']
   
   if token.surface in '、。？！' or pos not in allowed_pos:
     print("skipped ", token.surface)
   else:
          r = Word.request(token.surface)
          if r and r.data:
             print(token.pos,token.surface, r.data[0].japanese[0].reading, r.data[0].senses[0].parts_of_speech, r.data[0].senses[0].english_definitions)
          else:
              print('not found')


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
