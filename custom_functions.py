#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import re
import json
import numpy as np
import sys
sys.setrecursionlimit(10000)



# Write a function that parses HTML pages into BeautifulSoup objects

# In[2]:


def soupify(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


# Film id (we need to download this again to perform a join later on)

# In[3]:


def scrape_id(soup):
    id = int(soup.find("div", class_="really-lazy-load").get("data-film-id"))
    return id


# Film title

# In[4]:


def scrape_title(soup):
    s = soup.find("script", {"type": "application/ld+json"}).string
    s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
    d = json.loads(s)
    
    title = d['name']
    return title


# Year

# In[5]:


def scrape_year(soup):
    try:
        s = soup.find("script", {"type": "application/ld+json"}).string
        s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
        d = json.loads(s)
        year = int(d['releasedEvent'][0]['startDate'])
    except:
        return np.nan
    else:
        return year


# Director

# In[6]:


def scrape_director(soup):
    try:
        s = soup.find("script", {"type": "application/ld+json"}).string
        s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
        d = json.loads(s)
        names = [director['name'] for director in d['director']]
        names = ';'.join(names)
    except:
        return np.nan
    else:
        return names


# Cast

# In[7]:


def scrape_cast(soup):
    try:
        s = soup.find("script", {"type": "application/ld+json"}).string
        s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
        d = json.loads(s)
        actors = [actor['name'] for actor in d['actors']]
        actors = ';'.join(actors)
    except:
        return np.nan
    else:
        return actors


# Country

# In[8]:


def scrape_country(soup):
    try:
        s = soup.find("script", {"type": "application/ld+json"}).string
        s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
        d = json.loads(s)
        countries_of_origin = [country['name'] for country in d['countryOfOrigin']]
        countries_of_origin = ';'.join(countries_of_origin)
    except:
        return np.nan
    else:
        return countries_of_origin
   


# Genres

# In[9]:


def scrape_genre(soup):
    try:
        s = soup.find("script", {"type": "application/ld+json"}).string
        s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
        d = json.loads(s)
        genre_names = ';'.join(d['genre'])
    except:
        return np.nan
    else:
        return genre_names


# Production company

# In[10]:


def scrape_production_company(soup):
    try:
        s = soup.find("script", {"type": "application/ld+json"}).string
        s = s.replace('\n/* <![CDATA[ */\n', '').replace('\n/* ]]> */\n', '')
        d = json.loads(s)
        company_names = [company['name'] for company in d['productionCompany']]
        company_names = ';'.join(company_names)
    except:
        return np.nan
    else:
        return company_names


# Runtime

# In[11]:


def scrape_runtime(soup):
    try:
        string = soup.find("p", class_="text-link text-footer").text
        pattern = r"\d+"
        runtime = int(re.findall(pattern, string)[0])
    except:
        return np.nan
    else:
        return runtime


# Languages

# In[12]:


def scrape_languages(soup):
    try:
        languages = [language.text for language in soup.find_all("a", href = re.compile("language"))]
        languages = ';'.join(languages)
    except:
        return np.nan
    else:
        return languages


# Alternative titles

# In[13]:


def scrape_alt_titles(soup):
    try:
        alt_titles = soup.find("div", class_ = "text-indentedlist").find("p").text
        alt_titles = alt_titles.replace("\n", "").replace("\t", "")
    except:
        return np.nan
    else:
        return alt_titles


# People

# In[14]:


def scrape_people(soup, role):
    try:
        people = [person.text for person in soup.find_all("a", class_="text-slug", href = re.compile(role))]
        people = ';'.join(people)
    except:
        return np.nan
    else:
        return people       

