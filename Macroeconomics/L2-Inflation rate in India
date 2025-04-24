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
years = list(range(2015, 2024)) + ['مارس 2025']
inflation_rates = [4.91, 4.95, 3.33, 3.94, 3.73, 6.62, 5.13, 6.70, 5.65, 3.34]

# الرسم
plt.figure(figsize=(10, 5))
plt.plot(years, inflation_rates, marker='s', linestyle='--', color='green')
plt.title(ar_text('معدل التضخم في الهند (2015–مارس 2025)'), fontproperties=font_prop)
plt.xlabel(ar_text('السنة'), fontproperties=font_prop)
plt.ylabel(ar_text('معدل التضخم (%)'), fontproperties=font_prop)
plt.grid(True)
plt.tight_layout()
plt.show()
