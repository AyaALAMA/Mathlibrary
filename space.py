# استيراد مكتبة الرياضيات لاستخدام قيمة ثابتة باي
import math

# تعريف دالة لحساب محيط الدائرة
def perimeter_circle(radius):
  # محيط الدائرة = 2 * باي * نصف القطر
  return 2 * math.pi * radius

# تعريف دالة لحساب مساحة الدائرة
def area_circle(radius):
  # مساحة الدائرة = باي * نصف القطر ^ 2
  return math.pi * radius ** 2

# تعريف دالة لحساب مساحة المستطيل
def area_rectangle(length, width):
  # مساحة المستطيل = الطول * العرض
  return length * width

# تعريف دالة لحساب مساحة المربع
def area_square(side):
  # مساحة المربع = طول الضلع ^ 2
  return side ** 2

# اختبار الدوال ببعض القيم
print("محيط الدائرة ذات نصف قطر 5 هو", perimeter_circle(5))
print("مساحة الدائرة ذات نصف قطر 5 هي", area_circle(5))
print("مساحة المستطيل ذو الطول 10 والعرض 6 هي", area_rectangle(10, 6))
print("مساحة المربع ذو طول ضلع 4 هي", area_square(4))
