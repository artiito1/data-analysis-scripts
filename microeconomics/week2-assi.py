import matplotlib.pyplot as plt
import numpy as np
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.font_manager as fm

font_path = "C:/Windows/Fonts/arial.ttf"  # استخدم خط Arial أو أي خط آخر لديك
font_prop = fm.FontProperties(fname=font_path, size=12)

# بيانات العرض والطلب
wages = np.array([70, 80, 90, 100, 110])  # معدل الأجور بالدولار في الساعة
demand = np.array([320, 300, 240, 200, 180])  # عدد العمال المطلوبين
supply = np.array([150, 200, 240, 280, 320])  # عدد العمال المعروضين

# تحديد نقطة التوازن
equilibrium_wage = 90
equilibrium_quantity = 240

# إعادة تشكيل النصوص العربية
title_ar = get_display(arabic_reshaper.reshape("توازن سوق العمل: تفاعل العرض والطلب"))
xlabel_ar = get_display(arabic_reshaper.reshape("معدل الأجر (دولار في الساعة)"))
ylabel_ar = get_display(arabic_reshaper.reshape("عدد العمال"))
demand_label = get_display(arabic_reshaper.reshape("الطلب على العمالة"))
supply_label = get_display(arabic_reshaper.reshape("العرض من العمالة"))
equilibrium_label = get_display(arabic_reshaper.reshape("نقطة التوازن"))

# رسم المنحنيات
plt.figure(figsize=(8, 6))
plt.plot(wages, demand, 'bo-', label=demand_label)
plt.plot(wages, supply, 'ro-', label=supply_label)
plt.axvline(x=equilibrium_wage, color='gray', linestyle='--', alpha=0.7)
plt.axhline(y=equilibrium_quantity, color='gray', linestyle='--', alpha=0.7)
plt.scatter(equilibrium_wage, equilibrium_quantity, color='black', label=equilibrium_label)

# إضافة التسميات
plt.xlabel(xlabel_ar, fontproperties=font_prop)
plt.ylabel(ylabel_ar, fontproperties=font_prop)
plt.title(title_ar, fontproperties=font_prop)
plt.legend(prop=font_prop)
plt.grid(True)

# عرض الرسم البياني
plt.show()

