
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
mpl.rcParams['font.family'] = 'Kozuka Gothic Pro'
#GDPを盾列にします。
cd = pd.DataFrame(\
[[2000, 48.6, 0.64],[2001, 51.3, 1.1], [2002, 53.9, 1.3], [2003, 56.1, 1.4],\
[2004, 58.1, 1.4], [2005, 59.9, 1.7], [2006, 61.3, 1.9], [2007, 62.7, 2.2],\
[2008, 62.7, 2.5], [2009, 60.0 ,2.5], [2010, 54.7, 2.9], [2011, 49.2, 3.8],\
[2012, 41.5, 4.9], [2013, 34.5, 5.0], [2014, 29.6, 4.2], [2015, 26.9, 3.7],\
[2016, 25.3, 3.7], [2017, 24.4, 4.0]],\
columns = ['年', 'シエラレオネのマラリアによる0~4歳の死亡率', 'GDP(10億米ドル)'])
#DF.plotで折れ線が描ける
"""
cd['シエラレオネのマラリアによる0~4歳の死亡率'].plot()
plt.show()
"""


#タイトルや軸ラベルを付ける
cd['シエラレオネのマラリアによる0~4歳の死亡率'].plot()
plt.title('シエラレオネのマラリアによる0~4歳の死亡率')
plt.xlabel('年')
plt.ylabel('死亡率(‰)')
plt.savefig('SLMDeathRate001.png')


#DF.plotではなくてplt.plot(DF)で描く
plt.plot(cd[['シエラレオネのマラリアによる0~4歳の死亡率']])
plt.title('シエラレオネのマラリアによる0~4歳の死亡率')
plt.xlabel('年')
plt.ylabel('死亡率(‰)')
plt.savefig('SLMDeathrate002.png')


"""
#2つのデータを描き、凡例を付ける

cd[['シエラレオネのマラリアによる0~4歳の死亡率', 'GDP(10億米ドル)']].plot(legend=True)

plt.title('シエラレオネのマラリアによる0~4歳の死亡率')
plt.xlabel('年')
plt.ylabel('シエラレオネのマラリアによる0~4歳の死亡率(‰)・GDP')
plt.savefig('SLMDeathrateGDP.png')
"""
#判例を表示する　

#cd[['シエラレオネのマラリアによる0~4歳の死亡率']].plot(legend=True)
cd['GDP(10億米ドル)'].plot(kind='bar')
plt.title('シエラレオネのマラリアによる0~4歳の死亡率とGDP')
plt.xlabel('年')
plt.ylabel('シエラレオネのマラリアによる0~4歳の死亡率(‰)・GDP(10億米ドル)')
plt.savefig('SLMDeathrateGDPbow.png')


cd['GDP(10億米ドル)'].plot(kind='bar')
plt.title('シエラレオネのマラリアによる0~4歳の死亡率とGDP')
plt.xlabel('年')
plt.ylabel('シエラレオネのマラリアによる0~4歳の死亡率(‰)・GDP(10億米ドル)')
plt.savefig('SLMDeathrateGDPbow.png')
