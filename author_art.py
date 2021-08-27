import requests
import json
import numpy as np
import pandas as pd

API_KEY = "e5cb8edc6bea5b5ff8098cd18ca780bb"
AUTHOR_ID = "22941628100"
INST_TOKEN = "8ecf8b976fb67bcdb3eb1cf3e2f09088"
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
    