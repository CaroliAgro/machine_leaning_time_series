import youtube_dl
import pandas as pd
import numpy as np

queries = ["machine+learning", "data+science", "kaggle"]

ydl = youtube_dl.YoutubeDL({"ignoreerrors": True})

resultados = []
for query in queries:
    r = ydl.extract_info("ytsearchdate10:{}".format(query), download=False)
    for entry in r['entries']:
        if entry is not None:
            entry['query'] = query
    resultados += r['entries']
resultados = [e for e in resultados if e is not None]

df = pd.DataFrame(resultados)
#colunas = ['title', 'upload_date', 'view_count']
df['upload_date'] = pd.to_datetime(df['upload_date'])
df['tempo_desde_pub'] = (pd.to_datetime("2021-02-10") -
                         df['upload_date']) / np.timedelta64(1, 'D')

pd.set_option("display.max_columns", 73)
df.tail()