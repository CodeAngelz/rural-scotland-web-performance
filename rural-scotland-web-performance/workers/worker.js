/**
 * Cloudflare Workers edge computing script.
 * Runs at the nearest Cloudflare edge location to the user.
 * Serves files from KV storage and handles routing.
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    let path = url.pathname;

    if (path === '/' || path === '') {
      path = '/index.html';
    }

    let asset = await env.ASSETS.get(path, { type: 'arrayBuffer' });

    if (!asset) {
      asset = await env.ASSETS.get('/index.html', { type: 'arrayBuffer' });
      path = '/index.html';
    }

    const contentType = getContentType(path);

    return new Response(asset, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Cache-Control': path === '/index.html'
          ? 'no-cache, no-store, must-revalidate'
          : 'public, max-age=31536000, immutable',
        'X-Served-By': 'Cloudflare-Workers-Edge',
        'X-Project': 'MSc Rural Scotland Web Performance',
      },
    });
  },
};

function getContentType(path) {
  if (path.endsWith('.html')) return 'text/html; charset=utf-8';
  if (path.endsWith('.css')) return 'text/css; charset=utf-8';
  if (path.endsWith('.js')) return 'application/javascript; charset=utf-8';
  if (path.endsWith('.jsx')) return 'application/javascript; charset=utf-8';
  if (path.endsWith('.json')) return 'application/json; charset=utf-8';
  if (path.endsWith('.png')) return 'image/png';
  if (path.endsWith('.jpg')) return 'image/jpeg';
  if (path.endsWith('.jpeg')) return 'image/jpeg';
  if (path.endsWith('.svg')) return 'image/svg+xml';
  if (path.endsWith('.ico')) return 'image/x-icon';
  if (path.endsWith('.woff2')) return 'font/woff2';
  if (path.endsWith('.woff')) return 'font/woff';
  if (path.endsWith('.ttf')) return 'font/ttf';
  return 'text/plain';
}
  if (path.endsWith('.ttf'))   return 'font/ttf';
  return 'text/plain';
}
