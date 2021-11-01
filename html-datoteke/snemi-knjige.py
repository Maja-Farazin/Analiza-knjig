import requests
import os

def file_name(page_num):
    return f'best-books-{page_num}.html'

#for page_num in range(91):
#    url = (f'https://www.goodreads.com/list/show/7.Best_Books_of_the_21st_Century?page={page_num + 1}')
#    response = requests.get(url)
#    vsebina = response.text
#    with open(file_name(page_num + 1), 'w', encoding='utf-8') as dat:
#        dat.write(vsebina)

for page_num in range(91):
    with open(file_name(page_num + 1), 'r', encoding='utf-8') as dat:
        vsebina = dat.read
        with open('best-books.html', 'w', encoding='utf-8') as f:
            f.write(vsebina)
