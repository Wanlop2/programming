#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[2]:


จำนวนเงิน=int(input("จำนวนเงิน :"))
ภาษี=7
จำนวนเงินภาษี=จำนวนเงิน*(ภาษี/100)
print("จำนวนเงินภาษี :",จำนวนเงินภาษี,"บาท")


# # 2.

# In[43]:


x=int(input("x :"))
y=int(input("y :"))
if x > y :
    มากกว่าอายุ=x-y
    print("มากกว่าอายุ :",มากกว่าอายุ,"ปี")
if x < y :
    น้อยกว่าอายุ=y-x
    print("น้อยกว่าอายุ :",น้อยกว่าอายุ,"ปี")
print("อายุเท่ากัน")


# # 3.

# In[31]:


Hello=0
while Hello < 5 :
    Hello += 1
    print("Hello")


# # 4

# In[41]:


number=int(input("number :"))
for i in range(1,12+1):
    print("%d * %d = %d"%(number,i,(number*i)))


# In[ ]:




