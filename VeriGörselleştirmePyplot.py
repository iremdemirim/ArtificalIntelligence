# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:38:36 2025

@author: iremd
"""

import matplotlib.pyplot as plt
import numpy as np

# Örnek veri
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]
#Grafiği çiz
plt.plot(x, y)
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.title("Örnek denemesi")
#Grafiği göster
plt.show(block=True)

#Çizgi Grafiği
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Çizgi Grafiği")
plt.show(block=True)

#Bar Chart
plt.bar(x, y, color="blue")  # Dikey çubuklar
'''
plt.barh(x, y, color="green")  # Yatay çubuklar
'''
plt.title("Bar Chart")
plt.show(block=True)

#Pie Chart
labels = ["A", "B", "C"]
sizes = [30, 50, 20]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["red", "blue", "green"])
plt.title("Pie Chart")
plt.show(block=True)

#Box-plot
data = [10, 20, 30, 40, 50, 60, 70]
plt.boxplot(data)
plt.title("Box-plot")
plt.show(block=True)


#Violin-plot
# Örnek veri (4 farklı kategori için rastgele dağılım)
np.random.seed(42)  # Rastgeleliği sabitle
data = [np.random.normal(50, 10, 100),  # Ortalama 50, standart sapma 10
        np.random.normal(60, 15, 100),  # Ortalama 60, standart sapma 15
        np.random.normal(40, 5, 100),   # Ortalama 40, standart sapma 5
        np.random.normal(70, 20, 100)]  # Ortalama 70, standart sapma 20

# Violin grafiğini çiz
plt.figure(figsize=(8, 5))
plt.violinplot(data, showmeans=True, showmedians=True)

# Ekseni ayarla
plt.xticks([1, 2, 3, 4], ["Kategori A", "Kategori B", "Kategori C", "Kategori D"])
plt.xlabel("Kategoriler")
plt.ylabel("Değerler")
plt.title("Violin Plot - Veri Dağılımı")

# Göster
plt.show(block=True)























