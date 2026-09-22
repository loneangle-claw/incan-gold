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
          .replace('__ILLUSION_MASK__', uri('illusion-mask.png'))
          .replace('__LOBBYBG__', uri('lobby.jpg', 'image/jpeg')))
for n in range(1, 13):  # 12 張洞窟切片：JS 陣列裡的裸 base64 字串
    f = root / 'textures' / f'cave{n:02d}.jpg'
    if f.exists(): out = out.replace(f'__CAVE{n:02d}__', "'" + base64.b64encode(f.read_bytes()).decode() + "'")
import datetime, subprocess
try: rev = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], cwd=root, capture_output=True, text=True).stdout.strip() or '0'
except Exception: rev = '0'
out = out.replace('__BUILD__', f"{datetime.date.today().isoformat()} · build {int(rev) + 1}")
assert '__' + 'GLITTER__' not in out
(root / 'index.html').write_text(out, encoding='utf-8')

drop = {'<!DOCTYPE html>', '<html lang="zh-Hant">', '<head>', '</head>', '<body>', '</body>', '</html>', '</body></html>'}
art = '\n'.join(l for l in out.split('\n') if l.strip() not in drop and not l.startswith('<meta '))
(root / 'artifact.html').write_text(art, encoding='utf-8')
print(f'index.html {len(out):,} bytes / artifact.html {len(art):,} bytes')
