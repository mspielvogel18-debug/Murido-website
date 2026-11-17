/**
 * Shared deferred-invite matching. The Cloud Function and the app both use
 * this file so a fingerprint built in Safari matches the one built on device.
 *
 * The key is coarse on purpose: IP, iOS major.minor, phone family, screen
 * size, timezone, and language. It expires after one hour.
 */

const FINGERPRINT_TTL_MS = 60 * 60 * 1000;

function normIp(raw) {
  return String(raw || '').split(',')[0].trim();
}

function normIos(raw) {
  const match = String(raw || '').match(/(\d+)[._](\d+)/);
  return match ? `${match[1]}.${match[2]}` : '';
}

function normModel(raw) {
  const value = String(raw || '').toLowerCase();
  if (value.includes('ipad')) return 'ipad';
  if (value.includes('iphone')) return 'iphone';
  if (value.includes('ipod')) return 'ipod';
  return value ? 'other' : '';
}

function normScreen(width, height) {
  const a = Math.round(Number(width) || 0);
  const b = Math.round(Number(height) || 0);
  if (!a || !b) return '';
  return `${Math.min(a, b)}x${Math.max(a, b)}`;
}

function normTz(raw) {
  return String(raw || '').trim();
}

function normLang(raw) {
  const value = String(raw || '').toLowerCase().replace('_', '-');
  return value.split('-')[0] || '';
}

function canonicalFingerprint(signals) {
  return [
    normIp(signals && signals.ip),
    normIos(signals && signals.ios),
    normModel(signals && signals.model),
    normScreen(signals && signals.screenW, signals && signals.screenH),
    normTz(signals && signals.tz),
    normLang(signals && signals.lang),
  ].join('|');
}

function fingerprintIsSpecific(signals) {
  const parts = canonicalFingerprint(signals).split('|');
  return Boolean(parts[0] && parts[1] && parts[3]);
}

function fingerprintExpiresAt(now) {
  return now + FINGERPRINT_TTL_MS;
}

function fingerprintIsUsable(expiresAt, now) {
  return typeof expiresAt === 'number' && expiresAt > now;
}

function codeFromInviteToken(raw) {
  const text = String(raw || '');
  const token = text.match(/murido-invite:([A-Za-z0-9]+)/i);
  if (token) return token[1];
  const path = text.match(/\/join\/([A-Za-z0-9]+)/i);
  if (path) return path[1];
  return null;
}

function normalizeEmail(raw) {
  const value = String(raw || '').trim().toLowerCase();
  if (!value || value.includes(' ') || !value.includes('@')) return null;
  return value;
}

function normalizePhone(raw) {
  const digits = String(raw || '').replace(/\D/g, '');
  if (digits.length < 8) return null;
  return digits;
}

function contactHashInput(kind, raw) {
  if (kind === 'email') {
    const email = normalizeEmail(raw);
    return email ? `email:${email}` : null;
  }
  const phone = normalizePhone(raw);
  return phone ? `phone:${phone}` : null;
}

/**
 * One winner. A universal link beats a fresh fingerprint, which beats the
 * clipboard, which beats a hashed contact, which beats a typed code.
 * An expired fingerprint is ignored.
 */
function chooseDeferredMatch(input) {
  const now = input.now;
  if (input.linkCode) return { method: 'universal_link', code: input.linkCode };
  if (input.fingerprint && fingerprintIsUsable(input.fingerprint.expiresAt, now)) {
    return { method: 'fingerprint', code: input.fingerprint.code };
  }
  if (input.clipboardCode) return { method: 'clipboard', code: input.clipboardCode };
  if (input.contactCode) return { method: 'contact', code: input.contactCode };
  if (input.typedCode) return { method: 'code', code: input.typedCode };
  return null;
}

module.exports = {
  FINGERPRINT_TTL_MS,
  canonicalFingerprint,
  fingerprintIsSpecific,
  fingerprintExpiresAt,
  fingerprintIsUsable,
  codeFromInviteToken,
  normalizeEmail,
  normalizePhone,
  contactHashInput,
  chooseDeferredMatch,
};
