import GetOldTweets3 as got
import pandas as pd

import os.path
from os import path
from tweets_scraper import *

dates = ["2018-1-1","2017-1-1","2016-1-1","2015-1-1","2014-1-1","2013-1-1","2012-1-1"]



name = "MujtabaaMusaa"
for i in range(1,6):
   tweets_df = hashtag_tweets( name, 10000, dates[i+1], dates[i])


