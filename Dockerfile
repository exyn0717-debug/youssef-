FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 METHOD_DATA_DIR=/srv/method-data
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && useradd --uid 10001 --create-home method && mkdir -p /srv/method-data && chown method:method /srv/method-data
COPY --chown=method:method app ./app
COPY --chown=method:method public ./public
COPY --chown=method:method content ./content
COPY --chown=method:method tools ./tools
COPY --chown=method:method run.py .
USER method
EXPOSE 8000
VOLUME ["/srv/method-data"]
HEALTHCHECK --interval=30s --timeout=5s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/api/health', timeout=3)"
CMD ["python", "run.py", "--host", "0.0.0.0", "--port", "8000"]
