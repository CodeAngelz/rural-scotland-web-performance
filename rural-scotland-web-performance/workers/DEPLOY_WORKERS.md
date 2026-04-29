# Deploying to Cloudflare Workers (Edge Computing)

## What is Cloudflare Workers?

Edge computing that runs your JavaScript code at the nearest Cloudflare location to each user.
Unlike a CDN, Workers executes code at the edge rather than just serving static files.

## Prerequisites

- Node.js installed ([nodejs.org](https://nodejs.org))
- Free Cloudflare account ([dash.cloudflare.com](https://dash.cloudflare.com))

## Deployment Steps

### 1. Install Wrangler

```bash
npm install -g wrangler
wrangler --version
```

### 2. Authenticate

```bash
wrangler login
```

Approve the browser prompt.

### 3. Build the React Site

```bash
cd demo-site
npm install
npm run build
cd ..
```

### 4. Create KV Namespace

```bash
wrangler kv:namespace create "ASSETS"
```

Copy the `id` printed (looks like `id = "abc123..."`)

### 5. Configure wrangler.toml

Edit `workers/wrangler.toml` and paste the KV namespace id:

```toml
[[kv_namespaces]]
binding = "ASSETS"
id = "PASTE_YOUR_ID_HERE"
```

### 6. Upload Files to KV

```bash
wrangler kv:bulk put --namespace-id YOUR_KV_ID demo-site/build
```

Replace `YOUR_KV_ID` with the id from step 4.

### 7. Deploy

```bash
cd workers
wrangler deploy
```

Your site is live at: `https://skyeandglen.skyeandglen-uws.workers.dev/`

## Verify Deployment

1. Visit your workers.dev URL
2. Open DevTools (F12) → Network tab
3. Click the main HTML file
4. Look for response header: `x-served-by: Cloudflare-Workers-Edge`

## Compare Performance

Compare TTFB between:
- Workers version (`workers.dev` URL) 
- CDN version (`pages.dev` URL)

Workers should show lower TTFB due to edge execution.

## Notes

- Free plan: 100,000 requests/day
- Redeploy: Re-run step 6 if rebuilding
