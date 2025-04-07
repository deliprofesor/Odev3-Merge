import pandas as pd
import matplotlib.pyplot as plt

# Veriyi yükleyin
df = pd.read_csv('food_data.csv')

# Veri setinin ilk birkaç satırına göz atın
print(df.head())

# Verinin genel yapısını kontrol edin
print(df.info())

# Besin kategorilerine göre gruplama ve ortalama besin değeri hesaplama
grouped_data = df.groupby('description_category')['amount'].mean()

# Veriyi görselleştirme
grouped_data.plot(kind='bar', figsize=(10,6))
plt.title('Ortalama Besin Değerleri - Kategori Bazında')
plt.xlabel('Kategori')
plt.ylabel('Ortalama Miktar')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Her bir besin öğesi için en yüksek ve en düşük değerleri bulma
highest_nutrient = df.loc[df['amount'].idxmax()]
lowest_nutrient = df.loc[df['amount'].idxmin()]

print(f'En yüksek besin değeri: {highest_nutrient["description"]} ({highest_nutrient["amount"]})')
print(f'En düşük besin değeri: {lowest_nutrient["description"]} ({lowest_nutrient["amount"]})')

# Kategorilere göre besin öğesi sayısı
category_counts = df['description_category'].value_counts()

# Kategorilerin bar grafiği
category_counts.plot(kind='barh', figsize=(10,6), color='skyblue')
plt.title('Besin Kategorilerine Göre Dağılım')
plt.xlabel('Kategori Sayısı')
plt.ylabel('Kategori')
plt.tight_layout()
plt.show()
<<<<<<< HEAD


# Assuming you have a 'date' column
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Time series plot
df['amount'].resample('M').mean().plot(figsize=(10,6))
plt.title('Zamanla Ortalama Besin Değeri')
plt.xlabel('Tarih')
plt.ylabel('Ortalama Besin Miktarı')
plt.tight_layout()
plt.show()
=======
<<<<<<< HEAD


category_amounts = df.groupby('description_category')['amount'].sum()
category_amounts.plot(kind='bar', figsize=(10,6), color='lightgreen')

plt.title('Toplam Besin Miktarı Kategori Bazında')
plt.xlabel('Kategori')
plt.ylabel('Toplam Miktar')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

df.boxplot(column='amount', by='description_category', figsize=(10,6), vert=False)
plt.title('Besin Değerlerinin Kategoriye Göre Dağılımı')
plt.suptitle('')
plt.xlabel('Besin Değeri')
plt.tight_layout()
plt.show()


df['amount'].hist(bins=20, figsize=(10,6), color='purple', alpha=0.7)
plt.title('Besin Değerlerinin Dağılımı')
plt.xlabel('Besin Miktarı')
plt.ylabel('Frekans')
plt.tight_layout()
plt.show()
=======
>>>>>>> 46864d1e1e4d3945ee3d2ef087198b074f28c7b1
>>>>>>> feature/new_feature
