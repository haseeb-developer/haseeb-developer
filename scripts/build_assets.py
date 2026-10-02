#!/usr/bin/env python3
"""HASEEB//OS asset compiler. Every panel in /assets is generated here from the DATA block.
Source of truth: https://haseebkn.vercel.app/   Run: python scripts/build_assets.py"""
import math, random, os, html
random.seed(7)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

# ───────────────────────── DATA (from haseebkn.vercel.app) ─────────────────────────
HANDLE = "haseeb-kn"
NAME = "HASEEB"
ROLE = "FRONTEND & SHOPIFY DEVELOPER"
STATS = [("PROJECTS", "100+"), ("SHOPIFY / WP", "20+"), ("YEARS", "4+"), ("LIGHTHOUSE", "90+")]
RADAR_SIGNALS = [
    ("Performance", "Homepage load time · 3.4s to 1.2s", .88),
    ("Release cadence", "Weekly production releases", .78),
    ("Checkout outcome", "Abandonment reduced nearly 20%", .82),
    ("Design fidelity", "Figma translated to pixel-accurate UI", .72),
    ("Code stewardship", "Maintainability over quick fixes", .86),
    ("Product discovery", "Business context before implementation", .68),
]
WORK = {
    "SHOPIFY": ["Wear London","Hudson Valley Fisheries","Nulastin","Payet Maison","Her Height","BarGear","Happy Day Pets","GolfTailor","Beach Weekend",
                "Sulene Serenity","More Hair Organics","Affinity Home Medical","Ordek Waterfowl","Happy Hands World","AZO Products","Archer Jerky","Trina Hot Sauce"],
    "WEB APPS": ["PanteraGPT","Brisbane Gateway","Zooplus","Kit","SkinDoc","Saalz CRM","Skyscanner","Ecommerce Store (Next.js)","Secure Dev Platform","API Manager"],
    "WORDPRESS": ["Petco Pakistan","MightyCall","SharePoint Design Works","Wolfpack Wrestling TX","Learnmate Australia"],
    "UI/UX": ["FarmInBox","TerraPay","TenTwenty","Colab Software"],
}
STACK_MATRIX = [
    ("Languages", ["JavaScript", "TypeScript", "HTML", "CSS", "SQL"]),
    ("Frontend", ["React.js", "Next.js", "Redux Toolkit", "Tailwind CSS", "SCSS", "Responsive Design", "REST APIs"]),
    ("Ecommerce & CMS", ["Shopify", "Shopify Liquid", "WordPress", "WooCommerce"]),
    ("Backend & Platform", ["Supabase", "Supabase Auth", "PostgreSQL", "Vercel", "Netlify", "Clerk"]),
    ("Tools & Workflow", ["Git", "GitHub", "VS Code", "Cursor", "npm", "Figma"]),
    ("Security & Engineering", ["Authentication", "Encryption", "API Integration", "Database Design", "RLS"]),
]
STACK_EXPLORING = ["Linux", "Docker", "Python", "Agentic AI", "AI workflow"]
STACK_DAILY = "Claude Code (Max plan) · Cursor (Pro plan)"
# ────────────────────────────────────────────────────────────────────────────────────
C = dict(bg="#04070d", cy="#00e5ff", mg="#ff2bd6", am="#ffb300", gr="#39ff88", dim="#5b7f94", tx="#d6f4ff")
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
e = html.escape
SP = chr(160)

def head(w, h):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}">
<defs>
<pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{C['cy']}" stroke-opacity=".07"/><animateTransform attributeName="patternTransform" type="translate" from="0 0" to="40 40" dur="6s" repeatCount="indefinite"/></pattern>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C['cy']}" stop-opacity="0"/><stop offset="1" stop-color="{C['cy']}" stop-opacity=".16"/></linearGradient>
<linearGradient id="wedge" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="{C['gr']}" stop-opacity=".55"/><stop offset="1" stop-color="{C['gr']}" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{w}" height="{h}" fill="{C['bg']}"/><rect width="{w}" height="{h}" fill="url(#g)"/>
'''

def frame(w, h, title, tag):
    s = f'<rect x="1" y="1" width="{w-2}" height="{h-2}" fill="none" stroke="{C["cy"]}" stroke-opacity=".22"/>'
    for x, y, dx, dy in [(0,0,1,1),(w,0,-1,1),(0,h,1,-1),(w,h,-1,-1)]:
        s += f'<path d="M{x+dx*2} {y+dy*24}V{y+dy*2}H{x+dx*24}" fill="none" stroke="{C["cy"]}" stroke-width="2" filter="url(#glow)"/>'
    s += f'<text x="26" y="30" fill="{C["cy"]}" font-size="12" letter-spacing="3">{e(title)}</text>'
    s += f'<text x="{w-40}" y="30" fill="{C["dim"]}" font-size="11" text-anchor="end" letter-spacing="2">{e(tag)}</text>'
    s += f'<circle cx="{w-26}" cy="26" r="3" fill="{C["gr"]}"><animate attributeName="opacity" values="1;.15;1" dur="1.4s" repeatCount="indefinite"/></circle>'
    s += f'<rect width="{w}" height="70" fill="url(#scan)"><animate attributeName="y" values="-70;{h}" dur="6s" repeatCount="indefinite"/></rect>'
    return s

def stack_matrix():
    w, h = 960, 370
    rng = random.Random(3)
    total_tools = sum(len(items) for _, items in STACK_MATRIX)
    s = head(w, h)
    s += (f'<rect x="20" y="20" width="920" height="330" rx="6" fill="#0a1122" stroke="#1c2a4a"/>'
          '<path d="M20 50H940" stroke="#1c2a4a"/>'
          '<rect x="32" y="31" width="8" height="8" fill="#ffb454"><animate attributeName="opacity" values="1;.2;1" dur="2.4s" repeatCount="indefinite"/></rect>'
          f'<text x="48" y="40" font-size="11" fill="#7fe8ff" letter-spacing="1.5">STACK_MATRIX</text>'
          f'<text x="928" y="40" text-anchor="end" font-size="11" fill="#5d6f93">{total_tools} tools / {len(STACK_MATRIX)} domains</text>'
          '<path d="M20 32V20H32 M928 20H940V32 M940 338V350H928 M32 350H20V338" fill="none" stroke="#7fe8ff" stroke-width="1.5"/>')
    s += '<clipPath id="stack-rain-clip"><rect x="21" y="51" width="918" height="298"/></clipPath>'
    glyphs = "01ABCDEF<>{}/;=#"
    rain = []
    for i in range(len(STACK_MATRIX)):
        for _ in range(3):
            rx = 40 + i * 150 + rng.randint(0, 130)
            pattern = [rng.choice(glyphs) for _ in range(12)]
            glyph_stream = "".join(
                f'<text x="{rx}" y="{60 + j * 14}" font-size="10" fill="#7fe8ff" opacity=".07">{e(pattern[j % 12])}</text>'
                for j in range(-12, 24)
            )
            rain.append(
                f'<g>{glyph_stream}<animateTransform attributeName="transform" type="translate" values="0 0;0 168" dur="{rng.uniform(5, 9):.1f}s" repeatCount="indefinite"/></g>'
            )
    s += f'<g clip-path="url(#stack-rain-clip)">{"".join(rain)}</g>'
    for column, (domain, items) in enumerate(STACK_MATRIX):
        x = 40 + column * 150
        s += f'<text x="{x}" y="64" font-size="10.5" fill="#7fe8ff">{e(domain)}</text>'
        s += f'<path d="M{x} 72H{x+134}" stroke="#1c2a4a"/>'
        for row, item in enumerate(items):
            y = 96 + row * 24
            s += f'<rect x="{x}" y="{y-7}" width="4" height="4" fill="#5d6f93"/>'
            s += f'<text x="{x+12}" y="{y}" font-size="13" fill="#c7d4ea">{e(item)}</text>'
        offsets = ";".join(f"0 {row*24}" for row in range(len(items)))
        s += (f'<g><rect x="{x-6}" y="81" width="142" height="21" fill="#7fe8ff" opacity=".12"/>'
              f'<rect x="{x-6}" y="81" width="2" height="21" fill="#ffb454"/>'
              f'<animateTransform attributeName="transform" type="translate" values="{offsets}" calcMode="discrete" dur="{len(items)*1.1:.1f}s" begin="{column*.5:.1f}s" repeatCount="indefinite"/></g>')
    s += '<path d="M40 262H920" stroke="#1c2a4a"/>'
    s += '<text x="40" y="288" font-size="12" fill="#5d6f93">exploring</text>'
    s += f'<text x="150" y="288" font-size="13" fill="#ffb454">{e(" · ".join(STACK_EXPLORING))}</text>'
    s += '<text x="40" y="318" font-size="12" fill="#5d6f93">daily rotation</text>'
    s += f'<text x="150" y="318" font-size="13" fill="#c7d4ea">{e(STACK_DAILY)}</text>'
    return s


def radar():
    w, h, period = 960, 480, 18
    panel, edge = "#0a1122", "#1c2a4a"
    ice, amber, violet, text, dim = "#7fe8ff", "#ffb454", "#7c78ff", "#c7d4ea", "#5d6f93"
    cx, cy, radius = 250, 250, 135
    b = [head(w, h)]

    def panel_box(x, y, pw, ph, title, right=""):
        return (
            f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="6" fill="{panel}" stroke="{edge}"/>'
            f'<path d="M{x} {y+30}H{x+pw}" stroke="{edge}"/>'
            f'<rect x="{x+12}" y="{y+11}" width="8" height="8" fill="{amber}"><animate attributeName="opacity" values="1;.2;1" dur="2.4s" repeatCount="indefinite"/></rect>'
            f'<text x="{x+28}" y="{y+20}" font-size="11" fill="{ice}" letter-spacing="1.5">{e(title)}</text>'
            f'<text x="{x+pw-12}" y="{y+20}" font-size="10" fill="{dim}" text-anchor="end">{e(right)}</text>'
            f'<path d="M{x} {y+12}V{y}H{x+12} M{x+pw-12} {y}H{x+pw}V{y+12} M{x+pw} {y+ph-12}V{y+ph}H{x+pw-12} M{x+12} {y+ph}H{x}V{y+ph-12}" fill="none" stroke="{ice}" stroke-width="1.5"/>'
        )

    b.append(panel_box(20, 20, 460, 440, "DELIVERY_RADAR", f"SWEEP {period}s"))
    for ring in range(1, 5):
        dash = ' stroke-dasharray="3 5"' if ring < 4 else ""
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{radius*ring/4:.0f}" fill="none" stroke="{edge}"{dash}/>')
    b.append(f'<path d="M{cx-radius} {cy}H{cx+radius}M{cx} {cy-radius}V{cy+radius}" stroke="{edge}"/>')
    for angle in range(0, 360, 10):
        sine, cosine = math.sin(math.radians(angle)), math.cos(math.radians(angle))
        tick = 10 if angle % 30 == 0 else 5
        b.append(f'<path d="M{cx+radius*sine:.1f} {cy-radius*cosine:.1f}L{cx+(radius+tick)*sine:.1f} {cy-(radius+tick)*cosine:.1f}" stroke="{dim}"/>')
        if angle % 30 == 0:
            b.append(f'<text x="{cx+(radius+22)*sine:.1f}" y="{cy-(radius+22)*cosine+4:.1f}" font-size="9" fill="{dim}" text-anchor="middle">{angle:03d}</text>')
    wedge = []
    for step in range(18):
        a1, a2 = math.radians(-step*3), math.radians(-(step+1)*3)
        x1, y1 = cx + radius*math.sin(a1), cy - radius*math.cos(a1)
        x2, y2 = cx + radius*math.sin(a2), cy - radius*math.cos(a2)
        wedge.append(f'<path d="M{cx} {cy}L{x1:.1f} {y1:.1f}A{radius} {radius} 0 0 0 {x2:.1f} {y2:.1f}Z" fill="{ice}" opacity="{.28*(1-step/18):.3f}"/>')
    b.append(f'<g>{"".join(wedge)}<path d="M{cx} {cy}V{cy-radius}" stroke="{ice}" stroke-width="1.5" filter="url(#glow)"/><animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};360 {cx} {cy}" dur="{period}s" repeatCount="indefinite"/></g>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{ice}"/>')

    b.append(panel_box(500, 20, 440, 440, "SIGNAL_LOG", "verified delivery outcomes"))
    for index, (name, detail, strength) in enumerate(RADAR_SIGNALS):
        angle = (25 + index*60) % 360
        distance = radius * (1 - strength*.72)
        x = cx + distance*math.sin(math.radians(angle))
        y = cy - distance*math.cos(math.radians(angle))
        begin = angle/360*period
        fade = f'<animate attributeName="opacity" values=".18;.18;1;.18" keyTimes="0;.82;.9;1" dur="{period}s" begin="{begin:.2f}s" repeatCount="indefinite"/>'
        b.append(f'<g opacity=".22"><circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{amber}"><title>{e(name)}: {e(detail)}</title>{fade}</circle>'
                 f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="none" stroke="{amber}"><animate attributeName="r" values="4;19;19" keyTimes="0;.2;1" dur="{period}s" begin="{begin:.2f}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;0" keyTimes="0;.2;1" dur="{period}s" begin="{begin:.2f}s" repeatCount="indefinite"/></circle></g>')
        y_text = 76 + index*54
        b.append(f'<g><rect x="522" y="{y_text-12}" width="3" height="40" fill="{violet if index%2 else ice}" opacity=".75"/>'
                 f'<text x="540" y="{y_text}" font-size="14" fill="{text}" font-weight="700">{e(name)}</text>'
                 f'<text x="540" y="{y_text+20}" font-size="10.5" fill="{dim}">{e(detail)}</text>'
                 f'<circle cx="920" cy="{y_text-4}" r="3" fill="{ice if index%2==0 else violet}"><animate attributeName="opacity" values=".45;1;.45" dur="{3.2+index*.35:.1f}s" repeatCount="indefinite"/></circle></g>')
    b.append(f'<text x="40" y="444" font-size="8.5" fill="{dim}">CLIENT-REPORTED / PORTFOLIO FACTS · POSITIONS QUALITATIVE, NOT SCORES</text>')
    b.append(f'<text x="920" y="444" text-anchor="end" font-size="8.5" fill="{dim}">SOURCE: HASEEB-KN.VERCEL.APP</text>')
    save("radar.svg", "".join(b))

def seq(t0, cycle):
    a = min(t0 / cycle, .94)
    return (f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{a:.4f};{a+.012:.4f};.97;1" dur="{cycle}s" repeatCount="indefinite"/>')

def save(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body + "</svg>\n")

def button(label):
    w = 460
    label = label.upper()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 40" width="{w}" height="40" role="img" aria-label="{e(label)}"><style>text{{font-family:{FONT}}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style><defs></defs><rect x="1" y="1" width="{w-2}" height="38" rx="4" fill="#0a1122" stroke="#1c2a4a"/><rect x="1" y="1" width="{w-2}" height="38" rx="4" fill="none" stroke="#7fe8ff" stroke-dasharray="6 8"><animate attributeName="stroke-dashoffset" values="0;-28" dur="1.4s" repeatCount="indefinite"/></rect><rect x="18" y="16" width="7" height="7" fill="#ffb454"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></rect><text x="{w/2}" y="25" text-anchor="middle" font-size="13" fill="#7fe8ff" letter-spacing="1">{e(label)}</text></svg>'''

def sysinfo():
    w, h = 960, 420
    bg, panel, edge = "#05070d", "#0a1122", "#1c2a4a"
    ice, amber, text, dim = "#7fe8ff", "#ffb454", "#c7d4ea", "#5d6f93"
    fields = [
        ("Subject", "Muhammad Haseeb (Haseeb Khan)"),
        ("Role", "Senior Shopify / React.js Developer"),
        ("Origin", "Islamabad, Pakistan"),
        ("Current", "Markloops · Senior Shopify / React.js"),
        ("Tenure", "4+ years frontend · 100+ projects"),
        ("Delivery", "Weekly releases with product and design"),
        ("Performance", "Homepage load time: 3.4s -> 1.2s"),
        ("Checkout", "Abandonment dropped nearly 20%"),
        ("Approach", "Understand the business before building"),
        ("Status", "available for new engagements"),
    ]
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Animated system information for Muhammad Haseeb, frontend and Shopify developer"><style>text{{font-family:{FONT}}}.wv{{animation:wave 3.4s ease-in-out infinite}}@keyframes wave{{0%,100%{{opacity:.18}}50%{{opacity:1}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style><defs><pattern id="sys-grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#0d172c" stroke-width="1"/></pattern></defs><rect width="{w}" height="{h}" fill="{bg}"/><rect width="{w}" height="{h}" fill="url(#sys-grid)"/>'''

    def panel_box(x, y, pw, ph, title, right=""):
        return (f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="6" fill="{panel}" stroke="{edge}"/>'
                f'<path d="M{x} {y+30}H{x+pw}" stroke="{edge}"/>'
                f'<rect x="{x+12}" y="{y+11}" width="8" height="8" fill="{amber}"><animate attributeName="opacity" values="1;.2;1" dur="2.4s" repeatCount="indefinite"/></rect>'
                f'<text x="{x+28}" y="{y+20}" font-size="11" fill="{ice}" letter-spacing="1.5">{e(title)}</text>'
                f'<text x="{x+pw-12}" y="{y+20}" font-size="11" fill="{dim}" text-anchor="end">{e(right)}</text>'
                f'<path d="M{x} {y+12}V{y}H{x+12} M{x+pw-12} {y}H{x+pw}V{y+12} M{x+pw} {y+ph-12}V{y+ph}H{x+pw-12} M{x+12} {y+ph}H{x}V{y+ph-12}" fill="none" stroke="{ice}" stroke-width="1.5"/>')

    s += panel_box(20, 20, 320, 380, "VISUAL_MAP", "archway / 0xA1")
    cx, cy, radius, arch_center, base = 180, 212, 96, -22, 128
    rng = random.Random(11)

    def in_arch(x, y, r, center, bottom):
        return x * x + (y - center) ** 2 <= r * r if y <= center else abs(x) <= r and y <= bottom

    def arch_edge(x, y):
        return radius - math.hypot(x, y - arch_center) if y <= arch_center else min(radius - abs(x), base - y)

    for gy in range(-120, base + 1, 7):
        dots = []
        for gx in range(-100, 101, 7):
            if not in_arch(gx, gy, radius, arch_center, base):
                continue
            if in_arch(gx, gy, 28, 62, base) and gy > 34:
                dots.append(f'<circle cx="{cx+gx}" cy="{cy+gy}" r="2.2" fill="{amber}"/>')
                continue
            band = int(arch_edge(gx, gy) / 9) % 3
            if band != 1 and rng.random() >= .1:
                dots.append(f'<circle cx="{cx+gx}" cy="{cy+gy}" r="{1.5 if band == 0 else 2.1}" fill="{ice}"/>')
        if dots:
            s += f'<g class="wv" style="animation-delay:-{(gy+120)*.013:.2f}s">{"".join(dots)}</g>'
    s += (f'<rect x="{cx-108}" y="70" width="216" height="2" fill="{ice}" opacity=".7"><animate attributeName="y" values="70;350;70" dur="5.6s" repeatCount="indefinite"/></rect>'
          f'<text x="{cx}" y="378" font-size="11" fill="{dim}" text-anchor="middle">archway :: storefront topology</text>')

    s += panel_box(360, 20, 580, 380, "SYSTEM_INFO", "whoami.sys  live")
    for i, (label, value) in enumerate(fields):
        y = 80 + i * 28
        s += (f'<text x="384" y="{y}" font-size="13" fill="{dim}">{e(label)}</text>'
              f'<text x="520" y="{y}" font-size="13" fill="{amber if label == "Status" else text}">{e(value)}</text>'
              f'<path d="M384 {y+11}H916" stroke="#101c36"/>')
    equalizer_rng = random.Random(5)
    max_height = min(120, max(24, 390 - (80 + len(fields) * 28 + 24)))
    for index in range(52):
        heights = [equalizer_rng.uniform(.12, 1) * max_height for _ in range(4)]
        heights.append(heights[0])
        height_values = ";".join(f"{height:.1f}" for height in heights)
        y_values = ";".join(f"{390-height:.1f}" for height in heights)
        duration = equalizer_rng.uniform(1.6, 3.6)
        opacity = .35 + .65 * (index / 52)
        x = 384 + index * 10
        s += (f'<rect x="{x}" y="{390-heights[0]:.1f}" width="6" height="{heights[0]:.1f}" fill="{ice}" opacity="{opacity:.2f}">'
              f'<animate attributeName="height" values="{height_values}" dur="{duration:.1f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="y" values="{y_values}" dur="{duration:.1f}s" repeatCount="indefinite"/></rect>')
    return s + "</svg>\n"

def curve(pts):
    d = f"M{pts[0][0]:.0f} {pts[0][1]:.0f}"
    for p, q in zip(pts, pts[1:]):
        mx = (p[0] + q[0]) / 2
        d += f" C{mx:.0f} {p[1]:.0f} {mx:.0f} {q[1]:.0f} {q[0]:.0f} {q[1]:.0f}"
    return d

def divider():
    w, h = 960, 36
    path = "M0 18"
    for x in (150, 330, 520, 700, 850):
        path += f"H{x}l6 -2l6 -12l8 26l8 -22l6 10l6 0"
    path += f"H{w}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Animated pulse divider"><style>@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style><path d="{path}" fill="none" stroke="#1c2a4a" stroke-width="1.4"/><path d="{path}" fill="none" stroke="#7fe8ff" stroke-width="1.8" pathLength="1000" stroke-dasharray="60 940"><animate attributeName="stroke-dashoffset" values="1000;0" dur="5s" repeatCount="indefinite"/></path></svg>\n'''

# ───────────────────────── 1. HERO ─────────────────────────
def hero():
    w, h = 1000, 450
    s = head(w, h) + frame(w, h, "HASEEB//OS  KERNEL 6.2.0", "ISLAMABAD / PK  SESSION 0x7F3A")
    cx, cy = 800, 225
    for r, da, d, dr, op in [(165,"3 9",40,1,.5),(135,"46 14",22,-1,.7),(105,"2 6",14,1,.5),(72,"90 24",9,-1,.8)]:
        s += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["cy"]}" stroke-opacity="{op}" stroke-dasharray="{da}">'
              f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="{360*dr} {cx} {cy}" dur="{d}s" repeatCount="indefinite"/></circle>')
    s += (f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="{C["mg"]}" stroke-width="3" stroke-dasharray="120 830" filter="url(#glow)">'
          f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="4s" repeatCount="indefinite"/></circle>')
    ticks = ""
    for a in range(0, 360, 6):
        r2, ra = (182 if a % 30 == 0 else 177), math.radians(a)
        ticks += f'M{cx+172*math.cos(ra):.1f} {cy+172*math.sin(ra):.1f}L{cx+r2*math.cos(ra):.1f} {cy+r2*math.sin(ra):.1f}'
    s += f'<path d="{ticks}" stroke="{C["cy"]}" stroke-opacity=".6" fill="none"><animateTransform attributeName="transform" type="rotate" from="360 {cx} {cy}" to="0 {cx} {cy}" dur="90s" repeatCount="indefinite"/></path>'
    hexp = " ".join(f"{cx+44*math.cos(math.radians(60*i+30)):.1f},{cy+44*math.sin(math.radians(60*i+30)):.1f}" for i in range(6))
    s += f'<polygon points="{hexp}" fill="{C["cy"]}" fill-opacity=".08" stroke="{C["cy"]}" stroke-width="2" filter="url(#glow)"><animate attributeName="fill-opacity" values=".05;.3;.05" dur="2.4s" repeatCount="indefinite"/></polygon>'
    s += f'<text x="{cx}" y="{cy+8}" text-anchor="middle" fill="{C["tx"]}" font-size="22" font-weight="700" letter-spacing="2">HK</text>'
    s += f'<text x="48" y="130" font-size="92" font-weight="800" letter-spacing="10" fill="{C["cy"]}" filter="url(#glow)">{NAME}</text>'
    s += (f'<text x="48" y="130" font-size="92" font-weight="800" letter-spacing="10" fill="{C["mg"]}" opacity="0">{NAME}'
          '<animate attributeName="opacity" values="0;0;.85;0;0;.6;0;0" keyTimes="0;.62;.63;.65;.8;.805;.82;1" dur="7s" repeatCount="indefinite"/>'
          '<animate attributeName="x" values="48;55;43;48" keyTimes="0;.63;.805;1" dur="7s" repeatCount="indefinite"/></text>')
    s += f'<text x="52" y="160" font-size="14" letter-spacing="5" fill="{C["tx"]}">{e(ROLE)}</text>'
    s += f'<text x="52" y="182" font-size="11" letter-spacing="2" fill="{C["dim"]}">React / Next.js / TypeScript / Shopify Plus / Liquid</text>'
    boot = [("mount /work  36 projects indexed", "OK"), ("load react.js + next.js", "OK"), ("load typescript", "OK"), ("link shopify liquid + plus", "OK"),
            ("attach supabase + clerk", "OK"), ("audit core web vitals 90+", "OK"), ("open for new engagements", "READY")]
    cyc = 16
    for i, (t, st) in enumerate(boot):
        y = 224 + i * 20
        col = C["gr"] if st == "OK" else C["am"]
        s += (f'<g opacity="0">{seq(1 + i * 1.1, cyc)}<text x="52" y="{y}" font-size="12" fill="{C["dim"]}">[{i*37+12:04d}.{(i*91)%1000:03d}] {e(t)}</text>'
              f'<text x="500" y="{y}" font-size="12" fill="{col}" text-anchor="end">[ {st} ]</text></g>')
    for i, (lab, val) in enumerate(STATS):
        x, col = 52 + i * 112, [C["cy"], C["gr"], C["mg"], C["am"]][i]
        s += (f'<text x="{x}" y="392" font-size="9" letter-spacing="2" fill="{C["dim"]}">{lab}</text>'
              f'<text x="{x}" y="418" font-size="26" font-weight="700" fill="{col}" filter="url(#glow)">{val}</text>'
              f'<rect x="{x}" y="426" width="96" height="3" fill="{col}" fill-opacity=".15"/>'
              f'<rect x="{x}" y="426" height="3" fill="{col}"><animate attributeName="width" values="0;96;96;0" keyTimes="0;.3;.9;1" dur="{5+i}s" repeatCount="indefinite"/></rect>')
    save("hero.svg", s)

# ───────────────────────── 2. SKILL GRAPH ─────────────────────────
def skills():
    w, h = 1000, 400
    s = head(w, h) + frame(w, h, "SKILL GRAPH / STACK DEPENDENCIES", "22 NODES  5 TIERS")
    L = [("LANGUAGES", ["HTML", "CSS", "JavaScript", "TypeScript", "Python"]),
         ("FRONTEND", ["React.js", "Next.js", "Redux Toolkit", "Tailwind CSS", "SCSS"]),
         ("PLATFORMS", ["Shopify", "Liquid", "WordPress", "Supabase", "Clerk"]),
         ("DELIVERY", ["Vercel", "Netlify", "Git / GitHub"]),
         ("OUTPUT", ["Shopify storefronts", "Next.js web apps", "Dashboards & CRMs", "Marketing sites"])]
    xs = [70 + i * 190 for i in range(5)]
    top, bot = 80, h - 56
    pos, tiers = {}, []
    for li, (tn, names) in enumerate(L):
        n = len(names)
        for i, nm in enumerate(names):
            pos[nm] = (xs[li], top + (bot - top) / (n - 1) * i)
        tiers.append(li)
    for a in range(4):
        for p in L[a][1]:
            for q in L[a + 1][1]:
                s += f'<line x1="{pos[p][0]}" y1="{pos[p][1]:.0f}" x2="{pos[q][0]}" y2="{pos[q][1]:.0f}" stroke="{C["cy"]}" stroke-opacity=".05"/>'
    chains = [(["JavaScript", "React.js", "Supabase", "Vercel", "Next.js web apps"], C["cy"]),
              (["TypeScript", "Next.js", "Clerk", "Vercel", "Dashboards & CRMs"], C["mg"]),
              (["HTML", "Tailwind CSS", "Liquid", "Git / GitHub", "Shopify storefronts"], C["gr"]),
              (["CSS", "SCSS", "WordPress", "Netlify", "Marketing sites"], C["am"]),
              (["JavaScript", "Redux Toolkit", "Supabase", "Vercel", "Dashboards & CRMs"], C["cy"]),
              (["TypeScript", "React.js", "Shopify", "Git / GitHub", "Shopify storefronts"], C["gr"])]
    for k, (ch, col) in enumerate(chains):
        d = curve([pos[n] for n in ch])
        s += f'<path d="{d}" fill="none" stroke="{col}" stroke-opacity=".3" stroke-width="1.2"/>'
        for j in range(2):
            dur = 4.5 + k * .3
            s += f'<circle r="3.4" fill="{col}" filter="url(#glow)"><animateMotion path="{d}" dur="{dur:.1f}s" begin="{k*.7 + j*dur/2:.1f}s" repeatCount="indefinite"/></circle>'
    for li, (tn, names) in enumerate(L):
        for nm in names:
            x, y = pos[nm]
            exploring = nm == "Python"
            col = C["am"] if exploring else (C["mg"] if li == 4 else C["cy"])
            if li == 4:
                s += f'<rect x="{x-6}" y="{y-6:.0f}" width="12" height="12" fill="{C["bg"]}" stroke="{col}" stroke-width="1.5"><animate attributeName="stroke-opacity" values="1;.3;1" dur="{random.uniform(1.6,3):.1f}s" repeatCount="indefinite"/></rect>'
            else:
                s += (f'<circle cx="{x}" cy="{y:.0f}" r="6" fill="{C["bg"]}" stroke="{col}" stroke-width="1.5"><animate attributeName="r" values="5;8;5" dur="{random.uniform(1.8,4):.1f}s" begin="{random.uniform(0,3):.1f}s" repeatCount="indefinite"/></circle>')
            lab = e(nm) + (f'<tspan fill="{C["am"]}"> (exploring)</tspan>' if exploring else "")
            s += (f'<text x="{x+13}" y="{y+3.5:.1f}" font-size="10.5" fill="{C["bg"]}" stroke="{C["bg"]}" stroke-width="5">{e(nm)}{"  (exploring)".replace(" ", SP) if exploring else ""}</text>'
                  f'<text x="{x+13}" y="{y+3.5:.1f}" font-size="10.5" fill="{C["tx"]}">{lab}</text>')
    for li, (tn, _) in enumerate(L):
        s += f'<text x="{xs[li]}" y="{h-18}" font-size="10" letter-spacing="3" fill="{C["dim"]}">{tn}</text>'
    save("skills.svg", s)

# ───────────────────────── 4. PIPELINE / ARCHITECTURE ─────────────────────────
def architecture():
    w, h = 1000, 440
    s = head(w, h) + frame(w, h, "SHIPPING PIPELINE / DESIGN TO PRODUCTION", "PACKETS IN FLIGHT")
    N = {"figma": ("FIGMA HANDOFF", "pixel-accurate specs", 95, 225),
         "react": ("REACT / NEXT.JS", "typescript, redux, tailwind", 335, 115), "liquid": ("SHOPIFY LIQUID", "themes, sections", 335, 225), "wp": ("WORDPRESS", "woocommerce, scss", 335, 335),
         "shop": ("SHOPIFY PLUS", "checkout, metafields", 595, 105), "supa": ("SUPABASE + CLERK", "postgres, auth, rls", 595, 225), "rest": ("REST APIS", "integrations", 595, 345),
         "vercel": ("VERCEL / NETLIFY", "deploy", 860, 120), "cwv": ("CORE WEB VITALS", "lighthouse 90+", 860, 232), "git": ("GIT / GITHUB", "weekly releases", 860, 340)}
    E = [("figma","react"),("figma","liquid"),("figma","wp"),("react","shop"),("react","supa"),("react","rest"),("liquid","shop"),("wp","rest"),
         ("shop","cwv"),("shop","git"),("supa","vercel"),("rest","vercel"),("rest","cwv"),("supa","git")]
    bw, bh = 156, 56
    paths = []
    for a, b in E:
        x1, y1, x2, y2 = N[a][2] + bw / 2, N[a][3], N[b][2] - bw / 2, N[b][3]
        mx = (x1 + x2) / 2
        d = f"M{x1:.0f} {y1} C{mx:.0f} {y1} {mx:.0f} {y2} {x2:.0f} {y2}"
        paths.append(d)
        s += f'<path d="{d}" fill="none" stroke="{C["cy"]}" stroke-opacity=".45" stroke-dasharray="4 7"><animate attributeName="stroke-dashoffset" from="22" to="0" dur="1.2s" repeatCount="indefinite"/></path>'
    for i, d in enumerate(paths):
        for k in range(2):
            col = C["mg"] if (i + k) % 3 == 0 else C["gr"]
            s += f'<circle r="3.4" fill="{col}" filter="url(#glow)"><animateMotion path="{d}" dur="{random.uniform(2.2,4):.1f}s" begin="{random.uniform(0,3):.1f}s" repeatCount="indefinite"/></circle>'
    for k, (lab, sub, x, y) in N.items():
        s += (f'<rect x="{x-bw/2}" y="{y-bh/2}" width="{bw}" height="{bh}" fill="#07111d" stroke="{C["cy"]}" stroke-opacity=".7"/>'
              f'<rect x="{x-bw/2}" y="{y-bh/2}" width="4" height="{bh}" fill="{C["cy"]}"/>'
              f'<text x="{x-bw/2+16}" y="{y-3}" font-size="11" letter-spacing="1" fill="{C["tx"]}">{lab}</text>'
              f'<text x="{x-bw/2+16}" y="{y+14}" font-size="9" fill="{C["dim"]}">{sub}</text>'
              f'<circle cx="{x+bw/2-12}" cy="{y-bh/2+12}" r="3" fill="{C["gr"]}"><animate attributeName="opacity" values="1;.1;1" dur="{random.uniform(1,2.6):.1f}s" repeatCount="indefinite"/></circle>')
    for x, t in [(95, "DESIGN"), (335, "BUILD"), (595, "PLATFORM"), (860, "SHIP")]:
        s += f'<text x="{x}" y="{h-18}" text-anchor="middle" font-size="10" letter-spacing="4" fill="{C["dim"]}">{t}</text>'
    save("pipeline.svg", s)

# ───────────────────────── 6. WORK MATRIX ─────────────────────────
def work():
    w, h = 1000, 340
    total = sum(len(v) for v in WORK.values())
    s = head(w, h) + frame(w, h, "WORK MATRIX / SELECTED BUILDS", f"{total} INDEXED  SOURCE: HASEEBKN.VERCEL.APP")
    colors = {"SHOPIFY": C["gr"], "WEB APPS": C["cy"], "WORDPRESS": C["am"], "UI/UX": C["mg"]}
    layout = {"SHOPIFY": [(30, 0, 9), (215, 9, 17)], "WEB APPS": [(420, 0, 10)], "WORDPRESS": [(660, 0, 5)], "UI/UX": [(660, 0, 4)]}
    heads = {"SHOPIFY": (30, 62), "WEB APPS": (420, 62), "WORDPRESS": (660, 62), "UI/UX": (660, 62 + 24 + 5 * 20 + 6)}
    DUR, idx = total * .28, 0
    s += f'<line x1="400" y1="52" x2="400" y2="{h-30}" stroke="{C["cy"]}" stroke-opacity=".15"/><line x1="640" y1="52" x2="640" y2="{h-30}" stroke="{C["cy"]}" stroke-opacity=".15"/>'
    for cat, names in WORK.items():
        col = colors[cat]
        hx, hy = heads[cat]
        s += f'<text x="{hx}" y="{hy}" font-size="11" letter-spacing="3" fill="{col}">{cat}  <tspan fill="{C["dim"]}">{len(names)}</tspan></text>'
        for (x, a, b) in layout[cat]:
            for r, nm in enumerate(names[a:b]):
                y = hy + 24 + r * 20
                anim = f'<animate attributeName="opacity" values=".45;1;.45;.45" keyTimes="0;.012;.05;1" dur="{DUR:.2f}s" begin="{idx*.28:.2f}s" repeatCount="indefinite"/>'
                s += (f'<g opacity=".45">{anim}<rect x="{x}" y="{y-8}" width="7" height="7" fill="{col}"/>'
                      f'<text x="{x+14}" y="{y}" font-size="11" fill="{C["tx"]}">{e(nm)}</text></g>')
                idx += 1
    s += f'<text x="30" y="{h-14}" font-size="9" fill="{C["dim"]}" letter-spacing="1">each node lights up in sequence: a live pass over every shipped build</text>'
    save("work.svg", s)

if __name__ == "__main__":
    with open(os.path.join(OUT, "sysinfo.svg"), "w", encoding="utf-8") as f:
        f.write(sysinfo())
    save("stack.svg", stack_matrix())
    for fn in (hero, skills, radar, architecture, work):
        fn()
    with open(os.path.join(OUT, "divider.svg"), "w", encoding="utf-8") as f:
        f.write(divider())
    for label in ("open portfolio", "hire me"):
        with open(os.path.join(OUT, f"btn-{label.replace(' ', '-')}.svg"), "w", encoding="utf-8") as f:
            f.write(button(label) + "\n")
    print("compiled:", sorted(os.listdir(OUT)))
