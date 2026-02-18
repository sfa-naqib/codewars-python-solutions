def domain_name(url):
    url = url.replace('http://','')
    url = url.replace('https://','')
    url = url.replace('www.','')
    split_url = url.split('.')
    return split_url[0]
