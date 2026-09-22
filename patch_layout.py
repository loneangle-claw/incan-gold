# -*- coding: utf-8 -*-
"""一次性補丁：DQ 戰鬥畫面版面（直式／橫式）、常駐指令窗四項、退出遊戲。跑一次即可。"""
import pathlib, sys
p = pathlib.Path(__file__).parent / 'index.src.html'
s = p.read_text(encoding='utf-8')

def rep(a, b, cnt=1):
    global s
    if a not in s:
        print('MISSING:', a[:100]); sys.exit(1)
    s = s.replace(a, b, cnt)

def cut(a, b, new):
    global s
    i = s.index(a); j = s.index(b, i)
    s = s[:i] + new + s[j:]

# ---------- CSS ----------
rep('#app{position:relative;min-height:100%;padding-block:8px 20px;padding-inline:12px;max-width:980px;margin:0 auto;display:flex;flex-direction:column;gap:8px}',
    '#app{position:relative;padding-block:6px 10px;padding-inline:10px;max-width:980px;margin:0 auto;display:grid;grid-template-rows:auto auto auto auto;gap:6px;min-height:100%}')
rep('.bgm .ib.on{color:var(--green);border-color:var(--green)}', '.bgm .ib.on{color:var(--green);border-color:var(--green)}\n.bgm .ib.quit{color:var(--red);border-color:var(--red)}')
rep('.scene{position:relative;width:100%;aspect-ratio:16/8.6;max-height:470px;border:3px solid var(--line);border-radius:7px;overflow:hidden;background:#05070a;image-rendering:pixelated}',
    '.scene{position:relative;width:100%;aspect-ratio:16/8.6;max-height:52dvh;min-height:150px;border:3px solid var(--line);border-radius:7px;overflow:hidden;background:#05070a;image-rendering:pixelated}')
rep('.sprite{position:absolute;width:48px;height:64px;translate:-50% -100%;z-index:4;transition:filter .3s}\n.sprite canvas{width:48px;height:64px;image-rendering:pixelated;display:block}',
    '.sprite{position:absolute;height:clamp(34px,16dvh,64px);aspect-ratio:3/4;translate:-50% -100%;z-index:4;transition:filter .3s}\n.sprite canvas{width:100%;height:100%;image-rendering:pixelated;display:block}')
rep('.cmd{position:absolute;left:10px;top:10px;z-index:10;min-width:150px}', '.cmdrow{display:grid;grid-template-columns:minmax(96px,auto) 1fr;gap:6px;align-items:stretch}\n.cmd{min-width:96px;padding:6px 10px}\n.cmd .menu button{opacity:.45}\n.cmd.armed .menu button[data-c="go"],.cmd.armed .menu button[data-c="leave"],.cmd .menu button[data-c="log"],.cmd .menu button[data-c="quit"]{opacity:1}\n.cmd .menu button[data-c="quit"]{color:var(--red)}\n.mystat{position:absolute;left:8px;top:8px;z-index:10;font-size:12px;padding:3px 9px;line-height:1.35;min-width:96px}\n.mystat .n{color:var(--pc,var(--p1));border-bottom:1px solid var(--line);margin-bottom:2px;padding-bottom:1px}\n.mystat .r{display:flex;justify-content:space-between;gap:8px}\n.mystat b{font-weight:400;color:var(--yellow)}')
rep('.cmd .who{color:var(--pc,var(--yellow));font-size:13px;margin-bottom:4px;padding-bottom:3px;border-bottom:1px solid var(--line)}', '.cmd .who{color:var(--pc,var(--yellow));font-size:12px;margin-bottom:3px;padding-bottom:2px;border-bottom:1px solid var(--line);white-space:nowrap}')
rep('.cavetag{position:absolute;right:10px;top:10px;z-index:10;font-size:12px;padding:3px 8px}', '.cavetag{position:absolute;right:8px;top:8px;z-index:10;font-size:12px;padding:3px 8px}')
cut('/* ===== 路徑窗 ===== */', '.left-badge{',
    '/* ===== 路徑窗（場景左下） ===== */\n.pathwin{position:absolute;left:8px;bottom:8px;z-index:6;display:flex;gap:8px;align-items:center;padding:4px 8px;background:rgba(0,0,0,.72);max-width:calc(100% - 16px)}\n.pathwin .lbl{font-size:11px;color:var(--dim);white-space:nowrap;line-height:1.2}\n.pathwin .lbl b{display:block;color:var(--yellow);font-weight:400;font-size:14px}\n.path{display:flex;gap:4px;overflow-x:auto;padding:3px 2px;--card-w:30px;--card-h:43px;min-height:50px;scrollbar-width:none}\n.path .frame,.path .corner{display:none}\n.path .art .name{display:none}\n.path-empty{color:var(--dim);font-size:11px;align-self:center}\n')
rep('.left-badge{position:absolute;right:-6px;top:-7px;z-index:3;min-width:18px;height:18px;border-radius:50%;background:var(--gold);color:#000;font-size:11px;display:grid;place-items:center;border:2px solid #000;transition:.3s}',
    '.left-badge{position:absolute;right:-5px;top:-6px;z-index:3;min-width:16px;height:16px;border-radius:50%;background:var(--gold);color:#000;font-size:10px;display:grid;place-items:center;border:2px solid #000;transition:.3s}')
cut('/* ===== 隊員窗 ===== */', '/* ===== 訊息窗 ===== */',
'''/* ===== 隊員窗 ===== */
.party{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px}
.pw{--pc:#fff;padding:5px 8px 6px;font-size:13px;transition:.3s;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto auto;column-gap:8px;row-gap:0;align-items:center}
.pw .face{grid-row:1/4;width:40px;height:30px;image-rendering:pixelated;border:2px solid var(--line);background:#111;border-radius:3px}
.pw .nm{color:var(--pc);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:13px}
.pw .stats{display:flex;flex-wrap:wrap;gap:0 8px;line-height:1.3;font-variant-numeric:tabular-nums}
.pw .stats span{color:var(--dim);white-space:nowrap}
.pw .stats b{font-weight:400;color:var(--text);margin-left:3px}
.pw .stats b.gem{color:var(--gold)}
.pw .st{font-size:11px;color:var(--green)}
.pw[data-status="out"]{color:var(--dim)}
.pw[data-status="out"] .st{color:var(--cyan)}
.pw[data-status="bust"] .st{color:var(--red)}
.pw[data-status="bust"] .nm{color:var(--red)}
.pw[data-status="bust"] .face{filter:grayscale(1) brightness(.6)}
.pw.thinking .st{color:var(--yellow);animation:blink 1s steps(2,start) infinite}
.pw.bounce{animation:winbounce .6s cubic-bezier(.2,1.6,.4,1)}
@keyframes winbounce{35%{transform:translateY(-10px)}}
.pw .lost{animation:blink .2s steps(2) 5;color:var(--red)}

''')
rep('.msgwin{min-height:96px;padding:8px 14px 10px;font-size:15px;line-height:1.5}\n.msgwin .lines{display:flex;flex-direction:column;gap:1px;min-height:68px;justify-content:flex-end}',
    '.msgwin{min-height:84px;padding:6px 12px 8px;font-size:14px;line-height:1.5}\n.msgwin .lines{display:flex;flex-direction:column;gap:1px;min-height:60px;justify-content:flex-end}')
rep('.msgwin .logbtn{position:absolute;right:12px;top:6px;font-size:11px;color:var(--dim);border:1px solid var(--dim);border-radius:3px;padding:0 5px}\n', '')
rep('.logwin{max-height:200px;overflow:auto;font-size:13px;scrollbar-width:thin}', '.logwin{position:fixed;left:50%;bottom:12px;translate:-50% 0;width:min(720px,calc(100% - 24px));max-height:46dvh;overflow:auto;font-size:13px;scrollbar-width:thin;z-index:40;background:rgba(0,0,0,.95)}')
rep('@media (max-width:640px){.hud .title{width:100%}.scene{aspect-ratio:16/10}.sprite{width:36px;height:48px}.sprite canvas{width:36px;height:48px}:root{--card-w:124px;--card-h:177px}.cmd{min-width:120px}.cmd .menu button{font-size:14px}}',
'''/* ===== 直式：場景更高、隊員四列橫條 ===== */
@media (orientation:portrait){
  :root{--card-w:clamp(108px,34vw,172px);--card-h:calc(var(--card-w) * 1.42)}
  .scene{aspect-ratio:4/3.1;max-height:48dvh}
  .party{grid-template-columns:1fr;gap:5px}
  .pw{grid-template-columns:auto auto 1fr;grid-template-rows:auto;column-gap:10px;padding:4px 10px}
  .pw .face{grid-row:auto}
  .pw .nm{min-width:5.5em}
  .pw .stats{justify-content:flex-end;gap:0 12px}
  .pw .st{display:none}
  .pw[data-status="out"] .nm::after{content:" ・回營";color:var(--cyan);font-size:11px}
  .pw[data-status="bust"] .nm::after{content:" ・埋葬";color:var(--red);font-size:11px}
  .pw.thinking .nm::after{content:" ・抉擇中";color:var(--yellow);font-size:11px;animation:blink 1s steps(2,start) infinite}
  .hud .title{display:none}
}
/* ===== 橫式：整頁塞進一屏 ===== */
@media (orientation:landscape){
  :root{--card-w:clamp(80px,27dvh,172px);--card-h:calc(var(--card-w) * 1.42)}
  #app{height:100dvh;grid-template-rows:auto minmax(120px,1fr) auto auto;padding-block:4px 6px}
  .scene{aspect-ratio:auto;height:100%;max-height:none;min-height:0}
  .msgwin{min-height:0}
  .msgwin .lines{min-height:calc(1.5em * 3)}
}
@media (orientation:landscape) and (max-height:520px){
  body{font-size:13px}
  .hud{font-size:11px;padding:2px 8px}.hud .title{display:none}
  .cmd .menu button{font-size:13px;padding:1px 4px}.cmd{padding:3px 8px}
  .msgwin{font-size:12px;padding:3px 10px 4px}.msgwin .lines{min-height:calc(1.5em * 3)}
  .pw{padding:2px 6px 3px;font-size:11px;column-gap:5px}.pw .face{width:30px;height:22px}.pw .st{display:none}.pw .nm{font-size:11px}
  .mystat{font-size:10px;padding:2px 6px;min-width:80px}.cavetag{font-size:10px;padding:2px 6px}
  .pathwin{padding:2px 6px}.path{--card-w:24px;--card-h:34px;min-height:40px}
  .toast{font-size:15px;padding:6px 14px}
}''')

# ---------- HTML ----------
rep('      <button class="ib" id="motion-toggle" title="開啟手機動作感應（陀螺儀）" hidden>📱</button>',
    '      <button class="ib" id="motion-toggle" title="開啟手機動作感應（陀螺儀）" hidden>📱</button>\n      <button class="ib quit" id="btn-quit" title="退出遊戲，直接回到標題">退出</button>')
_i = s.index('<svg class="cave"'); _j = s.index('</svg>', _i) + len('</svg>')
SVG = s[_i:_j]
cut('  <main class="screen" style="display:flex;flex-direction:column;gap:8px">', '</div>\n\n<!-- lobby / title -->',
'''  <section class="scene" id="scene">
      __SVG__
      <div class="vig"></div>
      <div class="altar-hint" id="altar-hint">你站在洞穴入口，祭壇上還沒有牌<br><small>按「出發」開始探險</small></div>
      <div id="sprites"></div>
      <div id="current-card"></div>
      <div class="win tight mystat" id="mystat"><div class="n">探險家P1</div><div class="r"><span>寶石</span><b id="my-round">0</b></div><div class="r"><span>帳篷</span><b id="my-tent">0</b></div></div>
      <div class="win tight cavetag" id="cave-title">CAVE I</div>
      <div class="win tight pathwin"><div class="lbl">路上餘數<b id="path-gems">0</b></div><div class="path" id="path"><span class="path-empty">尚未翻牌</span></div></div>
      <div class="bustfx" id="bust"><div class="flash"></div><div class="big" id="bust-icon">🪨</div></div>
  </section>

  <div class="cmdrow">
    <div class="win cmd" id="decision">
      <div class="who" id="decision-who">指令</div>
      <div class="menu" id="cmd-menu">
        <button id="btn-go" data-c="go">前進</button>
        <button id="btn-leave" data-c="leave">撤退</button>
        <button id="btn-log" data-c="log">紀錄</button>
        <button id="btn-quit2" data-c="quit">退出</button>
      </div>
      <div class="hint" id="cmd-hint"></div>
    </div>
    <div class="win msgwin" id="msgwin"><div class="lines" id="msg-lines"></div><span class="tri blink" id="msg-tri" hidden>▼</span></div>
  </div>

  <div class="party" id="players"></div>
  <div class="win logwin" id="log" hidden><h3>探險紀錄</h3></div>
  <div class="lockmsg" id="lockmsg" hidden></div>
''')
s = s.replace('__SVG__', SVG)
assert s.count('<svg class="cave"') == 1

# ---------- JS ----------
rep("""    host.innerHTML = G.players.map(p => `<div class="win pw" id="pl-${p.id}" style="--pc:${p.color}">
      <div class="nm">${p.emoji} ${p.name}</div>
      <div class="row"><span>寶石</span><b class="gem round-n">0</b></div>
      <div class="row"><span>帳篷</span><b class="tent-n">0</b></div>
      <div class="row"><span>Lv</span><b>${p.type === 'human' ? '－' : p.level + ' ' + LEVELS[p.level].n}</b></div>
      <div class="st"></div></div>`).join('');
  }""",
"""    host.innerHTML = G.players.map(p => `<div class="win pw" id="pl-${p.id}" style="--pc:${p.color}">
      <canvas class="face" width="12" height="9"></canvas>
      <div class="nm">${p.name}</div>
      <div class="stats"><span>寶<b class="gem round-n">0</b></span><span>帳<b class="tent-n">0</b></span><span>Lv<b>${p.type === 'human' ? '－' : p.level}</b></span></div>
      <div class="st"></div></div>`).join('');
    G.players.forEach(p => drawFace($('#pl-' + p.id + ' .face'), p.pal));
  }
  const me = G.players[+($('#decision').dataset.pid ?? 0)] || G.players[0];
  if (me) { $('#mystat').style.setProperty('--pc', me.color); $('#mystat .n').textContent = me.name; $('#my-round').textContent = me.round; $('#my-tent').textContent = me.tent; }""")
rep("function drawSprite(cv, map, pal) {", """function drawFace(cv, pal) {
  const ctx = cv.getContext('2d'); ctx.clearRect(0, 0, 12, 9);
  const C = { H: pal[0], h: pal[1], S: '#f1c27d', e: '#111', C: '#8b5a2b' };
  SPR_A.slice(0, 9).forEach((row, y) => [...row].forEach((ch, x) => { if (C[ch]) { ctx.fillStyle = C[ch]; ctx.fillRect(x, y, 1, 1); } }));
}
function drawSprite(cv, map, pal) {""")

cut("let cmdIndex = 0;", "function onChoice(choice) {",
r'''let cmdIndex = 0;
const CMDS = ['go', 'leave', 'log', 'quit'];
function cmdEnabled(i) { const c = CMDS[i]; return (c === 'go' || c === 'leave') ? $('#decision').classList.contains('armed') : true; }
function showDecision(p) {
  const d = $('#decision'); d.classList.add('armed');
  d.style.setProperty('--pc', p.color); $('#decision-who').textContent = `${p.name} 要怎麼做？`;
  d.dataset.pid = p.id; setCursor(0); renderPlayers();
  log(`${p.name}，前進還是撤退？`);
}
function setCursor(i) {
  cmdIndex = i; $$('#cmd-menu button').forEach((b, k) => b.classList.toggle('on', k === i));
  const d = $('#decision'); const p = G.players[+d.dataset.pid]; const hint = $('#cmd-hint');
  const leave = CMDS[i] === 'leave' && d.classList.contains('armed'); $('#app').classList.toggle('hl-path', leave);
  if (leave && p) { const pt = pathTotal(); hint.innerHTML = `撤退可帶回 <b>${p.round + pt}</b> 顆（本輪 ${p.round}＋路上 ${pt}）`; }
  else if (CMDS[i] === 'quit') hint.textContent = '直接結束這場探險，回到標題';
  else if (CMDS[i] === 'log') hint.textContent = '顯示／隱藏完整探險紀錄';
  else hint.textContent = d.classList.contains('armed') ? '↑↓ 選擇　Enter 決定' : '';
}
function hideDecision() { const d = $('#decision'); d.classList.remove('armed'); $('#decision-who').textContent = '指令'; $('#app').classList.remove('hl-path'); $$('#cmd-menu button').forEach(b => b.classList.remove('on')); $('#cmd-hint').textContent = ''; }
function runCmd(c) {
  if (c === 'log') { const l = $('#log'); l.hidden = !l.hidden; l.scrollTop = l.scrollHeight; AudioEngine.sfx('cursor'); return; }
  if (c === 'quit') return quitGame();
  onChoice(c);
}
function quitGame() {
  G.running = false; G.phase = 'lobby'; hideDecision(); closeModal(); $('#handoff').hidden = true; $('#log').hidden = true;
  $('#bust').className = 'bustfx'; $('#app').classList.remove('shake'); $('#scene').classList.remove('turn');
  $$('.fx').forEach(e => e.remove()); $$('.toast').forEach(e => e.remove());
  $('#current-card').innerHTML = ''; $('#altar-hint').hidden = false;
  G.round = 0; G.deck = []; G.pathCards = []; G.shown = {}; setupPlayers(); delete $('#decision').dataset.pid;
  renderPlayers(); renderTop(); renderPath(); AudioEngine.sfx('lock'); $('#lobby').hidden = false;
}
''')
rep("""  if (G.phase !== 'decide') return; const p = G.players[+$('#decision').dataset.pid]; if (!p || p.choice) return;""",
    """  if (G.phase !== 'decide' || !$('#decision').classList.contains('armed')) return; const p = G.players[+$('#decision').dataset.pid]; if (!p || p.choice) return;""")
# 常駐指令窗：不再 hidden 切換
rep("""  $('#current-card').innerHTML = ''; hideDecision();
  renderPlayers(); renderTop(); renderPath();
  AudioEngine.sfx('round');""", """  $('#current-card').innerHTML = ''; hideDecision();
  renderPlayers(); renderTop(); renderPath();
  if (!G.running) return;
  AudioEngine.sfx('round');""")
rep("function startGame() {\n  setupPlayers(); G.round = 0; G.removed = {}; Msg.clear();", "function startGame() {\n  setupPlayers(); G.round = 0; G.removed = {}; Msg.clear(); G.running = true; delete $('#decision').dataset.pid;")
rep("async function revealCard() {\n", "async function revealCard() {\n  if (!G.running) return;\n")
rep("function goDecision() {\n", "function goDecision() {\n  if (!G.running) return;\n")
rep("async function revealChoices() {\n", "async function revealChoices() {\n  if (!G.running) return;\n")
rep("async function bust(type) {\n", "async function bust(type) {\n  if (!G.running) return;\n")
rep("function endRound(busted) {\n", "function endRound(busted) {\n  if (!G.running) return;\n")
rep("async function nextRound() {\n", "async function nextRound() {\n  if (!G.running) return;\n")
rep("function askHuman() {\n", "function askHuman() {\n  if (!G.running) return;\n")
# 事件綁定
rep("""$$('#cmd-menu button').forEach((b, i) => { b.onclick = () => onChoice(b.dataset.c); b.addEventListener('pointerenter', () => { if (cmdIndex !== i) { AudioEngine.sfx('cursor'); setCursor(i); } }); b.addEventListener('focus', () => setCursor(i)); });""",
    """$$('#cmd-menu button').forEach((b, i) => { b.onclick = () => { if (!cmdEnabled(i)) return; setCursor(i); runCmd(b.dataset.c); }; b.addEventListener('pointerenter', () => { if (cmdIndex !== i) { AudioEngine.sfx('cursor'); setCursor(i); } }); b.addEventListener('focus', () => setCursor(i)); });
$('#btn-quit').onclick = quitGame;""")
rep("""$('#log-toggle').onclick = () => { const l = $('#log'); l.hidden = !l.hidden; l.scrollTop = l.scrollHeight; };
""", "")
rep("""document.addEventListener('keydown', e => {
  if ($('#decision').hidden || G.phase !== 'decide') return;
  if (e.key === 'ArrowUp' || e.key === 'ArrowDown') { e.preventDefault(); AudioEngine.sfx('cursor'); setCursor(cmdIndex === 0 ? 1 : 0); }
  if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onChoice(cmdIndex === 0 ? 'go' : 'leave'); }
});""",
"""document.addEventListener('keydown', e => {
  if (!$('#lobby').hidden || !$('#modal').hidden || !$('#handoff').hidden) return;
  if (e.key === 'ArrowUp' || e.key === 'ArrowDown') { e.preventDefault(); AudioEngine.sfx('cursor'); let i = cmdIndex; for (let k = 0; k < 4; k++) { i = (i + (e.key === 'ArrowDown' ? 1 : 3)) % 4; if (cmdEnabled(i)) break; } setCursor(i); }
  if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (cmdEnabled(cmdIndex)) runCmd(CMDS[cmdIndex]); }
});""")
# 亮牌後隊員窗顏色重置時也更新 mystat
rep("const G = { mode: 'solo', levels: [3, 3, 3], players: [], round: 0,", "const G = { running: false, mode: 'solo', levels: [3, 3, 3], players: [], round: 0,")
# 舊的 lockmsg 引用清掉
s = s.replace("$('#lockmsg').hidden = false; $('#lockmsg').textContent = '你已在營地，AI 們正在抉擇…';", "")
s = s.replace("$('#lockmsg').hidden = true; ", "")
assert 'decision-who' in s and 'btn-quit2' in s
p.write_text(s, encoding='utf-8'); print('patched ok')
