import re

vzorec_knjige = re.compile(
    r'class="number">(?P<uvrstitev>\d+)</td>.*?'
    r'<div id="(?P<id>\d+)".+?</div>.*?'
    r'aria-level=\'4\'>(?P<naslov>.+?)</span>.*?'
    r'<a class="authorName".+?itemprop="name">(?P<avtor>.+?)</span></a>.*?'
    r'</span></span> (?P<povp_ocena>.+?) avg rating &mdash; (?P<st_ocen>.+?) ratings?</span>.*?'
    r'return false;">score: (?P<ocena>.+?)</a>.*?'
    r'return false;">(?P<st_glasov>.+?) (people|person) voted</a><img',
    flags=re.DOTALL
)

with open('best-books.html', 'r', encoding='utf-8') as f:
  vsebina = f.read()

for i, knjiga in enumerate(vzorec_knjige.finditer(vsebina), 1):
    print(i, knjiga.groupdict())