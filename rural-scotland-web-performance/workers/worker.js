/**
 * Cloudflare Workers edge computing script.
 * Runs at the nearest Cloudflare edge location to the user.
 * Serves files from KV storage and handles routing.
 */
export default {
  async fetch(request, env) {
    try {
      const url = new URL(request.url);
      let path = url.pathname;

      if (path === '/' || path === '') {
        return serveFile(env, 'index.html', 'text/html; charset=utf-8');
      }

      if (path.includes('.css')) {
        return serveFile(env, 'static/css/main.css', 'text/css; charset=utf-8');
      }

      if (path.includes('.js') && !path.includes('.json')) {
        return serveFile(env, 'static/js/main.js', 'application/javascript; charset=utf-8');
      }

      return serveFile(env, 'index.html', 'text/html; charset=utf-8');

    } catch (err) {
      return new Response('Error: ' + err.message, { status: 500 });
    }
  },
};

async function serveFile(env, key, contentType) {
  const asset = await env.ASSETS.get(key, { type: 'arrayBuffer' });
  if (!asset) {
    return new Response('Not found: ' + key, { status: 404 });
  }
  return new Response(asset, {
    status: 200,
    headers: {
      'Content-Type': contentType,
      'Cache-Control': key === 'index.html'
        ? 'no-cache, no-store, must-revalidate'
        : 'public, max-age=31536000, immutable',
      'X-Served-By': 'Cloudflare-Workers-Edge',
    },
  });
}

function getContentType(path) {
  if (path.endsWith('.html')) return 'text/html; charset=utf-8';
  if (path.endsWith('.css'))  return 'text/css; charset=utf-8';
  if (path.endsWith('.js'))   return 'application/javascript; charset=utf-8';
  return 'text/plain';
}