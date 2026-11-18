"""Assemble source slides and labs while applying the saved deck exclusions.

Regenerates lectures/*.md from sources/*.json. Edit source_math.py for code labs.
Keep decisions about original slides in a later lecture-by-lecture review.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TITLES = {1: 'Geometry of linear equations', 2: 'Elimination with matrices',
          3: 'Matrix multiplication and inverses',
          5: 'Permutations, transposes, and vector spaces',
          9: 'Independence, basis, and dimension'}
FILES = {1: '01-geometry', 2: '02-elimination', 3: '03-products-inverses',
         5: '05-permutations-spaces', 9: '09-independence-basis'}


def frontmatter(**fields):
    return '---\n' + '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key,value in fields.items()) + '\n---\n\n'


def build():
    decks = json.loads((ROOT / 'sources/powerpoint.json').read_text(encoding='utf-8-sig'))
    canva = json.loads((ROOT / 'sources/canva.json').read_text(encoding='utf-8'))
    lessons = json.loads((ROOT / 'sources/code-lessons.json').read_text(encoding='utf-8'))
    edits = json.loads((ROOT / 'sources/deck-edits.json').read_text(encoding='utf-8'))
    excluded_slides = edits.get('excludedSourceSlides', {})
    excluded_demos = set(edits.get('excludedDemos', []))
    counts = {}
    index = []
    next_page = 1
    for lecture in TITLES:
        parts = []
        for deck in decks:
            for slide in deck['slides']:
                belongs = (lecture == 1 and deck['id'] == 'Seminar' and slide['number'] <= 18
                           or lecture == 2 and deck['id'] == 'Seminar' and slide['number'] >= 19
                           or lecture == 3 and deck['id'] == 'Presentation2'
                           or lecture == 5 and deck['id'] == 'Lecture5')
                if not belongs:
                    continue
                if slide['number'] in excluded_slides.get(deck['id'], []):
                    continue
                fields = dict(layout='none', original=True, lecture=lecture,
                              title=f"Lecture {lecture} · {deck['id']} · slide {slide['number']}",
                              clicks=slide['clicks'])
                if not parts:
                    fields.update(routeAlias=f'lecture-{lecture}', section=True)
                parts.append(frontmatter(**fields) + f'<OriginalSlide deck="{deck["id"]}" :slide="{slide["number"]}" />\n\n'
                             f'<!-- Original source: {deck["id"]}.pptx, slide {slide["number"]}. Content and source order retained. -->\n')
        if lecture == 9:
            for page in canva['pages']:
                fields = dict(layout='none', original=True, lecture=lecture,
                              title=f'Lecture 9 · Canva · page {page["number"]}')
                if not parts:
                    fields.update(routeAlias='lecture-9', section=True)
                parts.append(frontmatter(**fields) + f'<OriginalSlide deck="CanvaLecture9" :slide="{page["number"]}" />\n\n'
                             '<!-- Original Canva page preserved, including repeated builds and template pages. The source toolbar opens the full-resolution animated original. -->\n')
        original_count = len(parts)
        for item in [x for x in lessons if x['lecture'] == lecture and x['key'] not in excluded_demos]:
            if item['scene']:
                parts.append(frontmatter(lecture=lecture, title=item['title'] + ' · Manim', kind='animation') +
                             f'<div class="eyebrow">Lecture {lecture} · Animation</div>\n\n# {item["title"]}\n\n'
                             f'<div class="film-wide"><MathFilm src="/animations/source/{item["scene"]}.mp4" poster="/animations/source/{item["scene"]}.jpg" caption="{item["stages"][-1]["caption"]}" /></div>\n\n'
                             f'<div class="source-note">{item["source"]}</div>\n\n<!-- New Manim scene. Numeric constants come from python_examples/source_math.py and match this source. -->\n')
            max_lines = max(len(stage['code'].splitlines()) for stage in item['stages'])
            blocks = '\n'.join('```python\n' + stage['code'] + '\n```' for stage in item['stages'])
            parts.append(frontmatter(lecture=lecture, title=item['title'] + ' · Python', kind='code', clicks=len(item['stages'])-1) +
                         f'<div class="eyebrow">Lecture {lecture} · Python</div>\n\n# {item["title"]}\n\n'
                         f'<div class="code-pair"><div class="code-panel" style="--code-lines: {max_lines}">\n\n'
                         '````md magic-move {duration:600}\n' + blocks + '\n````\n\n</div>\n'
                         f'<CodeOutput lesson="{item["key"]}" />\n</div>\n\n'
                         '<div class="step-hint">Space advances the code and output. Left arrow returns one step.</div>\n\n'
                         f'<div class="source-note">{item["source"]}</div>\n\n'
                         '<!-- Each code stage was executed independently to generate the displayed output. Run python python_examples/source_math.py to regenerate. -->\n')
        output = ROOT / 'lectures' / (FILES[lecture] + '.md')
        output.write_text('\n'.join(parts), encoding='utf-8')
        counts[lecture] = {'originals': original_count, 'new_labs': len(parts)-original_count, 'total': len(parts)}
        index.append({'lecture': lecture, 'title': TITLES[lecture], 'start': next_page, 'file': 'lectures/' + output.name, **counts[lecture]})
        next_page += len(parts)
    (ROOT / 'sources/lecture-index.json').write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(counts))


if __name__ == '__main__':
    build()
