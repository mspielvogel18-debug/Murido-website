# Invite links on muridoapp.com

Shared links are `https://muridoapp.com/join/<code>`. This repo serves them.

- `join.html` is the join page. `/join/*` rewrites to it (200, no redirect).
- `/.well-known/apple-app-site-association` is the existing file. It is served as `application/json` with no redirect. `appID` is `V29V78883D.com.murido.app`. Paths include `/join.html`, `/join.html*`, and `/join/*`.
- `netlify/functions/` holds the three handlers from the app repo's `hosting/netlify/functions/` (`feature/gamified-journey-native`). Shared code lives in `netlify/lib/` so Netlify does not try to publish `http.js` and `fingerprint.js` as their own functions. The handler logic is unchanged.

The app calls these on the same host:

- `POST /api/preview-invite`
- `POST /api/record-invite`
- `POST /api/match-invite`

The page copies `murido-invite:<code>` plus `https://muridoapp.com/join/<code>` to the clipboard (plain text and a URL), then the download button records a one-hour device fingerprint. Names and emails are not logged.

## FIREBASE_SERVICE_ACCOUNT

Set this in the Netlify UI. Do not commit the JSON. Do not paste the Render variable `FIREBASE_SERVICE_ACCOUNT_B64`. That one is base64. This one is the JSON object itself. `JSON.parse` reads it.

The value has to be a Firebase service account that can read `invites` and write `pendingInvites`. The Firebase Admin SDK key for project `murido-8378a` can do both.

1. Open [Firebase console](https://console.firebase.google.com/) and select project `murido-8378a`.
2. Click the gear next to Project overview, then Project settings.
3. Open the Service accounts tab.
4. Click Generate new private key, then Generate key. A JSON file downloads (name like `murido-8378a-firebase-adminsdk-....json`).
5. In Netlify, open the muridoapp.com site, then Site configuration, Environment variables, Add a variable.
6. Key: `FIREBASE_SERVICE_ACCOUNT`
7. Value: paste the file contents unchanged. It starts with `{` and ends with `}`. Do not wrap it in quotes and do not put a file path. A single line or the original pretty-printed file both work. Keep the `\n` sequences inside `private_key`.
8. Mark it secret if Netlify offers that. Scopes: Production, plus Deploy Previews if preview URLs should call Firebase too.
9. Save, then Deploys, Trigger deploy, Deploy site. The variable applies on the next deploy.

Until that variable is set, the three functions respond with HTTP 500 and `{ "ok": false }`. The join page still renders, and the clipboard copy still works.

## Check

```
curl -sI https://muridoapp.com/.well-known/apple-app-site-association | head
curl -s https://muridoapp.com/.well-known/apple-app-site-association
curl -sI https://muridoapp.com/join/K3PQ7M | head
```

The association response must be 200, `content-type: application/json`, and no redirect. `/join/K3PQ7M` must be 200 HTML, not 404.
