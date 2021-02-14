import pandas as pd
import numpy as np
import re
import time
import requests as rq
import bs4 as bs4

url = "https://g1.globo.com/"
response = rq.get(url).text
soup = bs4.BeautifulSoup(response, "html.parser")

x = soup.find_all("a")

for i in range(len(x)):
    try:
        if x[i]["class"][0] == "feed-post-link":
            print(x[i].text)
    except:
        continue
