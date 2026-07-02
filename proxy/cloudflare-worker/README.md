# NPC Image Draw Proxy

Cloudflare Worker proxy for `npc-image-prompt`.

The worker keeps the Right Codes API key on the server side, so machines that install the
skill can generate images without configuring an API key locally.

## Deploy

1. Install Wrangler:

```bash
npm install -g wrangler
```

2. Login:

```bash
wrangler login
```

3. Set the secret:

```bash
wrangler secret put RIGHT_CODES_DRAW_API_KEY
```

4. Deploy:

```bash
wrangler deploy
```

5. Configure the skill script to use the deployed URL:

```powershell
$env:RIGHT_CODES_DRAW_PROXY_URL="https://your-worker-name.your-subdomain.workers.dev"
```

After this, local users do not need `RIGHT_CODES_DRAW_API_KEY`.

## Request

`POST /`

```json
{
  "model": "gpt-image-2",
  "prompt": "Full-body Japanese anime game character illustration...",
  "n": 1,
  "size": "auto",
  "quality": "auto",
  "output_format": "png",
  "background": "auto",
  "moderation": "auto"
}
```

The response is the upstream Right Codes JSON.
