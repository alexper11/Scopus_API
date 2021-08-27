import requests
import json
import numpy as np
import pandas as pd

API_KEY = "e5cb8edc6bea5b5ff8098cd18ca780bb"
AUTHOR_ID = "22941628100"
INST_TOKEN = "8ecf8b976fb67bcdb3eb1cf3e2f09088"

url = f'https://api.elsevier.com/content/author/author_id/{AUTHOR_ID}'
response = requests.get(url,
                        headers={'Accept':'application/json',
                                'X-ELS-APIKey': API_KEY,
                                'X-ELS-Insttoken': INST_TOKEN})
result = response.json()
#print(json.dumps(result, indent=4, sort_keys=True))
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
