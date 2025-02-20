import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# إعداد الخط العربي
font_path = "C:/Windows/Fonts/arial.ttf"  # تأكد من أن هذا المسار صحيح لخط Arial أو استخدم خطًا عربياً آخر
font_prop = fm.FontProperties(fname=font_path, size=12)

def reshape_text(text):
    return get_display(arabic_reshaper.reshape(text))

# البيانات للمرونة السعرية (PED)
price_old = 50
price_new = 60
quantity_old_ped = 150
quantity_new_ped = 100

# البيانات لمرونة الدخل (YED)
income_old = 3000
income_new = 3500
quantity_old_yed = 150
quantity_new_yed = 180

# البيانات للمرونة المتقاطعة (XED)
competitor_price_old = 55
competitor_price_new = 50
quantity_old_xed = 150
quantity_new_xed = 130

# إنشاء الرسوم البيانية
fig, axs = plt.subplots(1, 3, figsize=(20, 5))

# ---------------------------
# 1. رسم المرونة السعرية (PED)
# ---------------------------
axs[0].plot([price_old, price_new], [quantity_old_ped, quantity_new_ped], marker='o', color='red', linestyle='--')
axs[0].set_title(reshape_text('المرونة السعرية للطلب (PED)'), fontproperties=font_prop)
axs[0].set_xlabel(reshape_text('السعر (دولار)'), fontproperties=font_prop)
axs[0].set_ylabel(reshape_text('الكمية المطلوبة'), fontproperties=font_prop)
axs[0].grid(True)
axs[0].annotate(reshape_text('PED = -2.2\n(مرونة عالية)'), 
                xy=(price_new, quantity_new_ped), 
                xytext=(55, 130), 
                arrowprops=dict(facecolor='black', shrink=0.05), 
                fontproperties=font_prop)

# ---------------------------
# 2. رسم مرونة الدخل (YED)
# ---------------------------
axs[1].plot([income_old, income_new], [quantity_old_yed, quantity_new_yed], marker='o', color='green', linestyle='--')
axs[1].set_title(reshape_text('مرونة الدخل للطلب (YED)'), fontproperties=font_prop)
axs[1].set_xlabel(reshape_text('الدخل الشهري (دولار)'), fontproperties=font_prop)
axs[1].set_ylabel(reshape_text('الكمية المطلوبة'), fontproperties=font_prop)
axs[1].grid(True)
axs[1].annotate(reshape_text('YED = +1.18\n(سلعة كمالية)'), 
                xy=(income_new, quantity_new_yed), 
                xytext=(3200, 170), 
                arrowprops=dict(facecolor='black', shrink=0.05), 
                fontproperties=font_prop)

# ---------------------------
# 3. رسم المرونة المتقاطعة (XED)
# ---------------------------
axs[2].plot([competitor_price_old, competitor_price_new], [quantity_old_xed, quantity_new_xed], marker='o', color='blue', linestyle='--')
axs[2].set_title(reshape_text('المرونة المتقاطعة للطلب (XED)'), fontproperties=font_prop)
axs[2].set_xlabel(reshape_text('سعر المنافس (دولار)'), fontproperties=font_prop)
axs[2].set_ylabel(reshape_text('الكمية المطلوبة'), fontproperties=font_prop)
axs[2].grid(True)
axs[2].annotate(reshape_text('XED = +1.5\n(سلع بديلة)'), 
                xy=(competitor_price_new, quantity_new_xed), 
                xytext=(48, 140), 
                arrowprops=dict(facecolor='black', shrink=0.05), 
                fontproperties=font_prop)

plt.tight_layout()
plt.savefig('Demand_Elasticity_Analysis.png', dpi=300)
plt.show()
