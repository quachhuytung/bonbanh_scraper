## Scrape data from bonbanh.com
1. How to install dependencies
* Install PostgreSQL, create a user and a database
* Install Python 3.7.4(any version of python 3.x may be ok)
* Install project dependencies ```pip install -r requirements.txt```
2. Config environment variable

**Create .env file and fill the following information to it**
* database_host
* database_port
* database
* database_username
* database_password
3. Specify how many pages you want to scrape, each page has 20 items by change max_pagination from config.yml
