# Building and visualizing a database of 30 000 films


## Steps

1. <b> Asynchronously scrape </b> data on 30 000 films from the website Letterboxd with Python
2. Do some <b> data cleaning </b> with the Pandas library
3. Store the data on a local <b> PostgreSQL database </b> from Python
4. <b> Query the database </b> with SQL
5. <b> Visualize </b> the output of the queries with R
6. Build a Tableau <b> dashboard </b> 

## Libraries

### Python

```python

import aiohttp
import asyncio
import backoff
import concurrent.futures
from bs4 import BeautifulSoup
import requests
import re
import itertools
import time
import json
import numpy as np
import pandas as pd
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import sqlalchemy

```

### R

```r

library(odbc)
library(DBI)
library(tidyverse)
library(plotly)
library(DT)
library(utf8)


```

## Contributor

<a href = "https://www.linkedin.com/in/jacopo-malatesta/"> Jacopo Malatesta </a> 

## Goals

I hope this project may help showcase my skills in scraping, synchronous programming, multi-processing, data cleaning, programming, SQL queries and data visualization.