#!/usr/bin/env python
# coding: utf-8

# # **Find mean and mode of a list of numbers **

# In[31]:


"""
Find mean and mode of a list of numbers 
"""
import statistics

class math_cal:
    def __init__(self,listNumber):
        self.listNumber = listNumber
        
    def mean_list(self,listNumber):
        total = 0
        for i in range(0,len(listNumber)):
            total = total + listNumber[i]
        mean = total/len(listNumber)
        print(f"The mean of this list is {mean} ")
        
    def mode_list(self,listNumber):
        result = statistics.mode(listNumber)
        print(f"The mode of the list is {result}")
        
        
    
object1 = math_cal([1,1,1,5,3,6]) 
object1.mean_list([1,1,1,5,3,6]) 
object1.mode_list([1,1,1,5,3,6])


# In[ ]:




