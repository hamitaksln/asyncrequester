#  Project description

Asyncrequester is a library that makes it easy to make async requests with grequests library.

# Install
```
pip install asyncrequester
```

# Quick start
```python
from asyncrequester import get_async_requests,get_single_request

headers = {
'authority': 'www.google.com',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'en'
}

urls = ["https://www.google.com"]*100 

responses = get_async_requests(urls,20,0.5,headers)
# it will make 20 requests every 0.5 seconds and return all responses
# 'headers' is optional

response = get_single_request(urls[0])
# it makes simple get request

```

### Output
```
Total web page count: 100
0 Waiting
20 Waiting
40 Waiting
60 Waiting
80 Waiting
100 Waiting
Succes: 100 , Fail: 0
It took 7.0120155811309814 seconds to retrieve 100 webpages.
```

### Parameters
- **urls:** url list
- **max_connections:** max connections at once
- **time_delay:** delay for every request
-  **headers:** headers *(Optinal)*