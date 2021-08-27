import requests
import json
import numpy as np
import pandas as pd
from readKey import read_key

API_KEY = ""
AUTHOR_ID = "22941628100"
INST_TOKEN = ""

API_KEY, INST_TOKEN = read_key()

url = f'https://api.elsevier.com/content/author/author_id/{AUTHOR_ID}'
response = requests.get(url,
                        headers={'Accept':'application/json',
                                'X-ELS-APIKey': API_KEY,
                                'X-ELS-Insttoken': INST_TOKEN})
result = response.json()
#print(json.dumps(result, indent=4, sort_keys=True))
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

