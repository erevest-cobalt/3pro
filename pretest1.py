import json

str = {
  "タピオカ":{
    "値段": 300,
    "売れた数": 15
  },
  "ナタデココ":{
    "値段": 250,
    "売れた数": 20
  },
  "つぶつぶみかんジュース":{
    "値段": 200,
    "売れた数": 22
  }
}

with open('prejson1.json','w')as f:
    json.dump(str, f, ensure_ascii=False)
