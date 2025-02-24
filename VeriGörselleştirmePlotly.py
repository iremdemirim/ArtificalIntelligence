# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:10:35 2025

@author: iremd
"""

import plotly.express as px  # Plotly Express kütüphanesini içe aktarma
import pandas as pd  # Veri işleme için Pandas
import webbrowser

# Örnek veri seti
df = px.data.gapminder()

# Box plot çizimi
fig = px.box(df, x="continent", y="gdpPercap", title="Kıtalara Göre GDP Dağılımı")
fig.write_html("box_plot.html")
webbrowser.open("box_plot.html")

# Violin plot çizimi
fig = px.violin(df, x="continent", y="gdpPercap", box=True, points="all", title="Kıtalara Göre GDP Dağılımı (Violin Plot)")
fig.write_html("violin_plot.html")
webbrowser.open("violin_plot.html")

#Line plot çizimi
# Yıllara göre kıtaların ortalama yaşam süresi
df_avg = df.groupby(["year", "continent"], as_index=False).agg({"lifeExp": "mean"})

# Daha temiz bir çizgi grafiği oluşturma
fig = px.line(df_avg, x="year", y="lifeExp", color="continent", markers=True,
              title="Yıllara Göre Ortalama Yaşam Süresi (Kıtalar Bazında)")
fig.write_html("line_chart.html")
webbrowser.open("line_chart.html")

# Bar chart çizimi
fig = px.bar(df, x="continent", y="pop", title="Kıtalara Göre Nüfus")
fig.write_html("bar_chart.html")
webbrowser.open("bar_chart.html")

# Pie chart çizimi
fig = px.pie(df, names="continent", values="pop", title="Kıtalara Göre Nüfus Dağılımı")
fig.write_html("pie_chart.html")
webbrowser.open("pie_chart.html")