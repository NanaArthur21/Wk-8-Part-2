#!/usr/bin/env python
# coding: utf-8

# In[1]:


gis = GIS('home')


# In[2]:


from datetime import datetime as dt
from IPython.display import display

from arcgis import GIS
from arcgis.features.analyze_patterns import find_hot_spots
from arcgis.features.enrich_data import enrich_layer
from arcgis.features.manage_data import overlay_layers
from arcgis.features.find_locations import find_existing_locations 


# In[3]:


gis = GIS('home')


# In[4]:


from arcgis import GIS
gis = GIS()


# In[6]:


map1 = gis.map('USA',3)
map1.basemap = 'dark-gray-vector'
map1


# In[7]:


search_result = gis.content.search("title:Homicides - Victim Race and Culprit Disposition", item_type = "Feature Layer")
display(search_result)


# In[8]:


search_result = gis.content.search('title:Homicides', item_type='Feature Layer')
search_result[0]


# In[9]:


search_result = gis.content.search('title:Homicides - Victim Race and Culprit Disposition', item_type='Feature Layer')
search_result[0]


# In[10]:


search_result = gis.content.search('title:Homicides - Victim Race and Culprit Disposition', item_type='Feature Layer')
search_result[0].id


# In[11]:


search_result = gis.content.search('title:Homicides - Victim Race and Culprit Disposition', item_type='Feature Layer')
search_result[0].id
search_layer = gis.content.get(search_result[0].id)
search_layer


# In[12]:


map1.add_layer(search_layer)
map1


# In[13]:


map1.zoom = Fort Worth


# In[14]:


map1.zoom = 'Fort Worth'


# In[15]:


import matplotlib
matplotlib.use('nbagg')
import matplotlib.pyplot as plt


# In[16]:





# In[17]:


labels = ['Ft. Worth', 'San Antonio', 'Houston', 'Oklahoma City', 'Tulsa']
Male = [26, 63, 26, 55, 55]
Female = [58, 25, 48, 25, 42]

x = np.arange(len(labels))  
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Male, width, label='Male')
rects2 = ax.bar(x + width/2, Female, width, label='Female')

ax.set_ylabel('Age')
ax.set_title('Age by City and Gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()


# In[18]:


labels = ['Ft. Worth', 'San Antonio', 'Houston', 'Oklahoma City', 'Tulsa']
Male = [26, 63, 26, 55, 55]
Female = [58, 25, 48, 25, 42]

x = np.arange(len(labels))  
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Male, width, label='Male')
rects2 = ax.bar(x + width/2, Female, width, label='Female')

ax.set_ylabel('Age')
ax.set_title('Age by City and Gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()


# In[19]:


import matplotlib.pyplot as plt
import numpy as np

labels = ['Ft. Worth', 'San Antonio', 'Houston', 'Oklahoma City', 'Tulsa']
Male = [26, 63, 26, 55, 55]
Female = [58, 25, 48, 25, 42]

x = np.arange(len(labels))  
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Male, width, label='Male')
rects2 = ax.bar(x + width/2, Female, width, label='Female')

ax.set_ylabel('Age')
ax.set_title('Age by City and Gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()


# In[20]:


import matplotlib.pyplot as plt
import numpy as np

labels = ['Ft. Worth', 'San Antonio', 'Houston', 'Oklahoma City', 'Tulsa']
Male = [26, 63, 26, 55, 55]
Female = [58, 25, 48, 25, 42]

x = np.arange(len(labels))  
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Male, width, label='Male')
rects2 = ax.bar(x + width/2, Female, width, label='Female')

ax.set_ylabel('Age')
ax.set_title('Age by City and Gender')
ax.set_xticks(x, labels)
ax.legend()

plt.show()


# In[ ]:




