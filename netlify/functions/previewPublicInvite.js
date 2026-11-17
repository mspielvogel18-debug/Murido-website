const { wrap, publicPreview, respond } = require('../lib/http');

exports.handler = wrap(async (event) => {
  const body = JSON.parse(event.body || '{}');
  const code = String(body.code || event.queryStringParameters?.code || '');
  const preview = await publicPreview(code);
  if (!preview) return respond(404, { ok: false });
  return respond(200, { ok: true, ...preview });
});
