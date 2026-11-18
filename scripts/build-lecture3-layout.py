"""Anthropic-inspired Lecture 3 layouts with recorded user text edits."""
import html,json,re
from pathlib import Path
from lxml import etree as ET
from PIL import ImageFont

ROOT=Path(__file__).resolve().parents[1]
native=json.loads((ROOT/'sources/lecture3-native.json').read_text(encoding='utf-8'))
deck_edits=json.loads((ROOT/'sources/deck-edits.json').read_text(encoding='utf-8'))
pages={}

def obj(n,i):return next(o for o in native['slides'][n-1]['objects'] if o['id']==i)
def place(n,i,box,stretch=False,max_scale=None,role='body'):
    item={'box':box,'role':'equation' if obj(n,i)['omml'] else role}
    if stretch:item['stretch']=True
    if max_scale:item['maxScale']=max_scale
    pages.setdefault(n,{})[i]=item
    return item
def panel(n,i,box):
    item=place(n,i,box,True,role='panel')
    item['svg']=f'<g xmlns="http://www.w3.org/2000/svg"><rect x="0" y="0" width="{box[2]}" height="{box[3]}" rx="3" fill="#f0eee6" stroke="#dedbd2" stroke-width="1"/></g>'
    return item
def label(n,i,box,max_scale=None):return place(n,i,box,max_scale=max_scale,role='label')
def text(n,i,box,size,lines=None,family=None,weight=None,role='body',fill='#141413'):
    source=obj(n,i)
    paragraphs=list(source['paragraphs'])
    edit=deck_edits.get('presentationTextEdits',{}).get('Presentation2',{}).get(str(n),{}).get(str(i),{})
    for removed in edit.get('removeLines',[]):
        assert removed in paragraphs,(n,i,'requested removed line missing from source',removed)
        paragraphs.remove(removed)
    if 'replace' in edit:
        assert paragraphs,(n,i,'requested title source is empty')
        paragraphs=edit['replace']
    first=next(t for t in ET.fromstring(source['svg'].encode()).iter() if t.tag.endswith('text') and ''.join(t.itertext()).strip())
    attrs={k:v for k,v in first.attrib.items() if k in ['font-family','font-weight','font-style','fill']}
    if family:attrs['font-family']=family
    if weight is not None:attrs['font-weight']=str(weight)
    attrs['fill']=fill
    attrs['font-size']=str(size)
    weight=int(attrs.get('font-weight','400'))
    face='SourceSerif4.ttf' if family=='Source Serif 4' else 'Inter.ttf'
    font=ImageFont.truetype(str(ROOT/'public/sources/fonts'/face),size)
    # Use the same weight and optical size as the browser's variable font.
    try:font.set_variation_by_axes([min(axis['maximum'],max(axis['minimum'],weight if b'Weight' in axis['name'] else size)) for axis in font.get_variation_axes()])
    except Exception:pass
    if lines is None:
        lines=[]
        for paragraph in paragraphs:
            if not paragraph.strip():continue
            line=''
            for word in paragraph.split():
                candidate=(line+' '+word).strip()
                if line and font.getlength(candidate)>box[2]-8:lines.append(line);line=word
                else:line=candidate
            lines.append(line)
    intended=re.sub(r'\s+','', ''.join(paragraphs))
    assert re.sub(r'\s+','', ''.join(lines))==intended,(n,i,'wording changed')
    attr=' '.join(f'{k}="{html.escape(v,quote=True)}"' for k,v in attrs.items())
    svg='<g xmlns="http://www.w3.org/2000/svg">'+''.join(f'<text {attr} x="0" y="{size+j*size*1.32:g}">{html.escape(line)}</text>' for j,line in enumerate(lines))+'</g>'
    item=place(n,i,box,max_scale=1,role=role);item['svg']=svg

def title(n,i):text(n,i,[56,48,1168,65],50,family='Source Serif 4',weight=400,role='heading')

# Cover: the same title has two large lines instead of one small line.
panel(1,-100013,[56,582,1168,1])
text(1,10,[56,132,1168,30],20,weight=500,role='kicker',fill='#a65a40')
text(1,11,[56,246,1168,245],100,['Matrix Multiplication','& Inverses'],family='Source Serif 4',weight=400,role='heading')
text(1,13,[56,636,1168,28],20,weight=400,role='attribution',fill='#6b6a62')

# Roadmap rows use the height of the slide and readable, continuous text.
title(2,19)
for shape,content,y in [(20,21,170),(22,25,339),(24,26,508)]:
    panel(2,shape,[56,y,1168,145]);text(2,content,[88,y+48,1104,76],34)

title(3,2);place(3,3,[56,132,1168,38],max_scale=1.35)
for shape,content,x,y in [(4,5,56,204),(7,8,652,204),(10,11,56,438),(13,14,652,438)]:
    panel(3,shape,[x,y,572,210]);place(3,content,[x+32,y+76,508,66],max_scale=1.7)

title(4,6)
panel(4,21,[56,162,670,238]);text(4,22,[84,190,614,186],32)
panel(4,9,[758,162,466,238]);text(4,19,[790,197,402,166],30)
panel(4,20,[56,430,1168,228]);label(4,17,[88,455,1076,36],max_scale=1.45)
text(4,18,[88,506,1076,148],31)

title(5,2)
panel(5,3,[56,162,1168,225]);text(5,5,[88,190,1104,169],34)
panel(5,12,[56,417,1168,240]);label(5,14,[88,440,1104,35],max_scale=1.45)
# The original overlapping example objects are kept together in their original order.
place(5,10,[88,487,1104,154],max_scale=1.38);place(5,24,[104,503,1104,138],max_scale=1.24)

title(6,4)
panel(6,6,[56,162,1168,225]);text(6,7,[88,190,1104,169],35)
panel(6,18,[56,417,1168,240]);label(6,11,[88,443,1104,36],max_scale=1.5)
text(6,13,[88,501,1104,136],34)

title(7,2)
panel(7,3,[56,164,455,504]);text(7,4,[84,192,399,180],30)
place(7,14,[84,430,399,185],max_scale=2)
panel(7,6,[543,164,681,504]);label(7,7,[575,192,617,42],max_scale=1.5)
place(7,8,[575,275,617,58],max_scale=1.6)
place(7,18,[575,365,617,70],max_scale=1.4)
place(7,20,[575,482,617,130],max_scale=1.6)

title(8,9)
for shape,heading,detail,x in [(11,12,13,56),(15,16,17,453),(19,21,22,850)]:
    panel(8,shape,[x,186,374,440]);label(8,heading,[x+28,218,318,56],max_scale=1.6)
    text(8,detail,[x+28,344,318,210],34)

title(9,9)
for shape,x in [(5,56),(18,453),(29,850)]:panel(9,shape,[x,164,374,504])
for i,x in [(6,88),(20,485),(30,882)]:place(9,i,[x,192,310,45],max_scale=1.25,role='label')
for i,box in {
 7:[88,253,310,42],8:[88,312,310,100],10:[88,433,310,42],14:[88,505,310,120],
 23:[485,259,310,37],24:[485,309,310,72],25:[485,397,310,37],26:[485,445,310,72],27:[485,533,310,37],28:[485,580,310,70],
 31:[882,253,310,100],32:[882,376,310,42],33:[882,444,310,130],34:[882,602,310,43]
}.items():place(9,i,box,max_scale=1.2)

title(10,12);place(10,17,[550,334,180,40],max_scale=1.2,role='arrow');place(10,19,[526,402,228,62],max_scale=1.3,role='label')
title(11,12)
arrow=place(11,4,[859,390,26,30],role='arrow')
arrow['svg']='<g xmlns="http://www.w3.org/2000/svg" transform="rotate(-90 428.64 365.626)">'+obj(11,4)['svg']+'</g>'

title(12,2)
for shape,heading,content,y in [(6,7,16,164),(9,10,11,333),(13,14,15,502)]:
    panel(12,shape,[56,y,1168,150]);place(12,heading,[88,y+25,250,48],max_scale=1.6,role='label')
    text(12,content,[362,y+25,830,110],31)

out=ROOT/'sources/lecture3-layout.json'
out.write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Wrote Anthropic-inspired layouts for {len(pages)} Lecture 3 slides with recorded text edits.')
