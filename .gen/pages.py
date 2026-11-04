import sys,re; sys.path.insert(0,'/workspace/gen')
from build import *
PH=lambda t:f'<span class="placeholder">[PLACEHOLDER: {t}]</span>'
FAQ_HOME=[
("Is Murido therapy?","No. Murido is a grief reflection, remembrance, and self-help tool. It does not diagnose, treat, or replace a licensed therapist or grief counselor. Many people use it alongside counseling, as a place to process what comes up between sessions."),
("What does Murido cost?","Murido is free to download. Murido Pro, which unlocks the companions, personalized prompts, reflection sessions, letter writing, and memory features, is $59.99 per year through your Apple Account. You can manage or cancel it any time in your Apple Account settings."),
("Who can see what I write?","By default, only you. Your Memory Board is stored on your device. If you invite someone into a shared memory book, they see the entries in that book and nothing else you have written."),
("Can my family add their own memories?","Yes. Invite them into a shared memory book and they can add their own stories, so the person you lost is remembered the way everyone actually knew them."),
("Will it try to make me move on?","Never. Murido is built on the idea that love continues after loss. The companions will not rush you toward closure, hand you platitudes, or tell you how long grief should take."),
("What if I'm in crisis?","Murido is not a crisis service. If you are in crisis, call or text <strong>988</strong> (US Suicide &amp; Crisis Lifeline), text HOME to 741741, or call 911 if you are in immediate danger."),
]
tick='<span class="yes" aria-label="Yes">&#10003;</span>'; no='<span class="no" aria-label="No">&ndash;</span>'.replace('&ndash;','&times;')
def part(t): return f'<span class="part">{t}</span>'
rows=[("Built only for grief and remembrance",tick,no,part('Sometimes'),tick),
("Never rushes you to move on",tick,no,tick,tick),
("Available at 3am",tick,tick,tick,no),
("Remembers who you lost",tick,no,part('You do'),tick),
("Guided memory prompts",tick,no,part('DIY'),part('Sometimes')),
("Letters for unfinished conversations",tick,no,part('DIY'),part('Sometimes')),
("Shared memory book with family",tick,no,no,no),
("Licensed clinical care",no,no,no,tick)]
table='<div class="compare-wrap reveal"><table class="compare"><caption class="small" style="padding:12px;text-align:left">How Murido compares</caption><thead><tr><th scope="col"></th><th scope="col" class="us">Murido</th><th scope="col">General AI chat</th><th scope="col">A journal</th><th scope="col">Grief counselor</th></tr></thead><tbody>'+''.join(f'<tr><th scope="row" style="font-weight:500;text-align:left">{r[0]}</th><td class="us">{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>' for r in rows)+'</tbody></table></div>'
tabs_data=[
("companions","Four companions","Different kinds of presence for different days.",'<div class="shot"><img src="assets/screen-1.jpg" alt="Murido app home screen" width="250" loading="lazy"></div>','Some days you want to talk it out. Some days you want quiet company. Choose the companion that fits how you grieve today.'),
("memory","Memory Board","Their voice, their stories, kept on your device.",'<div class="shot"><img src="assets/screen-2.jpg" alt="Murido Memory Board screen" width="250" loading="lazy"></div>','Guided prompts help you hold on to the details you are afraid of losing. Everything stays private on your phone.'),
("books","Shared memory books","Invite family to remember together.",'<div class="mock"><h4>Memory book: Dad</h4><div class="row">Mom added: "The way he hummed while making pancakes on Sundays."</div><div class="row">Sam added: "He taught me to drive in the church parking lot."</div><div class="row me">You: "He called every Thursday at 7. I still look at my phone."</div></div>','Invite the people who loved them too. Everyone adds their own stories, so no one\'s memories get lost.'),
("patterns","Reflection and letters","For the harder parts, and the things left unsaid.",'<div class="shot"><img src="assets/screen-3.jpg" alt="Murido patterns and reflection screen" width="250" loading="lazy"></div>','Reflection sessions for guilt, anger, anniversaries, and firsts. Letter writing for "I miss you," "I\'m sorry," and "I hope you knew."'),
]
tabs='<div class="tabs"><div class="tablist reveal" role="tablist" aria-label="Murido features">'+''.join(f'<button class="tab" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}"><strong>{t}</strong><span>{s}</span></button>' for i,(k,t,s,_,_) in enumerate(tabs_data))+'</div><div class="panels reveal">'+''.join(f'<div class="panel{" active" if i==0 else ""}" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}">{m}<p>{p}</p></div>' for i,(k,_,_,m,p) in enumerate(tabs_data))+'</div></div>'
REVS=[("A genuine source of comfort","Sep 10","HopeMarlowe15","Murido has been an incredibly meaningful source of comfort while I've been navigating grief. It gives me a gentle, private space to express feelings that can be difficult to put into words, while helping me preserve precious memories of the person I lost. The thoughtful prompts, reflections, and supportive conversations make me feel heard and less alone, especially on the hardest days when grief arrives unexpectedly. This app was clearly created with so much care and compassion, and I'm truly grateful to have found it. &#10084;&#65039;"),
("Helps me feel close to him","Oct 15","eleanorh10","Murido has been really comforting since my brother passed. I use it to save little memories about him, write down things I don't want to forget, and just feel close to him in a way. It's become a really special place for me to keep his memory alive."),
("I miss my mom every day","Oct 15","Zender123","I lost my mom last year and honestly there's not a day that goes by where I don't think about her. I started using Murido to keep all the little memories I have of her in one place. Things she used to say, funny moments we shared, and all the small stuff I never want to forget. It's been really comforting to have somewhere I can go when I miss her and feel a little closer to her again")]
REV=[f'<figure class="review lift"><div class="stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><h3>{t}</h3><blockquote><p>{q}</p></blockquote><figcaption class="who">{h} &middot; {d} &middot; App Store review</figcaption></figure>' for t,d,h,q in REVS]
home=f'''<section class="hero-x"><div class="container"><div class="reveal"><span class="pill"><span class="dot"></span>Grief and memory companion for iPhone</span></div>
<h1 class="reveal" style="--d:80ms">Keep loving them after loss.</h1>
<p class="lede reveal" style="--d:160ms">You do not have to move on to keep going. Murido is a quiet, private place to carry grief, preserve their story, and say what still needs saying, at 3am, on the hard anniversaries, or on an ordinary Tuesday when it catches you off guard.</p>
<div class="cta-row reveal" style="--d:240ms"><a class="btn btn-dark" href="checkin.html">Take the Free Grief Check-In <span class="arrow" aria-hidden="true">&rarr;</span></a><a class="btn btn-quiet" href="#how-it-works">See how it works</a></div>
<ul class="chips" data-stagger><li>No timelines</li><li>Private by default</li><li>Made for grief, nothing else</li></ul></div></section>
<section class="band band-surface"><div class="container"><div class="section-head reveal"><span class="eyebrow">See inside</span><h2>Somewhere to put what you are carrying.</h2><p>Four ways Murido meets you, depending on the day.</p></div>{tabs}</div></section>
<section class="band" id="how-it-works"><div class="container"><div class="section-head reveal"><span class="eyebrow">How it works</span><h2>A few minutes a day, at your own pace.</h2></div>
<div class="step-grid" data-stagger><div class="step lift"><div class="num">01</div><h3>Tell Murido who you lost</h3><p>Share a name and a little about them. Murido uses it to make every prompt and conversation about your person, not grief in general.</p></div>
<div class="step lift"><div class="num">02</div><h3>Remember, reflect, write</h3><p>Answer a daily memory prompt, work through a hard feeling, or write the letter you never got to send.</p></div>
<div class="step lift"><div class="num">03</div><h3>Talk whenever it hits</h3><p>When grief shows up out of nowhere, a companion who already knows your story is there, without rushing you anywhere.</p></div></div></div></section>
<section class="band band-surface"><div class="container"><div class="section-head reveal"><span class="eyebrow">Why Murido</span><h2>Made for remembering, not for moving on.</h2><p>General chatbots try to fix things. Journals cannot answer back. Counseling is invaluable but not there at 3am. Murido fills the space in between.</p></div>{table}<p class="small reveal" style="margin-top:16px">We always encourage working with a grief counselor or therapist if you can. Murido is here between sessions, and for everyone who cannot get one.</p></div></section>
<section class="band"><div class="container"><div class="section-head reveal"><span class="eyebrow">From people using Murido</span><h2>In their words.</h2><p>Real reviews from the App Store.</p></div>
<div class="grid-3" data-stagger style="margin-top:32px">'''+''.join(REV)+f'''</div></div></section>
<section class="band"><div class="container"><div class="privacy-band reveal"><div class="section-head"><span class="eyebrow">Privacy</span><h2>What you write about them stays yours.</h2><p>Grief is about as personal as it gets. Murido was built around that from the start.</p></div>
<div class="grid-3" data-stagger style="margin-top:28px"><div><h3>On-device Memory Board</h3><p>Everything on your Memory Board is stored on your phone, not uploaded to our servers.</p></div><div><h3>Shared only by invitation</h3><p>Memory books are shared only with the people you invite, and only that book.</p></div><div><h3>Never sold</h3><p>We do not sell your data or share your conversations with advertisers. <a href="privacy.html" style="color:#fff">Read the privacy policy</a>.</p></div></div></div></div></section>
<section class="band"><div class="narrow"><div class="section-head reveal"><span class="eyebrow">Questions</span><h2>Frequently asked questions</h2></div>{faq(FAQ_HOME)}</div></section>'''+final()
page('index.html','Murido | Grief & Memory Companion for iPhone','Murido is an AI remembrance companion for grief: four gentle companions, a private on-device Memory Board, letters, and shared memory books for families.',home)

about=f'''<section class="hero-x"><div class="container"><span class="eyebrow reveal">About Murido</span><h1 class="reveal" style="--d:80ms">Built for grief by people who know it.</h1><p class="lede reveal" style="--d:160ms">Murido exists for the long stretch after the funeral, when everyone else has gone home and the love you have for someone still needs somewhere to go.</p></div></section>
<!-- PLACEHOLDER founder story, fill and uncomment:
<section class="band band-surface"><div class="narrow reveal"><h2>Why we started</h2><p>{PH("Founder story: who you lost or what you saw, why existing tools fell short, and why you built Murido. 2 to 3 short paragraphs in your own words.")}</p></div></section>
-->
<section class="band"><div class="narrow"><div class="reveal"><h2>How we build</h2></div><ul class="principles" data-stagger>
<li>Focused only on grief and remembrance, not generic wellness.</li><li>Grounded in continuing bonds: the idea that healthy grief keeps a connection rather than cutting it.</li><li>We never rush anyone toward closure or tell them how long grief should take.</li><li>We do not use platitudes. "Everything happens for a reason" will never come out of Murido.</li><li>Private by design, with the Memory Board kept on your device.</li><li>Honest about limits: Murido is not therapy or a crisis service, and it points people to real help when they need it.</li><li>Shaped by ongoing conversations with grieving people who use the app.</li></ul></div></section>
<!-- PLACEHOLDER team, fill and uncomment:
<section class="band band-surface"><div class="container"><div class="section-head reveal"><span class="eyebrow">The team</span><h2>The people behind Murido.</h2></div><div class="grid-3 team" data-stagger style="margin-top:32px">'''+''.join(f'<div class="card lift"><div class="avatar" aria-hidden="true"></div><h3>{PH("Name")}</h3><p>{PH("Role, background, and why grief matters to them. Add real bios only.")}</p></div>' for _ in range(3))+f'''</div></div></section>
-->
<section class="band"><div class="narrow reveal" style="text-align:center"><span class="eyebrow">Our mission</span><h2>So that no one's life becomes smaller with time.</h2><p class="lede">We want every grieving person to have a place to remember, reflect, and keep talking to the people they love, and to never feel like they have to carry it alone.</p></div></section>'''+final()
page('about.html','About Murido | Built for grief','Why Murido exists, how we build it, and the people behind it.',about)

approach=f'''<section class="hero-x"><div class="container"><span class="eyebrow reveal">Our approach</span><h1 class="reveal" style="--d:80ms">Grief is love with nowhere to go. We give it somewhere.</h1><p class="lede reveal" style="--d:160ms">Murido is built on ideas from grief research and on what grieving people tell us actually helps.</p></div></section>
<section class="band band-surface"><div class="container"><div class="grid-3" data-stagger>
<div class="card lift"><h3>Continuing bonds</h3><p>Older models of grief treated "letting go" as the goal. Many grief researchers now describe healthy grieving as finding a new, ongoing relationship with the person who died. Murido is designed around keeping that bond.</p></div>
<div class="card lift"><h3>Moving between both sides</h3><p>The dual process model describes grief as a back and forth between facing the loss and attending to daily life. Murido is there for both: a memory prompt one day, a reason to get through Tuesday the next.</p></div>
<div class="card lift"><h3>Telling the story</h3><p>Putting a loss into words, through writing and conversation, helps many people make sense of it. Prompts, letters, and memory books give those words a home.</p></div></div></div></section>
<section class="band"><div class="narrow"><div class="reveal"><h2>What Murido is</h2><ul><li>A remembrance companion with four AI companions who know your person and your story.</li><li>A private, on-device Memory Board for the details you never want to lose.</li><li>Invite-based shared memory books for families and friends.</li><li>Guided reflection sessions and letter writing for the harder parts of grief.</li></ul>
<h2>What Murido is not</h2><ul><li>It is not a licensed therapist and does not diagnose or treat anything.</li><li>It is not a crisis service.</li><li>It is not a way to simulate or impersonate the person who died. The companions talk with you about them, not as them.</li></ul></div>
<!-- PLACEHOLDER results, fill and uncomment:
<div class="reveal"><h2>Results and research</h2><p>{PH("Add only real, verified outcome data or user research here, with sources. Leave this section out until you have it.")}</p></div>
-->
<div class="note reveal"><strong>Safety.</strong> If you are thinking about harming yourself, call or text <strong>988</strong> (US Suicide &amp; Crisis Lifeline), or text HOME to 741741. Grief that feels unbearable deserves real, human support.</div></div></section>'''+final()
page('approach.html','Our Approach | Murido','The grief research behind Murido: continuing bonds, the dual process model, and storytelling, plus what Murido is and is not.',approach)

comp=f'''<section class="hero-x"><div class="container"><span class="eyebrow reveal">Companions and memory</span><h1 class="reveal" style="--d:80ms">Four companions. One story worth keeping.</h1><p class="lede reveal" style="--d:160ms">Grief changes by the hour. Murido gives you different kinds of presence for different moments, plus places to keep what you remember.</p></div></section>
<section class="band band-surface"><div class="container"><!-- PLACEHOLDER named companion cards, fill and uncomment:
<div class="grid-2" data-stagger>'''+''.join(f'<div class="card lift"><span class="tag">Companion {i}</span><h3>{PH("Companion name")}</h3><p>{PH("What this companion is like and when people choose it, e.g. a calm listener, a gentle question-asker, a memory-keeper, a steady presence for hard days")}</p></div>' for i in range(1,5))+'</div>\n-->'+'<div class="section-head reveal"><span class="eyebrow">The companions</span><h2>Four different kinds of presence.</h2><p>Some days you want to talk it out. Some days you want gentle questions, quiet company, or help remembering. Choose the companion that fits how you are grieving today, and switch any time.</p></div>'+f'''<p class="small reveal" style="margin-top:16px;text-align:center">Every companion remembers who you lost and what they meant to you, never rushes you, and never offers platitudes.</p></div></section>
<section class="band"><div class="container"><div class="grid-2" data-stagger><div class="card lift"><h3>The Memory Board</h3><p>Guided prompts for their voice, sayings, routines, favorite things, advice, and the moments you are afraid of forgetting. Written at your pace and stored on your device.</p></div><div class="card lift"><h3>Shared memory books</h3><p>Invite family and friends with a link or code. Everyone adds their own stories to the same book, so the person you lost is remembered the way everyone knew them. Only the people you invite can see it.</p></div><div class="card lift"><h3>Reflection sessions</h3><p>For guilt, anger, regret, birthdays, anniversaries, firsts without them, family tension, and the days grief comes out of nowhere.</p></div><div class="card lift"><h3>Letters</h3><p>For the things that still need saying: thank you, I miss you, I'm sorry, I wish you were here, I need your advice, I hope you knew.</p></div></div></div></section>'''+final()
page('companions.html','Companions & Memory Books | Murido','Meet the four Murido companions, the private Memory Board, shared memory books, reflection sessions, and letters.',comp)

get=f'''<section class="hero-x"><div class="container"><span class="eyebrow reveal">Get Murido</span><h1 class="reveal" style="--d:80ms">Start remembering today.</h1><p class="lede reveal" style="--d:160ms">Murido: Grief &amp; Memory is available for iPhone and iPad on the App Store.</p><div class="cta-row reveal" style="--d:240ms"><a class="btn btn-dark" href="{APP}">Download on the App Store <span class="arrow" aria-hidden="true">&rarr;</span></a></div>
<div class="grid-3" data-stagger style="max-width:820px;margin:0 auto">'''+''.join(f'<div class="shot lift" style="margin:0 auto;width:220px"><img src="assets/screen-{i}.jpg" alt="Murido screenshot {i}" loading="lazy" width="220"></div>' for i in (1,2,3))+f'''</div></div></section>
<section class="band band-surface"><div class="narrow reveal"><h2>Pricing</h2><p>Murido is free to download. Murido Pro is required for personalized prompts, AI conversations, grief reflection sessions, letter writing, and memory features. It costs <strong>$59.99 per year</strong>, charged to your Apple Account, and renews automatically unless cancelled at least 24 hours before the period ends. Manage or cancel any time in your Apple Account settings.</p></div></section>'''
page('get.html','Get Murido for iPhone | Grief & Memory','Download Murido: Grief & Memory on the App Store. Pricing and what is included.',get)

# legacy pages: swap nav/footer, wrap
for f in ['privacy.html','terms.html','support.html','join.html','r.html']:
    p=f'{R}/{f}'; s=open(p).read()
    if 'site-header' in s:
        s=re.sub(r'<a class="skip".*?</header>',header('',f),s,count=1,flags=re.S); s=re.sub(r'<footer class="site-footer">.*?</script>',footer(''),s,count=1,flags=re.S)
        if THEME_JS not in s: s=s.replace('<meta charset="utf-8">','<meta charset="utf-8">'+THEME_JS,1)
        open(p,'w').write(s); continue
    s=re.sub(r'<nav>.*?</nav>',header('',f)+'<main id="main" class="page">',s,count=1,flags=re.S)
    s=re.sub(r'<footer>.*?</footer>','',s,flags=re.S)
    s=s.replace('<body><div class="wrap">','<body>').replace('<div class="wrap">','')
    s=re.sub(r'</div>\s*</body>','</body>',s)
    s=s.replace('</body>','</main>'+footer('')+'</body>',1) if '</main>' not in s else s
    # wrap main content in .wrap
    s=s.replace('<main id="main" class="page">','<main id="main" class="page"><div class="wrap">',1).replace('</main>','</div></main>',1)
    s=s.replace('<link rel="stylesheet" href="style.css">','<link rel="stylesheet" href="style.css"><link rel="icon" href="assets/icon.png">',1)
    open(p,'w').write(s)
posts=build_blog(parse()); print(len(posts),'posts')

# ---------- check-in ----------
CHECKIN=r'''<section class="page checkin"><div class="narrow">
<div class="ci-intro reveal" id="ci-intro"><span class="eyebrow">Free grief check-in</span><h1>How is grief showing up for you right now?</h1><p class="lede">Seven gentle questions, about two minutes. There are no right answers. Your answers stay in this browser tab and are never sent anywhere.</p><button class="btn btn-dark" id="ci-start" type="button">Begin the check-in <span class="arrow" aria-hidden="true">&rarr;</span></button><p class="small" style="margin-top:16px">This is a reflection tool, not a clinical assessment or diagnosis.</p></div>
<div class="ci-quiz" id="ci-quiz" hidden><div class="ci-progress" role="progressbar" aria-valuemin="0" aria-valuemax="7" aria-valuenow="0" aria-label="Check-in progress"><span id="ci-bar"></span></div><p class="small" id="ci-count" aria-live="polite"></p><div id="ci-stage" class="ci-stage"></div><button class="ci-back" id="ci-back" type="button">&larr; Back</button></div>
<div class="ci-result" id="ci-result" hidden tabindex="-1"></div>
</div></section>
<script>
(function(){
var Q=[
{q:"Who are you grieving?",o:["A parent","A partner or spouse","A child or pregnancy","A sibling, friend, or other family","A pet","More than one person"],k:"who"},
{q:"How long ago was the loss?",o:["Less than a month","One to six months","Six months to a year","One to three years","More than three years"],k:"when"},
{q:"Over the past two weeks, how often has grief felt overwhelming?",o:["Rarely","Some days","Most days","Nearly every day"],s:[0,1,2,3]},
{q:"How are you sleeping?",o:["About as usual","A little off","Often poorly","Hardly at all"],s:[0,1,2,3]},
{q:"Do you have someone you can talk to about them?",o:["Yes, and I do","Yes, but I hold back","Not really","No one right now"],s:[0,1,2,3]},
{q:"Which of these feels heaviest lately?",o:["Missing them","Guilt or regret","Anger","Fear of forgetting them","Things left unsaid","Feeling numb"],k:"heavy"},
{q:"How much is grief getting in the way of daily life, like work, meals, or caring for yourself?",o:["Not much","A little","Quite a lot","Almost completely"],s:[0,1,2,3]}
];
var A=[],i=0,stage=document.getElementById('ci-stage'),bar=document.getElementById('ci-bar'),cnt=document.getElementById('ci-count'),pb=document.querySelector('.ci-progress');
function show(dir){var x=Q[i];cnt.textContent='Question '+(i+1)+' of '+Q.length;bar.style.width=(i/Q.length*100)+'%';pb.setAttribute('aria-valuenow',i);
var el=document.createElement('fieldset');el.className='ci-q enter'+(dir<0?' back':'');el.innerHTML='<legend><h2>'+x.q+'</h2></legend>'+x.o.map(function(o,j){return '<button type="button" class="ci-opt'+(A[i]===j?' sel':'')+'" data-j="'+j+'">'+o+'</button>';}).join('');
stage.innerHTML='';stage.appendChild(el);requestAnimationFrame(function(){el.classList.remove('enter');});
el.querySelectorAll('.ci-opt').forEach(function(b){b.addEventListener('click',function(){A[i]=+b.dataset.j;b.classList.add('sel');setTimeout(function(){if(i<Q.length-1){i++;show(1);}else done();},220);});});
el.querySelector('.ci-opt').focus({preventScroll:true});document.getElementById('ci-back').style.visibility=i?'visible':'hidden';}
var heavyMsg=["Missing them is love that still has somewhere to go. Murido's daily memory prompts give that longing a place to land.","Guilt is one of the most common parts of grief, and it usually grows out of love. Writing a letter that says what you wish you had said can loosen its grip.","Anger is a normal, often unspoken part of grief. It deserves a safe place to be said out loud, without anyone flinching.","The fear of forgetting is real, and so are the ways to hold on. Capturing their sayings, habits, and stories now keeps the details close.","Unfinished conversations can stay heavy for a long time. Letter writing is a gentle way to say the thing that never got said.","Numbness is grief's way of pacing itself. It does not mean you loved them less. Small, low-pressure moments of remembering can help feeling return gently."];
function done(){bar.style.width='100%';var s=0;Q.forEach(function(x,j){if(x.s)s+=x.s[A[j]];});
var lvl=s<=3?0:s<=7?1:2;
var head=["You are carrying this with real steadiness.","Grief is asking a lot of you right now.","Grief is weighing very heavily on you."][lvl];
var body=["From your answers, grief is present but not overwhelming most days. That is worth noticing. Steady stretches are a good time to gather memories and keep their story close, so the hard days have something to hold.","From your answers, grief is showing up often and touching sleep, connection, or daily life. That is a very human response to loss, and it is a sign to be gentle with yourself and let a little more support in.","From your answers, grief is affecting nearly every part of your days. You deserve real support with this. Consider reaching out to a doctor, grief counselor, or support group, and let one trusted person know how you are really doing."][lvl];
var r=document.getElementById('ci-result');document.getElementById('ci-quiz').hidden=true;r.hidden=false;
r.innerHTML='<div class="ci-card reveal in"><span class="eyebrow">Your reflection</span><h1>'+head+'</h1><p class="lede">'+body+'</p><h2>What feels heaviest</h2><p>'+heavyMsg[A[5]]+'</p>'+(lvl==2?'<div class="crisis" role="note"><strong>If you are thinking about harming yourself,</strong> please call or text <strong>988</strong> now (US Suicide &amp; Crisis Lifeline), or call 911 if you are in immediate danger.</div>':'')+'<h2>A place to keep going</h2><p>Murido is a grief and memory companion for iPhone: four gentle AI companions, a private on-device Memory Board, letters, and shared memory books for family.</p><div class="cta-row" style="justify-content:flex-start"><a class="btn btn-dark" href="'+'''+'"'+APP+'"'+'''+'">Download Murido for iPhone <span class="arrow" aria-hidden="true">&rarr;</span></a><button class="btn btn-quiet" type="button" onclick="location.reload()">Start over</button></div><p class="small">This check-in is a reflection, not a diagnosis or clinical assessment, and it is not a substitute for professional care. Nothing you answered was saved or sent.</p></div>';r.focus();window.scrollTo({top:0,behavior:'smooth'});}
document.getElementById('ci-start').addEventListener('click',function(){document.getElementById('ci-intro').hidden=true;document.getElementById('ci-quiz').hidden=false;show(1);});
document.getElementById('ci-back').addEventListener('click',function(){if(i>0){i--;show(-1);}});
})();
</script>'''
page('checkin.html','Free Grief Check-In | Murido','A free, private, two-minute grief check-in with a gentle reflection at the end. Not a diagnosis. Nothing is saved or sent.',CHECKIN)
