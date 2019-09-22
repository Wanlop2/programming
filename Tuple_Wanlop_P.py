#!/usr/bin/env python
# coding: utf-8

# # 1.กำหนดให้ brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
# 
# 1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของ Benz, Ford และ Volvo
# 1.2 ให้เขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดในทูเพิล
# 1.3 ให้เขียนคำสั่งโปรแกรมตรวจสอบมียี่ห้อรถ Suzuki, Ferrari, Ford อยู่ใน cars หรือไม่

# In[3]:


brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
print("ตำแหน่งของยี่ห้อรถ BMW คือ",brand_cars.index("BMW"))
print("ตำแหน่งของยี่ห้อรถ Toyota คือ",brand_cars.index("Toyota"))
print("ตำแหน่งของยี่ห้อรถ Tesla คือ",brand_cars.index("Tesla"))
print("จำนวนข้อมูลทั้งหมดในทูเพิล คือ",len(brand_cars),"รายการ")
print("มียี่ห้อรถของ Nissan อยู่ภายใน brand_cars หรือไม่ =","Nissan" in brand_cars)
print("มียี่ห้อรถของ Tesla อยู่ภายใน brand_cars หรือไม่ =","Tesla" in brand_cars)
print("มียี่ห้อรถของ Chevrolet อยู่ภายใน brand_cars หรือไม่ =","Chevrole" in brand_cars)


# In[ ]:




