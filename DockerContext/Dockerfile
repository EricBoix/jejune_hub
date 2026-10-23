FROM nginx:alpine
COPY DockerContext/static/ /usr/share/nginx/html/
COPY DockerContext/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENV JEJUNE_DOCS_SERVER_URL="" \
    JEJUNE_KG_VIEWER_URL="" \
    JEJUNE_MARKDOWN_BROWSER_URL="" \
    JEJUNE_KG_VIEWER_OXIGRAPH_URL="" \
    JEJUNE_OXIGRAPH_URL=""
ENTRYPOINT ["/docker-entrypoint.sh"]
