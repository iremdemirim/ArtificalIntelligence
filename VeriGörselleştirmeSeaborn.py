# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:42:36 2025

@author: iremd
"""
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")  # Grafik stilini belirleme
data = sns.load_dataset("tips")  # Örnek veri seti yükleme
sns.scatterplot(x="total_bill", y="tip", data=data)  # Dağılım grafiği çizme
plt.show()

# Örnek veri seti
data = sns.load_dataset("tips")

# Box plot çizimi
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Günlere Göre Toplam Hesap Dağılımı")
plt.show(block=True)

# Violin plot çizimi
sns.violinplot(x="day", y="total_bill", data=data)
plt.title("Günlere Göre Toplam Hesap Dağılımı (Violin Plot)")
plt.show(block=True)

# Örnek veri
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "x": np.arange(1, 11),
    "y": np.random.randint(10, 100, 10)
})

# Çizgi grafiği çizimi
sns.lineplot(x="x", y="y", data=df)
plt.title("Örnek Çizgi Grafiği")
plt.show(block=True)

# Bar chart çizimi
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Günlere Göre Ortalama Hesap")
plt.show(block=True)

# Pie chart için veri hazırlama
day_counts = data["day"].value_counts()
# Pie chart çizimi
plt.pie(day_counts, labels=day_counts.index, autopct="%.1f%%")
plt.title("Günlere Göre Sipariş Dağılımı")
plt.show(block=True)














