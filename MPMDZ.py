
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
mpl.rcParams['font.family'] = 'Kozuka Gothic Pro'
#よっしゃあ!今度からこのフォント使いますうう!
#順調に減ってますねえ…。
#GDPを盾列にします。
cd = pd.DataFrame(\
[[2000, 38.8, 19.1],[2001, 37.9, 7.4], [2002, 38.6, 8.7], [2003, 39.6, 8.9],\
[2004, 41.2, 10.3], [2005, 39.8, 12.0], [2006, 38.5, 14.5], [2007, 33.8, 16.7],\
[2008, 28.7, 19.8], [2009, 24.2, 18.6], [2010, 19.5, 21.6], [2011, 16.0, 25.8],\
[2012, 13.9, 29.3], [2013, 12.9, 32.7], [2014, 12.4, 35.9], [2015, 12.0, 37.9],\
[2016, 11.8, 37.1], [2017,11.4,38.0]],\
columns = ['年', 'コンゴ民主共和国のマラリアによる0~4歳の死亡率', 'GDP(10億米ドル)'])
#DF.plotで折れ線が描ける
"""
cd['コンゴ民主共和国のマラリアによる0~4歳の死亡率'].plot()
plt.show()
"""


#タイトルや軸ラベルを付ける
cd['コンゴ民主共和国のマラリアによる0~4歳の死亡率'].plot()
plt.title('コンゴ民主共和国のマラリアによる0~4歳の死亡率')
plt.xlabel('年')
plt.ylabel('死亡率(‰)')
plt.savefig('CDMDeathRate001.png')


#DF.plotではなくてplt.plot(DF)で描く
plt.plot(cd[['コンゴ民主共和国のマラリアによる0~4歳の死亡率']])
plt.title('コンゴ民主共和国のマラリアによる0~4歳の死亡率')
plt.xlabel('年')
plt.ylabel('死亡率(‰)')
plt.savefig('CDMDeathrate002.png')



#2つのデータを描き、凡例を付ける
cd[['コンゴ民主共和国のマラリアによる0~4歳の死亡率', 'GDP(10億米ドル)']].plot(legend=True)
plt.title('コンゴ民主共和国のマラリアによる0~4歳の死亡率')
plt.xlabel('年')
plt.ylabel('コンゴ民主共和国のマラリアによる0~4歳の死亡率(‰)・GDP')
plt.savefig('CDMDeathrateGDP.png')
