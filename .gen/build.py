import os,re,glob,html,datetime
R='/workspace/Murido-website'
APP='https://apps.apple.com/app/id6798652505'
CATS={'grief-basics':('Grief Basics','What grief is, how it behaves, and why it does what it does.'),
      'kinds-of-loss':('Kinds of Loss','Every loss has its own shape. Guides for specific losses and the feelings that come with them.'),
      'coping-and-healing':('Coping & Healing','Practical, gentle ways to carry grief and stay connected to the person you lost.')}
THEME_JS='<script>(function(){try{var t=localStorage.getItem("theme");if(!t)t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script><meta name="color-scheme" content="light dark">'
def head(title,desc,pre,canon):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">{THEME_JS}<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://muridoapp.com/{canon}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="https://muridoapp.com/assets/icon.png">
<link rel="icon" href="{pre}assets/icon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="{pre}style.css"></head>'''
def header(pre,cur):
    items=[('index.html','Home'),('about.html','About'),('approach.html','Our Approach'),('companions.html','Companions'),('blog/','Blog')]
    links=''.join(f'<a href="{pre}{h}"'+(' aria-current="page"' if cur==h else '')+f'>{t}</a>' for h,t in items)
    return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="inner"><a class="brand" href="{pre}index.html"><img src="{pre}assets/icon.png" alt="" width="30" height="30">murido</a><button class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button><nav id="site-nav" class="site-nav" aria-label="Main">{links}<button class="theme-toggle" type="button" aria-label="Toggle dark mode"><svg class="i-moon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="i-sun" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button><a class="btn" href="{pre}checkin.html">Take the Free Grief Check-In</a></nav></div></header>'''
CRISIS='<strong>If you are in crisis, please reach out now.</strong> Call or text <strong>988</strong> (US Suicide &amp; Crisis Lifeline) or text HOME to 741741. If you are in immediate danger, call 911. Murido is peer-style emotional support for grief. It is not therapy, medical care, or a crisis service.'
def footer(pre):
    return f'''<footer class="site-footer"><div class="container"><div class="cols"><div><a class="brand" href="{pre}index.html">murido</a><p>A gentle companion for grief and memory. Keep loving them after loss.</p><a class="btn btn-dark" href="{APP}">Download for iPhone</a></div>
<div><h4>Murido</h4><ul><li><a href="{pre}about.html">About</a></li><li><a href="{pre}approach.html">Our Approach</a></li><li><a href="{pre}companions.html">Companions</a></li><li><a href="{pre}get.html">Get the app</a></li></ul></div>
<div><h4>Resources</h4><ul><li><a href="{pre}blog/">Blog</a></li><li><a href="{pre}support.html">Support</a></li><li><a href="{pre}privacy.html">Privacy Policy</a></li><li><a href="{pre}terms.html">Terms of Use</a></li><li><a href="mailto:info@muridoapp.com">info@muridoapp.com</a></li></ul></div></div>
<p class="crisis" role="note">{CRISIS}</p><p class="copy">&copy; 2026 Bubu Technologies LLC</p></div></footer><script src="{pre}site.js" defer></script>'''
def page(path,title,desc,body,cur=None):
    pre='../'*path.count('/')
    canon=path.replace('index.html','')
    out=head(title,desc,pre,canon)+'<body>'+header(pre,cur or path)+f'<main id="main">{body}</main>'+footer(pre)+'</body></html>\n'
    os.makedirs(os.path.dirname(f'{R}/{path}') or R,exist_ok=True); open(f'{R}/{path}','w').write(out)
def faq(items):
    return '<div class="faq">'+''.join(f'<details class="reveal"><summary>{q}</summary><div class="ans"><div><p>{a}</p></div></div></details>' for q,a in items)+'</div>'
def final(h='You do not have to carry it alone.',p='Start with a gentle, free check-in. A few quiet questions about how grief is showing up for you right now.',pre=''):
    return f'<section class="final"><div class="reveal"><h2>{h}</h2><p class="lede" style="max-width:46ch;margin:0 auto 1.8em">{p}</p><a class="btn btn-dark" href="{pre}checkin.html">Take the Free Grief Check-In <span class="arrow" aria-hidden="true">&rarr;</span></a></div></section>'
# ---------- posts ----------
def parse():
    posts=[]
    for f in sorted(glob.glob('/workspace/gen/posts/*.txt')):
        for blk in open(f).read().split('====='):
            blk=blk.strip()
            if not blk: continue
            meta,_,body=blk.partition('\n---\n')
            m=dict(l.split(': ',1) for l in meta.strip().split('\n'))
            m['body']=body.strip(); posts.append(m)
    # long versions override
    for f in glob.glob('/workspace/gen/long/*.txt'):
        meta,_,body=open(f).read().strip().partition('\n---\n')
        m=dict(l.split(': ',1) for l in meta.strip().split('\n'))
        for p in posts:
            if p['slug']==m['slug']: p['body']=body.strip(); p['long']=True
    return posts
def fmt(t):
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    return re.sub(r'\[(.+?)\]\((.+?)\)',r'<a href="\2">\1</a>',t)
def md(body):
    out=[]
    for para in re.split(r'\n\s*\n',body):
        para=para.strip()
        if para.startswith('### '): out.append(f'<h3>{fmt(para[4:])}</h3>')
        elif para.startswith('## '): out.append(f'<h2>{fmt(para[3:])}</h2>')
        elif para.startswith('> '): out.append(f'<blockquote class="pull"><p>{fmt(para[2:])}</p></blockquote>')
        elif para.startswith('- '): out.append('<ul>'+''.join(f'<li>{fmt(l[2:])}</li>' for l in para.split('\n'))+'</ul>')
        elif re.match(r'\d+\. ',para): out.append('<ol>'+''.join(f'<li>{fmt(re.sub(r"^\d+\. ","",l))}</li>' for l in para.split('\n'))+'</ol>')
        else: out.append(f'<p>{fmt(para)}</p>')
    return '\n'.join(out)
def words(b): return len(re.findall(r'\w+',b))
def img(slug,pre,cls,alt=''):
    return f'<div class="{cls}"><img src="{pre}assets/blog/{slug}.webp" alt="{alt}" loading="lazy" onerror="this.remove()"></div>'
def card(p,pre):
    c=CATS[p['cat']][0]
    return f'<a class="post-card lift" href="{pre}{p["slug"]}.html">{img(p["slug"],"../"*(pre.count("../")+1),"thumb")}<div class="pc-body"><span class="tag">{c}</span><h3>{p["title"]}</h3><p class="excerpt">{p["desc"]}</p><span class="meta">{p["datef"]} &middot; {p["mins"]} min read</span></div></a>'
def build_blog(posts):
    for p in posts:
        d=datetime.date.fromisoformat(p['date']); p['datef']=d.strftime('%b %-d, %Y'); p['mins']=max(3,round(words(p['body'])/230))
    posts.sort(key=lambda p:p['date'],reverse=True)
    filt=lambda cur:'<nav class="filters" aria-label="Categories"><a href="'+('../' if cur else '')+'index.html"'+(' aria-current="page"' if not cur else '')+'>All</a>'+''.join(f'<a href="'+('' if cur else 'category/')+f'{k}.html"'+(' aria-current="page"' if cur==k else '')+f'>{v[0]}</a>' for k,v in CATS.items())+'</nav>'
    grid=lambda ps,pre:'<div class="post-grid" data-stagger>'+''.join(card(p,pre) for p in ps)+'</div>'
    page('blog/index.html','The Murido Blog | Grief, memory, and life after loss','Long-form guides on grief, remembrance, continuing bonds, and coping with loss, from the team behind Murido.',
        f'<section class="page blog-head"><div class="container"><div class="reveal"><h1>The Murido blog</h1><p class="lede">Gentle, honest guides for grief, remembrance, and the life that continues after loss.</p></div>{filt(None)}{grid(posts,"")}</div></section>'+final(pre='../'),cur='blog/')
    for k,(n,dsc) in CATS.items():
        ps=[p for p in posts if p['cat']==k]
        page(f'blog/category/{k}.html',f'{n} | The Murido Blog',dsc,
            f'<section class="page blog-head"><div class="container"><p class="breadcrumb"><a href="../index.html">Blog</a> / {n}</p><div class="reveal"><h1>{n}</h1><p class="lede">{dsc}</p></div>{filt(k)}{grid(ps,"../")}</div></section>'+final(pre='../../'),cur='blog/')
    for p in posts:
        rel=[q for q in posts if q['cat']==p['cat'] and q is not p][:3]
        cn=CATS[p['cat']][0]
        body=f"""<article class="page article"><div class="narrow"><p class="breadcrumb"><a href="index.html">Blog</a> / <a href="category/{p['cat']}.html">{cn}</a></p>
<header class="reveal"><span class="tag">{cn}</span><h1>{p['title']}</h1><div class="byline"><img src="../assets/mascot-avatar.webp" alt="" width="40" height="40"><div><strong>The Murido Team</strong><span class="meta">{p['datef']} &middot; {p['mins']} min read</span></div></div></header></div>
<div class="container">{img(p['slug'],'../','hero-img reveal',p['title'])}</div>
<div class="narrow"><div class="prose reveal">{md(p['body'])}</div>
<aside class="app-cta reveal" aria-label="Murido app"><img src="../assets/icon.png" alt=""><div><h3>A place for what you are carrying</h3><p>Murido gives you four gentle AI companions, a private on-device Memory Board, and shared memory books your family can add to.</p><a class="btn btn-dark" href="{APP}">Download for iPhone <span class="arrow" aria-hidden="true">&rarr;</span></a></div></aside>
<p class="note">This article is for general information and support. It is not medical or mental health advice. If grief has become unbearable or you are thinking about harming yourself, call or text <strong>988</strong> right now.</p></div>
<section class="band"><div class="container"><h2>Related reading</h2><div class="post-grid" data-stagger>{"".join(card(q,"") for q in rel)}</div></div></section></article>"""
        page(f'blog/{p["slug"]}.html',f'{p["title"]} | Murido',p['desc'],body,cur='blog/')
    return posts
