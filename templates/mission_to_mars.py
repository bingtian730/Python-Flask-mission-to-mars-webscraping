
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


#news_title[0]


# In[9]:


#news_title[0].find('a').text[1:-1]


# In[10]:


#news_text[0]


# In[11]:


#news_text[0].text[1:-1]


# In[12]:


title_list=[]
for title in news_title:
    title_text=title.find('a').text[1:-1]
    title_list.append(title_text)


# In[13]:


#NASA Mars News, title and text
title_list


# In[14]:


p_list=[]
for texts in news_text:
    texts=texts.text[1:-1]
    p_list.append(texts)


# In[15]:


p_list


# In[16]:


d_news={'title':title_list, 'text':p_list}


# In[17]:


df_news=pd.DataFrame(d_news)


# In[18]:


# Nasa mars news title and txt dataframe
df_news


# In[19]:


# JPL Mars space images
URL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[20]:


Response = requests.get(URL)


# In[21]:


Soup = BeautifulSoup(Response.text, 'html.parser')


# In[22]:


print(Soup.prettify())


# In[23]:


jpl_images=Soup.find_all('a', class_='fancybox')


# In[24]:


print(jpl_images)


# In[25]:


jpl_images[0]


# In[26]:


jpl_images[0].get('data-fancybox-href')
    


# In[93]:


featured_img_url=[]
for img in jpl_images:
    
    img_url="https://www.jpl.nasa.gov"+img.get('data-fancybox-href')
    featured_img_url.append(img_url)


# In[94]:


featured_img_url


# In[29]:


# HTML object


# In[30]:


# Mars space images
img_url


# In[31]:


# Tweeter mars weather text

url='https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())


# In[32]:


weather = soup.find_all('p',class_='TweetTextSize')


# In[33]:


weather


# In[34]:


#weather[0]


# In[35]:


#weather[0].text


# In[36]:


#weather[1].text[:-29]


# In[37]:


# Mars weather from tweeter
mars_weather=[]
for text in weather:
    weather_text=text.text[:-29]
    mars_weather.append(weather_text)


# In[38]:


mars_weather


# In[39]:


mars_weather[0]


# In[40]:


# Mars facts
URL='https://space-facts.com/mars/'
response = requests.get(URL)
soup= BeautifulSoup(response.content, 'lxml')


# In[41]:


table=soup.find_all('table')[0]


# In[42]:


table


# In[43]:


df_table=pd.read_html(str(table))


# In[44]:


df_table


# In[45]:


df_table[0]


# In[47]:


json_file=df_table[0].to_json(orient='records')
json_file


# In[48]:


# Mars facts pandas table
df_marsfact=pd.read_json(json_file)
df_marsfact


# In[49]:


# Mars facts html table
html_file=df_marsfact.to_html
html_file


# In[50]:


# Mars hemispheres 
url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
images = soup.find_all('a',class_='itemLink product-item')


# In[51]:


images


# In[52]:


#images[0]


# In[53]:


#images[0].get('href')


# In[54]:


#images[0].find(class_='thumb').get('alt')


# In[55]:


# Mars Hemispheres 
url_list=[]
title_list=[]
for image in images:
    url='astrogeology.usgs.gov'+image.get('href')
    print(url)
    url_list.append(url)

    try:
        title=image.find(class_='thumb').get('alt')
    except:
        title=image.find('h3').text
    print(title)
    title_list.append(title)


# In[56]:


url_list


# In[57]:


title_list


# In[58]:


new_list=zip(url_list, title_list)
new_list=list(new_list)


# In[59]:


# Mars Hemispheres images and title
new_list


# In[60]:


df=pd.DataFrame(new_list,columns=['Title','Url'])


# In[61]:


# Mars hemispheres image and title dataframe
df


# In[62]:


url_list


# In[63]:


dic={}
dic_list=[]
for  url, title in zip(url_list, title_list):
    dic['title']=title
    dic['url']=url
    dic_list.append(dic)


# In[64]:


dic


# In[65]:


type(dic)


# In[66]:


# Mars hemispheres dictionary
dic_list


# In[92]:


featured_img_url[0]


# In[84]:


def scrape():
    title=title_list[0]
    news=p_list[0]
    f_img_url=featured_img_url[0]
    mars_w=mars_weather[0]
    mars_fact=df_table[0]
    mars_hemi=dic_list
    dic_mars={'title':title,
                'news':news,
                'feature_img_url': f_img_url}
                #'current_weather':mars_w,
                #'mars_fact': mars_fact,
                #'mars_hei': dic_list}
   
    return(dic_mars)


# In[68]:





# In[86]:





# In[87]:





# In[90]:





# In[91]:




