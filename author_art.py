import requests
import json
import numpy as np
import pandas as pd
from readKey import read_key

API_KEY = ""
AUTHOR_ID = "22941628100"
INST_TOKEN = ""

API_KEY, INST_TOKEN = read_key()
S = 0

def get_articles(autorid, s):
        global S
        url = f'https://api.elsevier.com/content/search/scopus?query=au-id({autorid})&start={s}&count=190'
        response = requests.get(url,
                                headers={'Accept':'application/json',
                                        'X-ELS-APIKey': API_KEY,
                                        'X-ELS-Insttoken': INST_TOKEN})
        
        result = response.json()
        TotalArt = int(result['search-results']['opensearch:totalResults'])
        issn=[]
        titles=[]
        doi=[]
        for r in result['search-results']["entry"]:
            try:
                issn.append(str(r['prism:issn']))
            except KeyError:
                issn.append('')
                
            titles.append(str(r['dc:title']))
            
            try:
                doi.append(str(r['prism:doi']))
            except KeyError:
                doi.append('')
            
            
        dic={'ISSN':issn,'Title':titles, 'DOI': doi}
                
        if s==0:
            S = 25
            return TotalArt, dic
        else:
            return dic
        
Total, dic = get_articles(AUTHOR_ID, S)

""""
while S <= Total:
    temp = {}
    temp = get_articles(AUTHOR_ID, S)
    for data in temp.keys():
                dic[data].extend(temp[data])
    S +=25
""" 

df = pd.DataFrame(dic)
df.to_excel(f'{AUTHOR_ID}.xlsx')
    