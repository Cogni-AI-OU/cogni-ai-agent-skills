---
name: docker
description: How to run, manage, and troubleshoot Docker containers, images, and networks safely via the command line.
license: MIT
---

# Skill: docker

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Execute, inspect, and manage Docker containers, images, and network components directly via the CLI, adhering to safe operational boundaries.

## Core Principles

- **Non-Interactive Execution**: Never use `-it` or interactive pseudo-TTY modes when executing container commands autonomously. Always run in detached (`-d`) or batch execution modes.
- **Resource Cleanup**: Always use `--rm` for ephemeral run commands to prevent container accumulation. Clean up unused images regularly using `docker system prune`, and prune unused volumes with `docker volume prune` or `docker system prune --volumes`.
- **Absolute Paths for Mounts**: When binding volumes via `-v`, strictly use absolute paths (`$PWD` or full paths) rather than relative paths.
- **JSON Formatting**: When querying for container state or image details, prefer structured output (`--format '{{json .}}'`) for robust parsing.

## Commands / Usage Patterns

- **Run Ephemeral Containers**:
  `docker run --rm -v "$PWD":/work -w /work <image> <command>`
- **Run Detached Services with Port Binding**:
  `docker run -d --name <container_name> -p <host_port>:<container_port> <image>`
- **Execute Commands in Running Container (Non-Interactive)**:
  `docker exec <container_name> <command>`
  *(Avoid `-it` for automated agent workflows)*
- **Stream Logs with Timestamps**:
  `docker logs --timestamps --tail 50 <container_name>`
- **Inspect Container Details via JSON**:
  `docker inspect --format='{{json .State.Health}}' <container_name>`
- **List Running Containers (Structured Output)**:
  `docker ps --format '{"ID":"{{.ID}}", "Image": "{{.Image}}", "Names":"{{.Names}}", "Status":"{{.Status}}"}'`
- **Build Image with Tags**:
  `docker build -t <image_name>:<tag> -f <Dockerfile_path> .`

## Diagnostics and Troubleshooting

- **Debugging Failed Starts**: If a container exits immediately, run `docker logs <container_name>` to trace startup errors.
- **Inspecting Mount Permissions**: For `permission denied` errors inside the container, verify host directory permissions or apply SELinux volume labels (`:z` or `:Z`).
- **Network Resolution Issues**: If containers cannot reach each other, verify they share a user-defined network using `docker network inspect <network_name>`.

## What to Avoid

- **Do not** run interactive sessions (`docker run -it` or `docker exec -it`). These will hang automated agents.
- **Do not** parse tabular `docker ps` or `docker images` output using `grep` or `awk` when `--format` json templating is available.
- **Do not** leak credentials via CLI arguments or environment variables (`-e PASSWORD=xyz`). Use `docker secret` (Swarm) or mount credential files securely.

## Limitations

- The agent cannot solve authentication steps interactively (e.g., `docker login` without a password feed).
- Building massive images may exceed time-to-live execution limits; prefer optimized caching.

## Related Skills

- **shell**:
  You MUST load this skill when handling shell commands with performance monitoring or timeouts.
- **dockerfile**:
  You MUST load this skill when writing, reviewing, or optimizing Dockerfiles.
