---
name: dockerfile
description: Write, review, and optimize Dockerfiles applying multi-stage builds, non-root constraints, layer caching, and strict image pinning.
---

# Skill: dockerfile

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Create and maintain highly optimized, secure, and minimal Dockerfiles. Focus on strict deterministic builds, security compliance, and caching efficiency.

## Core Process

1. **Base Selection**: Use official, minimal bases (e.g., `alpine`, `distroless`) with precise version tags or SHA256 pinning.
2. **Dependency Layering**: Copy manifests (e.g., `package.json`, `go.mod`) first, install dependencies, then `COPY` source code to maximize cache hits.
3. **Multi-Stage Builds**: Separate build-time environments from runtime execution. Only copy compiled artifacts to the final stage.
4. **Layer Consolidation**: Chain `RUN` commands with `&&` and clear package manager caches within the same layer.
5. **Least Privilege**: Define a non-root `USER` before `ENTRYPOINT` or `CMD`.

## Core Principles

- **Determinism**: Avoid `latest` tags to prevent build drift and ensure reproducible environments.
- **Immutability**: Treat the container filesystem as read-only. Mount volumes for mutable paths.
- **Signal Handling**: Use the `exec` JSON array form for `ENTRYPOINT` and `CMD` (e.g., `["node", "app.js"]`) instead of shell form to allow graceful termination (SIGTERM).

## Commands / Usage Patterns

- **Minimal Multi-Stage Pattern**:
  ```dockerfile
  FROM golang:1.24-alpine AS builder
  WORKDIR /app
  COPY go.mod go.sum ./
  RUN go mod download
  COPY . .
  RUN CGO_ENABLED=0 go build -o /server .

  FROM gcr.io/distroless/static-debian11
  COPY --from=builder /server /server
  USER nonroot:nonroot
  EXPOSE 8080
  ENTRYPOINT ["/server"]
  ```

- **Apt Cache Cleanup**:
  ```dockerfile
  RUN apt-get update && \
      apt-get install -y --no-install-recommends curl jq && \
      rm -rf /var/lib/apt/lists/*
  ```

- **Discovering Real-World Usage**:
  Use `gh search` to surface advanced Dockerfile patterns and community best practices directly from GitHub:
  - Find multi-stage architecture examples:
    `gh search code '/FROM[[:space:]]+[^[:space:]]+[[:space:]]+AS[[:space:]]+/' --filename="Dockerfile" --limit 5 --json repository,path,url`
  - Locate top-rated repository templates and guides:
    `gh search repos "Dockerfile best practices" --sort stars --order desc --limit 5 --json fullName,description,url`

## Diagnostics and Troubleshooting

- **Large Images**: Inspect layer bloat with `docker history <image>` or use `dive`. Watch for orphaned cache files.
- **Cache Misses**: Ensure `COPY . .` is positioned as late as possible. A single modified source file busts the cache for all subsequent steps.
- **Permission Denied**: If a non-root user fails to execute, verify ownership of `WORKDIR` and any required runtime directories using `chown` in the previous build stage.

## What to Avoid

- **Avoid Root**: Never omit the `USER` directive in a production image.
- **Avoid Shell Form**: Do not write `ENTRYPOINT npm start`. Using shell form spawns a `/bin/sh` wrapper, breaking signal propagation.
- **Avoid Build Tools in Runtime**: Never ship `gcc`, `make`, or similar tools in the final image.
- **Avoid Baked Secrets**: Never embed credentials using `ENV` or `COPY`. Use `--mount=type=secret` during build or inject at runtime.