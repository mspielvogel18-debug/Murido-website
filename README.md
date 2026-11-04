# Murido website

Static HTML/CSS/JS for muridoapp.com. No build step; Netlify deploys on push to main.

- `index.html`: home (hero, feature tabs, how it works, comparison, testimonials, privacy, FAQ, CTA)
- `about.html`, `approach.html`, `companions.html`, `get.html`: main pages
- `blog/`: blog index, `blog/category/*.html` category pages, one HTML file per post
- `privacy.html`, `terms.html`, `support.html`: legal and support (App Store links here)
- `join.html`, `r.html`: invite and referral landing pages
- `style.css`: brand tokens and all styles; `site.js`: scroll reveal, sticky header, mobile menu, tabs
- `assets/`: app icon and App Store screenshots

Every page must keep the shared header, the footer, and the 988 crisis note. Search for `[PLACEHOLDER` to find content still to fill in.
Copy rule: no em or en dashes.
