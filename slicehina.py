#同じディレクトリ内のCSVファイルをスライスします。
#年別にスライスされたデータはコピペして使います。
#わからないことがあったらいつでも言ってください。
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
import csv

csv_file = open("./スライスしたいデータの名前.csv", "r", encoding="utf_8", errors="", newline="")
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
#f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(f)
#print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
   print(row)

df = pd.read_csv('./スライスしたいデータの名前(上と同じ).csv',index_col=0)
df1=(df[['縦列のデータの名前']])#新しいcsvを作る。[['欲しい']]
df1.to_csv('出力するスライスされたデータの名前.csv')#スライスされたcsvファイルを新しい名前のcsvとして保存
