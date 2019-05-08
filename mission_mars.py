
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# # 1. # Latest Mars News 

# In[2]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[3]:


# Retrieve page with the requests module
response = requests.get(url)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[6]:


news_title = soup.find_all('div', class_="content_title")
news_text= soup.find_all('div' , class_="rollover_description_inner")


# In[7]:


news_title


# In[8]:


title_list=[]
for title in news_title:
    title_text=title.find('a').text[1:-1]
    title_list.append(title_text)


# # 1. # latest mars news ## result #

# In[9]:


#NASA Mars News, title and text
title_list


# In[10]:


p_list=[]
for texts in news_text:
    texts=texts.text[1:-1]
    p_list.append(texts)


# In[11]:


p_list


# In[12]:


d_news={'title':title_list, 'text':p_list}


# In[13]:


df_news=pd.DataFrame(d_news)


# In[14]:


# Nasa mars news title and txt dataframe
df_news


# # 2. # Featured Mars Image 

# In[15]:


# JPL Mars space images
URL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[16]:


Response = requests.get(URL)


# In[17]:


Soup = BeautifulSoup(Response.text, 'html.parser')


# In[18]:


print(Soup.prettify())


# In[19]:


jpl_images=Soup.find_all('a', class_='fancybox')


# In[20]:


print(jpl_images)


# In[21]:


jpl_images[0]


# In[22]:


jpl_images[0].get('data-fancybox-href')
    


# In[23]:


featured_img_url=[]
for img in jpl_images:
    
    img_url="https://www.jpl.nasa.gov"+img.get('data-fancybox-href')
    featured_img_url.append(img_url)


# In[24]:


featured_img_url


# # 2. # feathered mars image ## result#

# In[25]:


# Mars space images
img_url=featured_img_url[0]


# # 3. # Current Mars Weather

# In[26]:


# Tweeter mars weather text

url='https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())


# In[27]:


weather = soup.find_all('p',class_='TweetTextSize')


# In[28]:


weather


# In[29]:


#weather[1].text[:-29]


# In[30]:


# Mars weather from tweeter
mars_weather=[]
for text in weather:
    weather_text=text.text[:-29]
    mars_weather.append(weather_text)


# In[31]:


mars_weather


# # 3. # mars weather ## result #

# In[32]:


mars_weather[0]


# # 4. # Mars Facts #

# In[33]:


# Mars facts
URL='https://space-facts.com/mars/'
response = requests.get(URL)
soup= BeautifulSoup(response.content, 'lxml')


# In[34]:


table=soup.find_all('table')[0]


# In[35]:


table


# In[36]:


df_table=pd.read_html(str(table))


# In[37]:


df_table


# In[38]:


df_table[0]


# In[39]:


json_file=df_table[0].to_json(orient='records')
json_file


# In[40]:


# Mars facts pandas table
df_marsfact=pd.read_json(json_file)
df_marsfact


# In[41]:


# Mars facts html table
html_file=df_marsfact.to_html
html_file


# In[42]:


df1=df_table[0]


# In[43]:


df1_transposed = df1.T


# In[44]:


df1_transposed


# In[45]:


df2=df1_transposed


# In[46]:


df2.columns = df2.iloc[0]


# In[47]:


df3=df2.iloc[1:]
df3


# In[48]:


df3=df3.reset_index(drop=True)


# # 4. # mars fact result ##

# In[49]:


dict_3=(df3.to_dict('records'))[0]
dict_3


# In[50]:


type(dict_3)


# # 5. # Mars Hemisphere#

# In[51]:


# Mars hemispheres 
url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
images = soup.find_all('a',class_='itemLink product-item')


# In[52]:


images


# In[53]:


images[0]


# In[54]:


images[0].find('img').get('src')


# In[55]:


images[0].get('href')


# In[56]:


images[0].find('img').get('alt')


# In[57]:


images[1].find('h3')


# In[58]:


#images[0].find(class_='thumb').get('alt')


# In[59]:


# Mars Hemispheres 
dic_hei=dict()
for image in images:
    try:
        url='https://astrogeology.usgs.gov'+image.find('img').get('src')
        title=image.find('img').get('alt')
    except:
        url=None 
        title=image.h3.string
        
    if url!=None:
        dic_hei[title]=url


# # 5 ## mars hemisphere result #

# In[60]:


dic_hei


# In[61]:


def scrape():
    title=title_list[0]
    news=p_list[0]
    f_img_url=featured_img_url[0]
    mars_w=mars_weather[0]
   
    dic_mars={'title':title,
              'news':news,
             'feature_img_url': f_img_url,
                'current_weather':mars_w,
                'mars_fact':dict_3,
                'mars_hei': dic_hei}
   
    return( dic_mars)


# In[62]:


scrape()


# In[63]:


browser.quit()

