#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')
import pandas as pd
import numpy as np
import yfinance as yf


# In[4]:


#Random assets : Disney, Microsoft, Amazon, Exxon, Apple, Gold ETF, Eni, Ford, Procter& Gamble, Pfizer
import pandas as pd
import yfinance as yf

tickers = ['DIS', 'MSFT', 'AMZN', 'XOM', 'AAPL', 'GLD', 'E', 'F', 'PG', 'PFE']

data = pd.DataFrame()

for t in tickers:
    try:
        data[t] = yf.download(t, start='2005-01-01', end='2023-01-01')['Adj Close']
    except:
        print(f"No data found for ticker: {t}")

#check with --> data.info()

#check with --> data.info()


# In[5]:


#stock returns 
log_ret = np.log( 1 + data.pct_change()) #check with --> log_ret.tail()
#annual stock returns
annual_log_ret = log_ret.mean()*252


# In[6]:


#randomly weighted portfolio
num_asset = len(tickers)
weights_1 = np.random.random(num_asset)
weights_1 /= np.sum(weights_1)
#check with --> sum(weights_1)


# In[8]:


#equally weighted portfolio
from numpy import zeros_like

weights_2 = zeros_like(weights_1)
weights_2[:] = 0.1 / num_asset


# In[9]:


#stock returns
log_ret = np.log( 1 + data.pct_change()) #check with --> log_ret.tail()
#annual stock returns
annual_log_ret = log_ret.mean()*252


# In[10]:


#randomly weighted portfolio
num_asset = len(tickers)
weights_1 = np.random.random(num_asset)
weights_1 /= np.sum(weights_1)
#check with --> sum(weights_1)


# In[11]:


#Vector product of annual_returns and (random) weights with np.dot
pfolio_1 = round(np.dot(annual_log_ret, weights_1),4)*100
print(pfolio_1, '%')


# In[17]:


#equally weighted portfolio


num_assets = 10
equal_weights = np.zeros_like(np.arange(num_assets), dtype=float)

for t in range(num_assets):
    equal_weights[t] = 0.1


# In[18]:


#Vector product of annual_returns and (equal) weights with np.dot
pfolio_2 = round(np.dot(annual_log_ret, weights_2),5)*100
print(pfolio_2, '%')


# In[ ]:




