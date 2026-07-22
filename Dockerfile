# ---------- deps ----------
FROM python:3.12-slim AS deps

WORKDIR /build

COPY requirements.txt .

RUN pip install \
    --prefix=/install \
    -r requirements.txt

# ---------- aql-link ----------
FROM deps AS aql-link

COPY --from=deps /install /usr/local

COPY src/ .

RUN python -m build

RUN mv dist/*.whl /tmp/

# ---------- runtime ----------
FROM deps AS runtime

COPY --from=deps /install /usr/local

COPY --from=aql-link /tmp/*.whl /tmp
RUN pip install /tmp/*.whl

WORKDIR /app

COPY data .