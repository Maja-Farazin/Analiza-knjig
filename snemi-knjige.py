import requests

for page_num in range(91):
    url = (f'https://www.goodreads.com/list/show/7.Best_Books_of_the_21st_Century?page={page_num + 1}')
    response = requests.get(url)
    vsebina = response.text
    with open('best-books.html', 'a', encoding='utf-8') as dat:
        dat.write(vsebina)