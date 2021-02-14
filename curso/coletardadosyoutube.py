import pandas as pd
import numpy as np
import re
import time
import requests as rq
import bs4 as bs4

queries = ["machine+learning", "data+science", "kaggle"]
url = "https://www.youtube.com/results?search_query={query}&sp=CAI%253D&p={page}"

for query in queries:
    for page in range(1, 101):
        urll = url.format(query=query, page=page)
        print(urll)
        response = rq.get(urll)

        with open("./dadosbrutos/{}_{}.html".format(query, page),
                  "w+",
                  encoding='utf8') as output:
            output.write(response.text)
        time.sleep(2)
