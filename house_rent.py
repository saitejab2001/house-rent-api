#!/usr/bin/env python
# coding: utf-8

# In[5]:import required libraries

print('Importing Dependencies.....')

import pickle


# In[2]:read the data

print('Reading the data......')



# In[3]:split the dataset into dependent and independent variables x=? and y= ?





# In[6]:build the model

print('Building Model...........')



# In[7]:fit the model




# In[8]:save the model as pickel file


print('saving model as pkl file.......')
pickle.dump(regressor, open('model.pkl','wb'))


# In[9]:


model = pickle.load(open('model.pkl','rb'))


# In[10]:


# print(model.predict([[1, 1, 2]]))
