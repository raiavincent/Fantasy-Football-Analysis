from sys import argv
from requests import get
import pandas as pd
from bs4 import BeautifulSoup

year = input('What season? Note: Input a season between 1999 and 2020. If not I cannot help you :) ')
week = input('What week of the {0} season? '.format(year))

year, week = int(year), int(week)

