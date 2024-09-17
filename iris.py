import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ham dizge kullanarak dosya yolunu belirtin
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Yazılım\googleplaystore.csv")

# İlk birkaç satırı görüntüle
print(df.head())

# Sütun adlarını görüntüle
print(df.columns)

# Boşluk yerine alt tire sembolleri yaz
df.columns = df.columns.str.replace(" ", "_")

print(df.columns)

# Satır ve sütun sayılarını görme
print(df.shape)

# Tipleri görüntüleme
print(df.dtypes)

# Eksik veriler
print(df.isnull().sum()) 

# Seaborn ayarları
sns.set_theme()
sns.set(rc={"figure.dpi":300, "figure.figsize":(12,9)})

# Eksik verileri görselleştirme
sns.heatmap(df.isnull(), cbar=False)

# Grafiklerin gösterilmesi
plt.show()

# Rating sütunundaki eksik verileri median ile doldur
rating_median = df["Rating"].median()
df["Rating"].fillna(rating_median, inplace=True)

# Diğer eksik verileri sil
df.dropna(inplace=True)
print(df.isnull().sum()) 

print(df.info())

# Reviews sütununu integer tipe dönüştür
df["Reviews"] = df["Reviews"].astype("int64")
print(df["Reviews"].describe())

# Size sütunundaki benzersiz değerleri incele
print(len(df["Size"].unique()))
print(df["Size"].unique())

# Size sütunundaki 'M' ve 'k' karakterlerini kaldır
df["Size"] = df["Size"].str.replace("M", "", regex=False)
df["Size"] = df["Size"].str.replace("k", "", regex=False)

# Size sütununda 'Varies with device' olanları median ile doldur
size_median = df[df["Size"] != "Varies with device"]["Size"].astype(float).median()
df["Size"].replace("Varies with device", size_median, inplace=True)

# Size sütununu numerik tipe dönüştür
df["Size"] = pd.to_numeric(df["Size"], errors='coerce')

# İlk birkaç değeri kontrol et
print(df["Size"].head())

print(df.Size.describe().round())

# Installs sütununun dönüşümü
df["Installs"] = df["Installs"].astype(str).apply(lambda x: x.replace("+", "").replace(",", "")).astype(int)
print(df["Installs"].unique())

# Price sütununun dönüşümü
df["Price"] = df["Price"].astype(str).apply(lambda x: x.replace("$", "")).astype(float)
print(df["Price"].unique())

# Genres sütununun dönüşümü
print(len(df["Genres"].unique()))
df["Genres"] = df["Genres"].str.split(";").str[0]
print(len(df["Genres"].unique()))
print(df["Genres"].value_counts())

# Genres sütununda isim değiştirme
df["Genres"].replace("Music & Audio", "Music", inplace=True)
print(df["Genres"].head())

# Last_Updated sütununun tarih dönüşümü
df["Last_Updated"] = pd.to_datetime(df["Last_Updated"], errors='coerce')
print(df.head())

print(df.dtypes)

df["Type"].value_counts().plot(kind="bar",color="red")

sns.boxplot(x = "Type", y ="Rating", data =df)

sns.countplot(y="Content_Rating", data =df)

plt.title("Content rating with their counts")

plt.show()

sns.boxplot(x = "Content_Rating", y = "Rating", data=df)

plt.show()

cat_num = df["Category"].value_counts().sort_values(ascending=False)

# `sns.barplot` ile `x` ve `y` parametrelerinde uygun değerlerin kullanımı
plt.figure(figsize=(10, 8))
sns.barplot(x=cat_num.values, y=cat_num.index)  # `x` ve `y` olarak sayısal değerler ve indeksleri kullanın
plt.title("The number of categories", size=20)
plt.xlabel("Count")
plt.ylabel("Category")
plt.show()

sns.scatterplot(data=df, y = "Category", x = "Price")

# Sadece sayısal sütunları seçmek için:
numeric_df = df.select_dtypes(include=["float64", "int64"])  # Sadece sayısal veriler seçilir

# Seaborn ile korelasyon ısı haritası oluşturma
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, linewidths=.5, fmt=".2f", cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()