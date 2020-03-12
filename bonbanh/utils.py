import re

def get_date(_, text):
    date_pattern = re.compile(r"\d{1,2}\/\d{1,2}\/\d{4}")
    content = text[0]
    return date_pattern.search(content).group()

def get_price_vnd(_, text):
    price_vnd_pattern = re.compile(r"\d+")
    price_vnd_unformated = text[0].split("-")[-1]
    return "".join(price_vnd_pattern.findall(price_vnd_unformated))

def get_price_dol(_, text):
    return text[0][3:-2]

def image_url_formater(image_url):
    large_image_url_pattern = re.compile('s(?=\_\d*)')
    return large_image_url_pattern.sub('l', image_url)
