import re

vzorec_bloka = re.compile(
    r'<tr itemscope itemtype="http://schema.org/Book">'
    r'.*?'
    r'<div class='wtrUp wtrLeft'>',
    flags=re.DOTALL
)

vzorec_knjige = re.compile(
    r'class="number">(?P<uvrstitev>\d+)</td>'
    r'<div id="(?P<id>\d+)".?*</div>'
    r'aria-level=\'4\'(?P<naslov>.?*)</span>'
    r'<a class="authorName".*?itemprop="name">(?P<avtor>.?*)</span></a>'
    r'<span class="minirating">.?*(?P<povp_ocena>avg rating) &mdash; (?P<st_ocen>ratings)</span>'
    r'&#39;score_explanation&#39;, 300.*?>score: (?P<ocena>.?*)</a>.?*return false;">(?P<st_glasov>.?*)people voted</a>',
    flags=re.DOTALL
)

vzorec_zbirke = re.compile(
    r'aria-level=\'4\'>.?*\((?P<zbirka>.?*), #(?P<zap_st_knjige_v_zbirki>.?*)\)</span>',
    flags=re.DOTALL
)

def izberi_podatke_iz_knjig(blok):
    knjiga = vzorec_knjige.search(blok).groupdict()
    knjiga['id'] = int(knjiga['id'])
    knjiga['uvrstitev'] = int(knjiga['uvrstitev'])
    knjiga['st_ocen'] = int(knjiga['st_ocen'])
    knjiga['ocena'] = int(knjiga['ocena'])
    knjiga['st_glasov'] = int(knjiga['st_glasov'])
# shranimo zbirko in zaporedno st. knjige, če je knjiga del nje:
    zbirka, zap_st = vzorec_zbirke.search(blok)
    if zbirka, zap_st:
        film['zbirka'] = zbirka['zbirka']
        film['zap_st'] = oznaka['zap_st_knjige_v_zbirki']
    else:
        film['zbirka'] = None
        film['zap_st'] = None

for page_num in range(91):
    with open(f'best-books-{page_num + 1}.html')

    