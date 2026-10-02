#!/usr/bin/env python3
"""Compiles assets/pulse.svg from real GitHub activity (last ~90 days of public events).
Usage: GH_USER=name GITHUB_TOKEN=... python scripts/live_pulse.py   |   python scripts/live_pulse.py --demo"""
import os, sys, json, random, datetime as dt, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "pulse.svg")
DAYS = 91
PENDING = "--pending" in sys.argv
today = dt.date.today()
counts = {}
if "--pending" in sys.argv:
    pass
elif "--demo" in sys.argv:
    random.seed(11)
    counts = {today - dt.timedelta(d): max(0, int(random.gauss(3, 3))) for d in range(DAYS)}
else:
    user, tok = os.environ.get("GH_USER", "Haseeb-kn"), os.environ.get("GITHUB_TOKEN", "")
    for page in (1, 2, 3):
        req = urllib.request.Request(f"https://api.github.com/users/{user}/events/public?per_page=100&page={page}",
                                     headers=({"Authorization": f"Bearer {tok}"} if tok else {}) | {"Accept": "application/vnd.github+json"})
        try:
            for ev in json.load(urllib.request.urlopen(req)):
                d = dt.date.fromisoformat(ev["created_at"][:10]); counts[d] = counts.get(d, 0) + 1
        except Exception as ex:
            print("fetch failed:", ex); break
days = [today - dt.timedelta(DAYS - 1 - i) for i in range(DAYS)]
vals = [counts.get(d, 0) for d in days]
mx = max(vals) or 1
total, peak = sum(vals), max(vals)
streak = 0
for v in reversed(vals):
    if v == 0: break
    streak += 1
cols = ["#0a1a26", "#064e5c", "#00a3b8", "#00e5ff", "#ff2bd6"]
cell, gap, gx, gy = 28, 5, 40, 78
s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 330" width="1000" height="330" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
<style>.c{{animation:p 3.6s ease-in-out infinite}}@keyframes p{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}</style>
<defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<rect width="1000" height="330" fill="#04070d"/><rect x="1" y="1" width="998" height="328" fill="none" stroke="#00e5ff" stroke-opacity=".22"/>
<text x="26" y="30" font-size="12" letter-spacing="3" fill="#00e5ff">ACTIVITY MATRIX / LAST {DAYS} DAYS{"  /  AWAITING FIRST SYNC" if PENDING else ""}</text>
<text x="974" y="30" font-size="11" letter-spacing="2" text-anchor="end" fill="#5b7f94">SOURCE: GITHUB EVENT STREAM</text>'''
for i, v in enumerate(vals):
    col, row = divmod(i, 7)
    lvl = 0 if v == 0 else (4 if v == mx else min(3, 1 + int(3 * v / mx)))
    x, y = gx + col * (cell + gap), gy + row * (cell + gap)
    s += f'<rect class="c" x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{cols[lvl]}" style="animation-delay:{-((col*7+row*3)%36)/10:.1f}s"/>'
sx = 560
for i, (lab, val, col) in enumerate([("TOTAL EVENTS", "--" if PENDING else total, "#00e5ff"), ("PEAK / DAY", "--" if PENDING else peak, "#ff2bd6"), ("ACTIVE STREAK", "--" if PENDING else f"{streak}d", "#39ff88")]):
    s += f'<text x="{sx+i*145}" y="110" font-size="10" letter-spacing="3" fill="#5b7f94">{lab}</text><text x="{sx+i*145}" y="156" font-size="42" font-weight="700" fill="{col}" filter="url(#glow)">{val}</text>'
s += f'<text x="{sx}" y="196" font-size="10" letter-spacing="3" fill="#5b7f94">WEEKDAY LOAD</text>'
wd = [0] * 7
for d, v in zip(days, vals): wd[d.weekday()] += v
wm = max(wd) or 1
for i, (n, v) in enumerate(zip("MON TUE WED THU FRI SAT SUN".split(), wd)):
    x = sx + i * 58; bh = 80 * v / wm
    s += f'<text x="{x}" y="318" font-size="10" fill="#5b7f94">{n}</text><rect x="{x}" y="{302-bh:.0f}" width="40" height="{bh:.0f}" fill="#00e5ff" fill-opacity=".8"><animate attributeName="height" values="0;{bh:.0f}" dur="1.2s" fill="freeze"/><animate attributeName="y" values="302;{302-bh:.0f}" dur="1.2s" fill="freeze"/></rect>'
open(OUT, "w").write(s + "</svg>\n")
print("pulse.svg written", total, peak, streak)
