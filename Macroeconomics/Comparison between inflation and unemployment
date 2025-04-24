import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.font_manager as fm

# إعداد الخط
font_path = "C:/Windows/Fonts/arial.ttf"
font_prop = fm.FontProperties(fname=font_path, size=12)

# دالة لتعديل النص العربي
def ar_text(txt):
    reshaped_text = arabic_reshaper.reshape(txt)
    return get_display(reshaped_text)

# البيانات
years = list(range(2015, 2024))
unemployment_rates = [7.89, 7.80, 7.72, 7.65, 6.51, 7.86, 6.38, 4.82, 4.17]
inflation_rates = [4.91, 4.95, 3.33, 3.94, 3.73, 6.62, 5.13, 6.70, 5.65]

# الرسم
plt.figure(figsize=(10, 6))
plt.plot(years, unemployment_rates, label=ar_text('البطالة (%)'), marker='o', color='blue')
plt.plot(years, inflation_rates, label=ar_text('التضخم (%)'), marker='s', color='orange')
plt.title(ar_text('مقارنة بين معدل البطالة والتضخم في الهند (2015–2023)'), fontproperties=font_prop)
plt.xlabel(ar_text('السنة'), fontproperties=font_prop)
plt.ylabel(ar_text('النسبة (%)'), fontproperties=font_prop)
plt.legend(prop=font_prop)
plt.grid(True)
plt.tight_layout()
plt.show()

