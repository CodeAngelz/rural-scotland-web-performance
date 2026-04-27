# Deploying to Cloudflare Pages (CDN)

## What is Cloudflare Pages?

A CDN that stores your built files on servers worldwide. Users download from the geographically nearest server.

## Prerequisites

- Free Cloudflare account ([dash.cloudflare.com](https://dash.cloudflare.com))
- Node.js installed

## Deployment Steps

### 1. Build the React Site

```bash
cd demo-site
npm install
npm run build
```

Creates a `build/` folder with production-ready files.

### 2. Deploy to Cloudflare Pages

**Method A: Drag & Drop (Easiest)**
1. Go to [dash.cloudflare.com](https://dash.cloudflare.com)
2. Click Workers and Pages → Create application
3. Select Pages tab → Upload assets
4. Give your project a name (e.g., `skye-and-glen`)
5. Drag entire `build/` folder into upload box
6. Click Deploy site

**Method B: Git Integration**
1. Push repo to GitHub
2. In Cloudflare Pages, connect your repo
3. Set build command: `npm run build`
4. Set publish directory: `build`

## Result

Your site will be live at: `https://[project-name].pages.dev`

## Monitoring

View deployment status and logs in Cloudflare Pages dashboard.
Updates are deployed on every new build.

### Option B — Connect to GitHub (recommended)

1. Push this repository to GitHub first
2. In Cloudflare Dashboard go to Workers and Pages
3. Click Create application, then Pages, then Connect to Git
4. Choose your GitHub repository from the list
5. Set Build command to:          npm run build
6. Set Build output directory to: build
7. Click Save and Deploy

With this option, every time you push a change to GitHub,
Cloudflare redeploys the site automatically.

---

## Checking it worked

Visit your pages.dev URL in a browser.
Press F12 to open developer tools and click the Network tab.
Click the main HTML file in the list.
Look for this in the response headers:
  cf-cache-status: HIT

This confirms Cloudflare served the file from its CDN cache.

---

## Notes

- The free Cloudflare Pages plan is more than enough for this project
- Build time is usually under 30 seconds
- Your site will have HTTPS automatically, no setup needed
