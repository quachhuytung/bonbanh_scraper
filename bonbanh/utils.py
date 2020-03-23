import re

def get_date(_, text):
    date_pattern = re.compile(r"\d{1,2}\/\d{1,2}\/\d{4}")
    content = text[0]
    return date_pattern.search(content).group()

def get_price_vnd(_, text):
    price_vnd_pattern = re.compile(r"\d+")
    price_vnd_unformated = text[0].split("-")[-1]
    raw_data = price_vnd_pattern.findall(price_vnd_unformated)
    if(len(raw_data)==1):
        return raw_data[0]
    else:
        return str(int(raw_data[0])*1000+int(raw_data[1]))

def get_price_dol(_, text):
    return text[0][3:-2]

def image_url_formater(image_url):
    large_image_url_pattern = re.compile('s(?=\_\d*)')
    return large_image_url_pattern.sub('l', image_url)
