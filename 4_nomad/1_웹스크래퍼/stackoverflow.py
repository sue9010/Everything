from typing import final
from bs4 import BeautifulSoup 
import requests
LIMIT = 50
URL = f"https://indeed.com/jobs?q=python&limit={LIMIT}"