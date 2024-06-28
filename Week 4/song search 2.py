import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1])
                        
i = response.json()
for result in i["results"]:
    print(result["trackName"])

