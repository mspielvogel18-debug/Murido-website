const admin = require('firebase-admin');
const crypto = require('crypto');
const fp = require('./fingerprint');

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Content-Type': 'application/json',
};

function firestore() {
  if (!admin.apps.length) {
    const raw = process.env.FIREBASE_SERVICE_ACCOUNT;
    if (!raw) throw new Error('FIREBASE_SERVICE_ACCOUNT is not set');
    admin.initializeApp({ credential: admin.credential.cert(JSON.parse(raw)) });
  }
  return admin.firestore();
}

function clientIp(event) {
  const headers = event.headers || {};
  return headers['x-nf-client-connection-ip']
    || headers['client-ip']
    || String(headers['x-forwarded-for'] || '').split(',')[0].trim();
}

function signalsFrom(event) {
  const body = JSON.parse(event.body || '{}');
  return {
    body,
    signals: {
      ip: clientIp(event),
      ios: body.ios,
      model: body.model,
      screenW: body.screenW,
      screenH: body.screenH,
      tz: body.tz,
      lang: body.lang,
    },
  };
}

async function publicPreview(code) {
  const snap = await firestore().doc(`invites/${code}`).get();
  if (!snap.exists) return null;
  const data = snap.data() || {};
  const expires = typeof data.expiresAt === 'string' ? Date.parse(data.expiresAt) : NaN;
  if (!Number.isNaN(expires) && expires < Date.now()) return null;
  const photo = typeof data.personPhoto === 'string' && data.personPhoto.startsWith('https://')
    ? data.personPhoto
    : '';
  return {
    inviterName: typeof data.inviterName === 'string' ? data.inviterName : 'Someone',
    personName: typeof data.personName === 'string' ? data.personName : 'them',
    photoUrl: photo,
  };
}

function respond(statusCode, payload) {
  return { statusCode, headers: CORS, body: JSON.stringify(payload) };
}

function wrap(run) {
  return async (event) => {
    if (event.httpMethod === 'OPTIONS') return { statusCode: 204, headers: CORS, body: '' };
    try {
      return await run(event);
    } catch (error) {
      return respond(500, { ok: false });
    }
  };
}

module.exports = {
  fp, crypto, firestore, signalsFrom, publicPreview, respond, wrap,
};
