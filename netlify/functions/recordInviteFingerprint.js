const { wrap, fp, crypto, firestore, signalsFrom, publicPreview, respond } = require('../lib/http');

exports.handler = wrap(async (event) => {
  const { body, signals } = signalsFrom(event);
  const code = String(body.code || '');
  if (!code || !fp.fingerprintIsSpecific(signals)) return respond(400, { ok: false });
  const preview = await publicPreview(code);
  if (!preview) return respond(404, { ok: false });
  const now = Date.now();
  const id = crypto.createHash('sha256').update(fp.canonicalFingerprint(signals)).digest('hex');
  await firestore().doc(`pendingInvites/${id}`).set({
    code,
    expiresAt: fp.fingerprintExpiresAt(now),
    createdAt: now,
  });
  return respond(200, { ok: true, expiresAt: fp.fingerprintExpiresAt(now), ...preview });
});
