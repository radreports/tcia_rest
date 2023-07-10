from tcia_utils import nbia
import pandas as pd
import requests

nbia.getToken()

data = nbia.getSeries(collection = "ACRIN-NSCLC-FDG-PET", 
                      api_url = "restricted")

print(len(data), 'Series returned')

df = nbia.downloadSeries(data, api_url = "restricted", format = "df")
# display(df)