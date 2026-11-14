"""Check generated static pages, local resources and cross-page anchors."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.file, self.ids, self.refs, self.images = file, [], [], 0
        self.feed(file.read_text())

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.refs.append(attrs[attr])
        if tag == 'option' and '.html' in attrs.get('value', ''):
            self.refs.append(attrs['value'])
        if tag == 'img':
            self.images += 1
            assert attrs.get('alt'), f'Missing image description: {self.file}'


pages = {p.resolve(): Page(p) for p in [ROOT / 'index.html', ROOT / 'characters.html', *ROOT.glob('books/*/*.html')]}
errors, checked = [], 0
for file, page in pages.items():
    for id_, count in Counter(page.ids).items():
        if count > 1:
            errors.append(f'{file.relative_to(ROOT)}: duplicate ID {id_}')
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        target = (file.parent / unquote(url.path)).resolve() if url.path else file
        if target.is_dir():
            target /= 'index.html'
        checked += 1
        if not target.exists():
            errors.append(f'{file.relative_to(ROOT)}: missing {ref}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            # Root characters.html is a compatibility redirect preserving the fragment.
            if target == ROOT / 'characters.html':
                target = ROOT / 'books/three-body/characters.html'
            if unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{file.relative_to(ROOT)}: missing anchor {ref}')

catalog = json.loads((ROOT / 'assets/catalog.json').read_text())
for book in catalog:
    directory = ROOT / 'books' / book['id']
    expected = {'index.html', 'characters.html'}
    actual = {p.name for p in directory.glob('*.html')}
    if actual != expected:
        errors.append(f'{book["id"]}: expected two pages, got {actual}')
    images = pages[(directory / 'index.html').resolve()].images
    if images < 5:
        errors.append(f'{book["id"]}: expected at least 5 timeline illustrations, got {images}')
for legacy in ('full.html', 'lite.html'):
    if (ROOT / legacy).exists():
        errors.append(f'Unwanted old edition: {legacy}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Checked {len(pages)} HTML pages, {checked} local links/resources; each of {len(catalog)} books has exactly two pages.')
