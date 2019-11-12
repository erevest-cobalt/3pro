#2019年10月17日作成
#MaraliaDeaths001.csvを2017年度のみでスライス
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
import csv

csv_file = open("./MaraliaDeaths001.csv", "r", encoding="utf_8", errors="", newline="")
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

df = pd.read_csv('./MaraliaDeaths001.csv',index_col=0)
df1=(df[['2017']])#新しいcsvを作る。#これでええんか ?
df1.to_csv('write_MD2017.csv')
