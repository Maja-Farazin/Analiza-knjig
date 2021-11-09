import re
import csv

vzorec_bloka = re.compile(
    r'<tr itemscope itemtype="http://schema.org/Book">.*?'
    r'5 of 5 stars</a></div>',
    flags=re.DOTALL
)

vzorec_knjige = re.compile(
    r'class="number">(?P<uvrstitev>\d+)</td>.*?'
    r'<div id="(?P<id>\d+)".+?</div>.*?'
    r'aria-level=\'4\'>(?P<naslov>.*?)( \((?P<zbirka>.+?),? #(?P<zap_st_knjige_v_zbirki>\d+)\))?<\/span>.*?'
    r'<a class="authorName".+?itemprop="name">(?P<avtor>.+?)</span></a>.*?'
    r'</span></span> (?P<povp_ocena>.+?) avg rating &mdash; (?P<st_ocen>.+?) ratings?</span>.*?'
    r'return false;">score: (?P<ocena>.+?)</a>.*?'
    r'return false;">(?P<st_glasov>.+?) (people|person) voted</a><img',
    flags=re.DOTALL
)

def izberi_podatke_iz_knjig(blok):
    knjiga = vzorec_knjige.search(blok).groupdict()
    knjiga['id'] = int(knjiga['id'])
    knjiga['uvrstitev'] = int(knjiga['uvrstitev'])
    knjiga['st_ocen'] = int((knjiga['st_ocen']).replace(',', ''))
    knjiga['ocena'] = int((knjiga['ocena']).replace(',', ''))
    knjiga['st_glasov'] = int((knjiga['st_glasov']).replace(',', ''))
# shranimo zbirko in zaporedno st. knjige, če je knjiga del nje:
    if knjiga['zbirka']:
        knjiga['zbirka'] = knjiga['zbirka']
    else:
        knjiga['zbirka'] = None  
    if knjiga['zap_st_knjige_v_zbirki']:  
        knjiga['zap_st_knjige_v_zbirki'] = knjiga['zap_st_knjige_v_zbirki']
    else:
        knjiga['zap_st_knjige_v_zbirki'] = None
    return knjiga

with open('best-books.html', 'r', encoding='utf-8') as dat:
    vsebina = dat.read()

knjige = []

for blok in vzorec_bloka.finditer(vsebina):
    knjige.append(izberi_podatke_iz_knjig(blok.group()))

with open('knjige.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, 
    ['uvrstitev',
    'id',
    'naslov',
    'avtor',
    'povp_ocena',
    'st_ocen',
    'ocena',
    'st_glasov',
    'zbirka',
    'zap_st_knjige_v_zbirki'])
    writer.writeheader()
    writer.writerows(knjige)