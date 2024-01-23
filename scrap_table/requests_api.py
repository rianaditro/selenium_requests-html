"""import requests

url = "https://api.dtm.com/data?query=wigeStandings&raceSeries=DTM&startDate=2023-01-01&endDate=2023-12-31&lang=en"

resp = requests.get(url)

resp_json = resp.json()

print(resp_json)
print(type(resp_json))"""

json = [
  {
    "nationality": "AUT",
    "name": "PREINING Thomas",
    "id": "f1c603bd-b698-4a22-be41-9123b611deeb",
    "position": 1,
    "racepoints": "229",
    "fastestlappoints": "0",
    "qualifyingpoints": "17",
    "totalpoints": "246"
  },
  {
    "nationality": "ITA",
    "name": "BORTOLOTTI Mirko",
    "id": "b25af476-b27c-4ea5-a1a2-c6dea8a73453",
    "position": 2,
    "racepoints": "199",
    "fastestlappoints": "0",
    "qualifyingpoints": "14",
    "totalpoints": "213"
  },
  {
    "nationality": "CHE",
    "name": "FELLER Ricardo",
    "id": "3e26f863-567d-4ee5-b80c-f906d3ed77cb",
    "position": 3,
    "racepoints": "170",
    "fastestlappoints": "0",
    "qualifyingpoints": "9",
    "totalpoints": "179"
  },
  {
    "nationality": "ZAF",
    "name": "VAN DER LINDE Sheldon",
    "id": "d6b5e077-cc8d-4b0b-8a76-6de34862bc2f",
    "position": 4,
    "racepoints": "141",
    "fastestlappoints": "0",
    "qualifyingpoints": "10",
    "totalpoints": "151"
  },
  {
    "nationality": "DEU",
    "name": "RAST Rene",
    "id": "f0685c65-7aa7-4eda-ad5d-6b114fade66e",
    "position": 5,
    "racepoints": "134",
    "fastestlappoints": "0",
    "qualifyingpoints": "6",
    "totalpoints": "140"
  },
  {
    "nationality": "NOR",
    "name": "OLSEN Dennis",
    "id": "25a5c02d-c484-4bc9-8b88-466bd7ec13be",
    "position": 7,
    "racepoints": "128",
    "fastestlappoints": "0",
    "qualifyingpoints": "1",
    "totalpoints": "129"
  }
]
import pandas 

df = pandas.DataFrame(json)

print(df)