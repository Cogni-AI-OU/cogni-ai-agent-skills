---
name: dockerfile
description: Write, review, and optimize Dockerfiles applying multi-stage builds, non-root constraints, layer caching, and strict image pinning.
license: MIT
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
  # Use specific version and digest for deterministic builds
  FROM golang:1.24.0-alpine3.21@sha256:e74d913cc537f546b946e685c84a98598ba93b4de1f762d0c353a4261a1d1052 AS builder
  WORKDIR /app
  COPY go.mod go.sum ./
  RUN go mod download
  COPY . .
  # Force static build by disabling CGO and stripping symbols
  RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /server .

  # Use a digest-pinned nonroot distroless base for maximum security
  FROM gcr.io/distroless/static-debian12:nonroot@sha256:e906328329624536768a49c9527ec3c3068e14e1a0b3554e2043697e88457e5e
  COPY --from=builder /server /server
  USER nonroot:nonroot
  EXPOSE 8080
  ENTRYPOINT ["/server"]
  ```

- **Deterministic Package Installation**:
  ```dockerfile
  RUN apt-get update && \
      apt-get install -y --no-install-recommends \
      curl=7.88.1-10+deb12u8 \
      jq=1.6-2.1 && \
      rm -rf /var/lib/apt/lists/*
  ```

- **Discovering Real-World Usage**:
  Use `gh search` to surface advanced Dockerfile patterns and community best practices directly from GitHub:
  - Find multi-stage architecture examples (requires `AS` keyword):
    `gh search code "FROM" "AS" --language dockerfile --limit 5 --json repository,path,url`
  - Locate repository templates and guides (sorted by stars):
    `gh search repos "Dockerfile best practices" --sort stars --order desc --limit 5 --json fullName,description,url`

## Diagnostics and Troubleshooting

- **Large Images**: Inspect layer bloat with `docker history <image>` or use `dive`. Watch for orphaned cache files.
- **Cache Misses**: Ensure `COPY . .` is positioned as late as possible. A single modified source file busts the cache for all subsequent steps.
- **Permission Denied**: If a non-root user fails to execute, verify ownership of `WORKDIR`, copied artifacts, and runtime directories. **Crucial**: Ownership must be fixed in the **final** image stage (e.g., using `COPY --chown` or `RUN chown` before switching to `USER`), as permissions set in builder stages do not persist for files copied to the final runtime image. Distroless images may require fixing ownership in the builder if the final image lacks shell tools, or ideally using `COPY --chown`.

## What to Avoid

- **Avoid Root**: Never omit the `USER` directive in a production image.
- **Avoid Shell Form**: Do not write `ENTRYPOINT npm start`. Using shell form spawns a `/bin/sh` wrapper, breaking signal propagation.
- **Avoid Build Tools in Runtime**: Never ship `gcc`, `make`, or similar tools in the final image.
- **Avoid Baked Secrets**: Never embed credentials using `ENV` or `COPY`. Use `--mount=type=secret` during build or inject at runtime.

## Related Skills

- **docker**:
  You MUST load this skill when running, managing, or troubleshooting Docker containers and networks.
