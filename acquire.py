#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import dependencies
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import json


# In[11]:


print('codeup: ' 'get_blog_articles(article_list)')
print('inshort: ' 'scrape_one_page(topic)')
print('inshort: ' 'get_news_articles()' 'includes:' 'business', 'sports', 'technology', 'entertainment')


# In[ ]:


links = ['https://codeup.com/data-science/recession-proof-career/',
         'https://codeup.com/codeup-news/codeup-x-comic-con/',
         'https://codeup.com/featured/series-part-3-web-development/'
         'https://codeup.com/featured/what-jobs-can-you-get-after-a-coding-bootcamp-part-2-cloud-administration/',
         'https://codeup.com/data-science/jobs-after-a-coding-bootcamp-part-1-data-science/']


# In[2]:


#Mimicked from class review
def get_blog_articles():
    
    file = 'blog_posts.json'
    
    if os.path.exists(file):
        
        with open(file) as f:
        
            return json.load(f)
    
    headers = {'User-Agent': 'Codeup Data Science'}
    
    article_info = []
    
    for link in links:
        
        info_dict = {}
        
        response = get(link, headers=headers)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        info_dict['title'] = soup.find('h1', class_ = 'entry-title').text
    
        info_dict['date_published'] = soup.find('span', class_='published').text
    
        info_dict['content'] = soup.find('div', class_='entry-content').text
    
        article_info.append(info_dict)
        
    with open(file, 'w') as f:
        
        json.dump(article_info, f)
        
    return article_info    


# In[ ]:





# In[3]:


#Mimicked after class review
def scrape_one_page(topic):
    
    base_url = 'https://inshorts.com/en/read/'
    
    response = get(base_url + topic)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find_all('span', itemprop='headline')
    
    body = soup.find_all('div', itemprop='articleBody')
    
    body_list = []
    
    for i in range(len(title)):
        
        temp_dict = {}
        
        temp_dict['title'] = title[i].text
        
        temp_dict['content'] = body[i].text
        
        temp_dict['category'] = topic
        
        body_list.append(temp_dict)
        
    return body_list    


# In[4]:


#Define a function that will scrape information about an array of topics
def get_news_articles():
    
    file = 'news_articles.json'
    
    if os.path.exists(file):
        
        with open(file) as f:
            
            return json.load(f)
    
    topic_list = ['business', 'sports', 'technology', 'entertainment']
    
    final_list = []
    
    for topic in topic_list:
        
        final_list.extend(scrape_one_page(topic))
        
    with open(file, 'w') as f:
        
        json.dump(final_list, f)
        
    return final_list  


# In[ ]:




