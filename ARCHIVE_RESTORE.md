# Archive: Murido web app at /app (2026-11-20)

This branch freezes muridoapp.com `main` as of merge 6ec12257cc0b3eccf0bf50bc77b16208eac1035f
(website PR #6), right before the web app at `/app` was taken private on Nov 20, 2026.

What it holds:
- `app/`: the Expo Web export of the Murido app (commit 878da0e, `npx expo export --platform web`
  with `experiments.baseUrl: "/app"`), bundle `app/_expo/static/js/web/index-596271973b9538494725e025c2402dd8.js`.
- `_redirects`: SPA fallback (`/app`, `/app/`, `/app/*` to `/app/index.html` 200).
- `_headers`: cache rules for `/app/index.html` and `/app/_expo/static/*`.
- The header CTA on every page: `<a class="btn" href="/app/">Use Murido on desktop</a>` next to
  `<a class="btn btn-quiet" href="https://apps.apple.com/app/id6798652505">Download on iPhone</a>`.
- `WEB_APP_HANDOFF.md`: the original web app handoff notes.

## How to restore later

The plan is to restyle the web app to match the current iOS app and add payments first, so a fresh
export will usually replace `app/`. To bring back exactly what was live on Nov 20:

1. `git checkout main && git checkout -b restore-web-app`
2. `git checkout archive/web-app-2026-11-20 -- app WEB_APP_HANDOFF.md`
3. In `_redirects`, delete the `/app` 301 lines and put back:
   ```
   /app     /app/index.html  200
   /app/    /app/index.html  200
   /app/*   /app/index.html  200
   ```
4. In `_headers`, remove the `X-Robots-Tag: noindex` block for `/app` and restore the two `/app` cache blocks.
5. Put the header CTA back on every page (and in the generator's `nav()` in `/workspace/gen/build.py`).
6. Open a PR, check the Netlify deploy preview, merge.
