import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ham dizge kullanarak dosya yolunu belirtin
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Yazılım\iris.csv")

# İlk birkaç satırı görüntüle
print(df.head())

# Boşluk yerine alt tire sembolleri yaz
df.columns = df.columns.str.replace(".", "_")

print(df.columns)

"""
# Eksik veriler
print(df.isnull().sum()) 

# Seaborn ayarları
sns.set_theme()
sns.set(rc={"figure.dpi":100, "figure.figsize":(4,3)})

# Eksik verileri görselleştirme
sns.heatmap(df.isnull(), cbar=False)

# Grafiklerin gösterilmesi
plt.show()

EKSİK VERİ OLMADIĞI İÇİN BU ŞEKİLDE AYARLADIK
"""

sns.countplot(y="variety", data =df)

plt.title("Content rating with their counts")

plt.show()