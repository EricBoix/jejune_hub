#!/bin/sh
# Write runtime config from env vars so the static page can read service URLs.
cat > /usr/share/nginx/html/config.js <<EOF
window.__JEJUNE_HUB_CONFIG__ = {
  DOCS_SERVER_URL:        "${JEJUNE_DOCS_SERVER_URL:-}",
  KG_VIEWER_URL:          "${JEJUNE_KG_VIEWER_URL:-}",
  MARKDOWN_BROWSER_URL:   "${JEJUNE_MARKDOWN_BROWSER_URL:-}",
  KG_VIEWER_OXIGRAPH_URL: "${JEJUNE_KG_VIEWER_OXIGRAPH_URL:-}",
  OXIGRAPH_URL:           "${JEJUNE_OXIGRAPH_URL:-}"
};
EOF
exec nginx -g 'daemon off;'
