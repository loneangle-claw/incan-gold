# -*- coding: utf-8 -*-
"""index.src.html（含 __GLITTER__ 等佔位符）→ index.html（本機可開）＋ artifact.html（去 doctype/head/body 包裝）。
改版一律改 index.src.html 再跑本檔；不要直接編輯 index.html（裡面是 base64 大塊）。"""
import base64, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'index.src.html').read_text(encoding='utf-8')

def uri(name, mime='image/png'):
    return f'data:{mime};base64,' + base64.b64encode((root / 'textures' / name).read_bytes()).decode()

out = (src.replace('__GLITTER__', uri('glitter.png'))
          .replace('__ILLUSION__', uri('illusion.png'))
          .replace('__ILLUSION_MASK__', uri('illusion-mask.png')))
assert '__' + 'GLITTER__' not in out
(root / 'index.html').write_text(out, encoding='utf-8')

drop = {'<!DOCTYPE html>', '<html lang="zh-Hant">', '<head>', '</head>', '<body>', '</body>', '</html>', '</body></html>'}
art = '\n'.join(l for l in out.split('\n') if l.strip() not in drop and not l.startswith('<meta '))
(root / 'artifact.html').write_text(art, encoding='utf-8')
print(f'index.html {len(out):,} bytes / artifact.html {len(art):,} bytes')
