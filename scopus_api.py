import requests
import json
import pandas as pd

API_KEY = "e5cb8edc6bea5b5ff8098cd18ca780bb"
url = "https://api.elsevier.com/content/search/scopus?query=af-id(60051434)&sort=citedby-count&start=0&count=25"
def scopus_search(url):
        response = requests.get(url,
                                headers={'Accept':'application/json',
                                        'X-ELS-APIKey': API_KEY})
        result = response.json()

        ids=[]
        titles=[]
        count=[]
        for r in result['search-results']["entry"]:
            
            try:
                ids.append(str(r['prism:issn']))
            except KeyError:
                ids.append('Error al leer ISSN')
            
            titles.append(str(r['dc:title']))
            count.append(str(r['citedby-count']))
                
        return ids, titles, count
    
ids, titles, count=scopus_search(url)
#print(ids)
#print(titles)
dic={'ISSN':ids,'Title':titles, 'Número de citaciones': count}
df = pd.DataFrame(dic)
df.to_excel('issn.xlsx')