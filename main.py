from tcia_utils import nbia
import pandas as pd
import requests

nbia.getToken()

data = nbia.getSeries(collection = "Head-Neck-PET-CT", 
                      api_url = "restricted")

print(len(data), 'Series returned')

df = nbia.downloadSeries(data, number = 2661, api_url = "restricted", format = "df")
# display(df)