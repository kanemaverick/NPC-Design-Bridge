const DEFAULT_BODY = {
  model: "gpt-image-2",
  n: 1,
  size: "auto",
  quality: "auto",
  output_format: "png",
  background: "auto",
  moderation: "auto",
};

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      ...CORS_HEADERS,
      "Content-Type": "application/json; charset=utf-8",
    },
  });
}

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    if (request.method !== "POST") {
      return json({ error: "Only POST is supported." }, 405);
    }

    if (!env.RIGHT_CODES_DRAW_API_KEY) {
      return json({ error: "Server is missing RIGHT_CODES_DRAW_API_KEY." }, 500);
    }

    let incoming;
    try {
      incoming = await request.json();
    } catch {
      return json({ error: "Invalid JSON body." }, 400);
    }

    const prompt = typeof incoming.prompt === "string" ? incoming.prompt.trim() : "";
    if (!prompt) {
      return json({ error: "Field `prompt` is required." }, 400);
    }

    const body = {
      ...DEFAULT_BODY,
      ...incoming,
      prompt,
      image: undefined,
      response_format: undefined,
    };

    const baseUrl = (env.RIGHT_CODES_DRAW_BASE_URL || "https://www.right.codes/draw").replace(/\/+$/, "");
    const upstream = await fetch(`${baseUrl}/v1/images/generations`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.RIGHT_CODES_DRAW_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const text = await upstream.text();
    return new Response(text, {
      status: upstream.status,
      headers: {
        ...CORS_HEADERS,
        "Content-Type": upstream.headers.get("Content-Type") || "application/json; charset=utf-8",
      },
    });
  },
};
