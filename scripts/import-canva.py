"""Save the Canva connector's page previews locally, without expired URLs in Git.

python scripts/import-canva.py .cache/source-import/canva-pages.json
The JSON input comes from Canva get_design_pages, not a public-page scraper.
"""
import concurrent.futures
import io
import json
from pathlib import Path
import sys
import urllib.parse
import urllib.request

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def main(input_path):
    source = json.loads(Path(input_path).read_text(encoding='utf-8-sig'))
    output = ROOT / 'public/sources/slides/CanvaLecture9'
    output.mkdir(parents=True, exist_ok=True)

    def download(page):
        number = page['page_number']
        target = output / f'{number:02}.png'
        if target.exists():
            with Image.open(target) as existing:
                if existing.width >= 1920:
                    return {'number': number, 'image': f'/sources/slides/CanvaLecture9/{number:02}.png',
                            'width': existing.width, 'height': existing.height, 'page_id': page['id'],
                            'capture': 'native Canva viewer (retained)'}
        url = page['thumbnail']['url']
        full = url.replace('/height:335/', '/height:1080/').replace('/width:596?', '/width:1920?')
        fallback = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get('fallback', [])
        errors = []
        for candidate in [full, url, *fallback]:
            try:
                request = urllib.request.Request(candidate, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(request, timeout=40) as response:
                    data = response.read()
                with Image.open(io.BytesIO(data)) as image:
                    image.convert('RGB').save(target)
                    width, height = image.size
                return {'number': number, 'image': f'/sources/slides/CanvaLecture9/{number:02}.png',
                        'width': width, 'height': height, 'page_id': page['id']}
            except Exception as error:
                errors.append(str(error))
        raise RuntimeError(f'Canva page {number}: {errors}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        pages = sorted(executor.map(download, source['pages']), key=lambda p: p['number'])
    manifest = {'id': source['design_id'], 'url': source['url'], 'pages': pages,
                'effects': 'Page progression retained. Original animation playback remains available in the native Canva viewer.'}
    (ROOT / 'sources/canva.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f"Saved {len(pages)} original Canva pages: " + str(sorted({(p['width'], p['height']) for p in pages})))


if __name__ == '__main__':
    main(sys.argv[1])
