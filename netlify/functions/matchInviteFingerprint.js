const { wrap, fp, crypto, firestore, signalsFrom, publicPreview, respond } = require('../lib/http');

exports.handler = wrap(async (event) => {
  const { signals } = signalsFrom(event);
  if (!fp.fingerprintIsSpecific(signals)) return respond(200, { match: false });
  const id = crypto.createHash('sha256').update(fp.canonicalFingerprint(signals)).digest('hex');
  const snap = await firestore().doc(`pendingInvites/${id}`).get();
  if (!snap.exists) return respond(200, { match: false });
  const data = snap.data() || {};
  if (!fp.fingerprintIsUsable(data.expiresAt, Date.now())) return respond(200, { match: false });
  const preview = await publicPreview(data.code);
  if (!preview) return respond(200, { match: false });
  return respond(200, { match: true, code: data.code, ...preview });
});
