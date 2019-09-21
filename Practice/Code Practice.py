#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[114]:


import os
os.getcwd()
os.chdir('C:/Users/LADOT/Desktop')


# In[108]:


one = 301
five = 305

a = [301]
for x in range(60):
    one -= 5
    a.append(one)

b = [305]
for y in range(60):
    five -= 5
    b.append(five)


# In[109]:


c = a
d = b


# In[110]:


list = []
for length in range(len(a)):
    e = str(c.pop()) + '-' + str(d.pop())
    list.append(e)
print(list)


# In[121]:


array1 = np.asarray(list)


# In[120]:


array1


# In[129]:


df1 = pd.DataFrame({
    'numbers':['1-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35',
       '36-40', '41-45', '46-50', '51-55', '56-60', '61-65', '66-70',
       '71-75', '76-80', '81-85', '86-90', '91-95', '96-100', '101-105',
       '106-110', '111-115', '116-120', '121-125', '126-130', '131-135',
       '136-140', '141-145', '146-150', '151-155', '156-160', '161-165',
       '166-170', '171-175', '176-180', '181-185', '186-190', '191-195',
       '196-200', '201-205', '206-210', '211-215', '216-220', '221-225',
       '226-230', '231-235', '236-240', '241-245', '246-250', '251-255',
       '256-260', '261-265', '266-270', '271-275', '276-280', '281-285',
       '286-290', '291-295', '296-300', '301-305'],
    'key':'key'
})


# In[140]:


df1.head(100)


# In[136]:


numbers = df1['numbers']


# In[137]:


key = df1['key']


# In[139]:





# In[142]:


export_csv = df1.to_csv(r'C:\Users\LADOT\Desktop\df1.csv', index= None, header=True)


# In[ ]:




