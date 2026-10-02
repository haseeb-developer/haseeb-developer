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
CAPABILITIES = [  # (label, strength fraction, display)  strength = years in production / 4.4 (from experience timeline)
    ("HTML", 1.0, "4y+"), ("CSS", 1.0, "4y+"), ("JAVASCRIPT", 1.0, "4y+"), ("REACT.JS", 1.0, "4y+"),
    ("SHOPIFY", 1.0, "4y+"), ("LIQUID", 1.0, "4y+"), ("NEXT.JS", .73, "3y+"), ("TYPESCRIPT", .73, "3y+"), ("PYTHON", .15, "EXPLORING")]
TERMINAL = [
    ('c', "haseeb whoami"),
    ('o', "name", "Muhammad Haseeb (Haseeb Khan)"),
    ('o', "role", "Senior Shopify / React.js Developer @ Markloops"),
    ('o', "base", "Islamabad, Pakistan"),
    ('c', "haseeb stack --primary"),
    ('o', "frontend", "React.js, Next.js, TypeScript, Tailwind CSS"),
    ('o', "commerce", "Shopify Plus, Liquid, WordPress, WooCommerce"),
    ('c', "haseeb stats"),
    ('o', "delivered", "100+ projects, 20+ Shopify and WordPress builds"),
    ('o', "lighthouse", "60s to 90+ across client sites"),
    ('c', "haseeb status"),
    ('o', "availability", "open for new engagements"),
    ('o', "contact", "mhaseebkn@gmail.com"),
    ('c', "haseeb --await-input"),
]
WORK = {
    "SHOPIFY": ["Wear London","Hudson Valley Fisheries","Nulastin","Payet Maison","Her Height","BarGear","Happy Day Pets","GolfTailor","Beach Weekend",
                "Sulene Serenity","More Hair Organics","Affinity Home Medical","Ordek Waterfowl","Happy Hands World","AZO Products","Archer Jerky","Trina Hot Sauce"],
    "WEB APPS": ["PanteraGPT","Brisbane Gateway","Zooplus","Kit","SkinDoc","Saalz CRM","Skyscanner","Ecommerce Store (Next.js)","Secure Dev Platform","API Manager"],
    "WORDPRESS": ["Petco Pakistan","MightyCall","SharePoint Design Works","Wolfpack Wrestling TX","Learnmate Australia"],
    "UI/UX": ["FarmInBox","TerraPay","TenTwenty","Colab Software"],
}
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

def seq(t0, cycle):
    a = min(t0 / cycle, .94)
    return (f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{a:.4f};{a+.012:.4f};.97;1" dur="{cycle}s" repeatCount="indefinite"/>')

def save(name, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(body + "</svg>\n")

def curve(pts):
    d = f"M{pts[0][0]:.0f} {pts[0][1]:.0f}"
    for p, q in zip(pts, pts[1:]):
        mx = (p[0] + q[0]) / 2
        d += f" C{mx:.0f} {p[1]:.0f} {mx:.0f} {q[1]:.0f} {q[0]:.0f} {q[1]:.0f}"
    return d

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

# ───────────────────────── 3. RADAR ─────────────────────────
def radar():
    w, h, P = 1000, 470, 9
    s = head(w, h) + frame(w, h, "SIGNAL RADAR / PRODUCTION EXPERIENCE", f"SWEEP {P}s  9 CONTACTS")
    cx, cy, R = 260, 258, 170
    for f in (.25, .5, .75, 1):
        s += f'<circle cx="{cx}" cy="{cy}" r="{R*f}" fill="none" stroke="{C["gr"]}" stroke-opacity=".3"/>'
    s += f'<path d="M{cx-R} {cy}H{cx+R}M{cx} {cy-R}V{cy+R}" stroke="{C["gr"]}" stroke-opacity=".25"/>'
    for a in range(0, 360, 15):
        r2, ra = R + (12 if a % 90 == 0 else 6), math.radians(a)
        s += f'<line x1="{cx+R*math.cos(ra):.1f}" y1="{cy+R*math.sin(ra):.1f}" x2="{cx+r2*math.cos(ra):.1f}" y2="{cy+r2*math.sin(ra):.1f}" stroke="{C["gr"]}" stroke-opacity=".6"/>'
    a40 = math.radians(40)
    s += (f'<g transform="translate({cx} {cy})"><g><path d="M0 0L{R} 0A{R} {R} 0 0 0 {R*math.cos(a40):.1f} {-R*math.sin(a40):.1f}Z" fill="url(#wedge)"/>'
          f'<line x1="0" y1="0" x2="{R}" y2="0" stroke="{C["gr"]}" stroke-width="2" filter="url(#glow)"/>'
          f'<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="{P}s" repeatCount="indefinite"/></g></g>')
    rx, ry, bw = 560, 90, 390
    for i, (lab, v, disp) in enumerate(CAPABILITIES):
        a = 20 + i * 40
        d = R * (1.0 - v * .72)
        bx, by = cx + d * math.cos(math.radians(a)), cy + d * math.sin(math.radians(a))
        t0 = a / 360 * P
        col = C["am"] if disp == "EXPLORING" else C["gr"]
        anim = f'<animate attributeName="opacity" values="1;.2;.2" keyTimes="0;.85;1" dur="{P}s" begin="{t0:.2f}s" repeatCount="indefinite"/>'
        s += (f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="4" fill="{col}" opacity=".2" filter="url(#glow)">{anim}</circle>'
              f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="4" fill="none" stroke="{col}" opacity="0"><animate attributeName="r" values="4;22" keyTimes="0;1" dur="{P}s" begin="{t0:.2f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values=".9;0;0" keyTimes="0;.2;1" dur="{P}s" begin="{t0:.2f}s" repeatCount="indefinite"/></circle>'
              f'<text x="{bx+9:.1f}" y="{by+3:.1f}" font-size="9" fill="{C["tx"]}" opacity=".2">C{i+1:02d}{anim}</text>')
        y = ry + i * 38
        s += (f'<text x="{rx}" y="{y}" font-size="11" letter-spacing="2" fill="{C["tx"]}">C{i+1:02d}  {e(lab)}</text>'
              f'<text x="{rx+bw}" y="{y}" font-size="11" text-anchor="end" fill="{col}">{disp}</text>'
              f'<rect x="{rx}" y="{y+8}" width="{bw}" height="6" fill="{col}" fill-opacity=".1"/>'
              f'<rect x="{rx}" y="{y+8}" height="6" fill="{col}" filter="url(#glow)"><animate attributeName="width" values="0;{bw*v:.0f};{bw*(v-.02):.0f};{bw*v:.0f}" keyTimes="0;.25;.6;1" dur="{5+i*.6:.1f}s" repeatCount="indefinite"/></rect>')
    s += f'<text x="{rx}" y="{h-16}" font-size="9" fill="{C["dim"]}">metric: years in production, from the experience timeline (05/2022 to now). closer to core = longer.</text>'
    save("radar.svg", s)

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

# ───────────────────────── 5. CAREER TELEMETRY ─────────────────────────
def telemetry():
    w, h = 1000, 330
    s = head(w, h) + frame(w, h, "CAREER TELEMETRY / 05.2022 TO NOW", "4Y 5M  3 ROLES")
    gx, gy, gw, gh = 30, 56, 610, 240
    M = 53
    sx = gw / M
    s += f'<defs><clipPath id="lc"><rect x="666" y="{gy}" width="310" height="{gh}"/></clipPath></defs>'
    s += f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" fill="none" stroke="{C["cy"]}" stroke-opacity=".3"/>'
    for m, lab in [(0, "2022"), (8, "2023"), (20, "2024"), (32, "2025"), (44, "2026")]:
        x = gx + m * sx
        s += f'<line x1="{x:.0f}" y1="{gy}" x2="{x:.0f}" y2="{gy+160}" stroke="{C["cy"]}" stroke-opacity=".25" stroke-dasharray="2 4"/><text x="{x+4:.0f}" y="{gy+14}" font-size="9" fill="{C["dim"]}">{lab}</text>'
    roles = [("UPTEK", "Frontend Developer", 0, 14, C["cy"]), ("NODE AGENCY", "Senior React.js / Next.js", 14, 29, C["mg"]), ("MARKLOOPS", "Senior Shopify / React.js", 29, 53, C["gr"])]
    cyc = 10
    for i, (n, r, a, b, col) in enumerate(roles):
        y = gy + 40 + i * 38
        x, wd, k = gx + a * sx, (b - a) * sx, (.6 + i * .9) / cyc
        s += f'<text x="{x:.0f}" y="{y}" font-size="10" fill="{col}">{e(n)} <tspan fill="{C["dim"]}">/ {e(r)}</tspan></text>'
        s += (f'<rect x="{x:.0f}" y="{y+6}" height="14" width="0" fill="{col}" fill-opacity=".85" filter="url(#glow)"><animate attributeName="width" values="0;0;{wd:.0f};{wd:.0f};0" keyTimes="0;{k:.3f};{k+.1:.3f};.96;1" dur="{cyc}s" repeatCount="indefinite"/></rect>')
        if i == 2:
            s += f'<circle cx="{x+wd-4:.0f}" cy="{y+13}" r="4" fill="{C["bg"]}" stroke="{C["gr"]}" stroke-width="2"><animate attributeName="r" values="3;8;3" dur="1.6s" repeatCount="indefinite"/></circle>'
    s += f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+160}" stroke="{C["am"]}" stroke-width="2"><animate attributeName="x1" values="{gx};{gx+gw}" dur="9s" repeatCount="indefinite"/><animate attributeName="x2" values="{gx};{gx+gw}" dur="9s" repeatCount="indefinite"/></line>'
    for i, (big, lab, col) in enumerate([("100+", "PROJECTS DELIVERED", C["cy"]), ("20+", "SHOPIFY / WP BUILDS", C["gr"]), ("90+", "LIGHTHOUSE (FROM 60s)", C["mg"])]):
        x = gx + i * 210
        s += (f'<rect x="{x}" y="{gy+176}" width="190" height="56" fill="{col}" fill-opacity=".06" stroke="{col}" stroke-opacity=".5"/>'
              f'<text x="{x+14}" y="{gy+212}" font-size="30" font-weight="700" fill="{col}" filter="url(#glow)">{big}</text>'
              f'<text x="{x+14}" y="{gy+226}" font-size="8.5" letter-spacing="1.5" fill="{C["dim"]}">{lab}</text>')
    logs = [("OK  ", "22-05 joined uptek / frontend", C["gr"]), ("INFO", "22-05 react.js + shopify liquid", C["cy"]), ("OK  ", "23-07 node agency / senior role", C["gr"]),
            ("INFO", "23-07 10+ client projects shipped", C["cy"]), ("OK  ", "23-07 lighthouse 60s -> 90+", C["gr"]), ("INFO", "23-07 mentored 2 junior devs", C["cy"]),
            ("OK  ", "24-10 markloops / shopify plus", C["gr"]), ("INFO", "24-10 checkout + metafields", C["cy"]), ("INFO", "24-10 react internal tooling", C["cy"]),
            ("OK  ", "now   100+ projects delivered", C["gr"]), ("NOTE", "now   open for new engagements", C["am"])]
    lh = 20
    s += '<g clip-path="url(#lc)"><g>'
    for rep in range(2):
        for i, (lv, msg, col) in enumerate(logs):
            y = gy + 16 + (rep * len(logs) + i) * lh
            s += f'<text x="666" y="{y}" font-size="10.5" xml:space="preserve"><tspan fill="{col}">{lv.replace(" ", SP)}</tspan><tspan fill="{C["tx"]}" fill-opacity=".85"> {e(msg).replace(" ", SP)}</tspan></text>'
    s += f'<animateTransform attributeName="transform" type="translate" from="0 0" to="0 {-lh*len(logs)}" dur="{len(logs)*1.5}s" repeatCount="indefinite"/></g></g>'
    s += f'<text x="666" y="{gy-8}" font-size="10" letter-spacing="3" fill="{C["dim"]}">EVENT STREAM</text>'
    save("career.svg", s)

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

# ───────────────────────── 7. TERMINAL ─────────────────────────
def terminal():
    w, h, cyc = 1000, 470, 28
    s = head(w, h) + f'<rect x="30" y="20" width="940" height="430" fill="#030a12" stroke="{C["cy"]}" stroke-opacity=".5"/><rect x="30" y="20" width="940" height="30" fill="{C["cy"]}" fill-opacity=".1"/>'
    for i, col in enumerate([C["mg"], C["am"], C["gr"]]):
        s += f'<rect x="{46+i*18}" y="31" width="9" height="9" fill="{col}"/>'
    s += f'<text x="500" y="40" font-size="11" letter-spacing="3" text-anchor="middle" fill="{C["dim"]}">haseeb@nexus: ~/console</text>'
    t, y, defs = 1.0, 84, ""
    for i, row in enumerate(TERMINAL):
        if row[0] == 'c':
            dur = len(row[1]) * .06
            a, b = t / cyc, (t + dur) / cyc
            wmax = 60 + len(row[1]) * 9
            defs += (f'<clipPath id="k{i}"><rect x="60" y="{y-16}" height="24" width="0"><animate attributeName="width" values="0;0;{wmax};{wmax};0" keyTimes="0;{a:.4f};{b:.4f};.97;1" dur="{cyc}s" repeatCount="indefinite"/></rect></clipPath>')
            s += f'<text x="48" y="{y}" font-size="14" fill="{C["gr"]}">&gt;</text><text x="66" y="{y}" font-size="14" fill="{C["tx"]}" clip-path="url(#k{i})">{e(row[1])}</text>'
            t += dur + .5
            y += 26
        else:
            s += (f'<g opacity="0">{seq(t, cyc)}<text x="66" y="{y}" font-size="13" xml:space="preserve"><tspan fill="{C["dim"]}">{e(row[1]).ljust(14).replace(" ", SP)}</tspan><tspan fill="{C["cy"]}">{e(row[2])}</tspan></text></g>')
            t += .35
            y += 22
    s += f'<rect x="66" y="{y-14}" width="9" height="17" fill="{C["gr"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>'
    s = s.replace("</defs>", defs + "</defs>", 1)
    save("terminal.svg", s)

if __name__ == "__main__":
    for fn in (hero, skills, radar, architecture, telemetry, work, terminal):
        fn()
    print("compiled:", sorted(os.listdir(OUT)))
