---
name: python
description: 'Expert Python language skill for writing, refactoring, and testing idiomatic Python 3 code. You MUST load this skill when developing Python modules, classes, or scripts.'
license: MIT
---

# Skill: python

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- When writing or refactoring Python 3 modules, classes, functions, or scripts following PEP 8 and idiomatic patterns.
- When adding type hints, dataclasses, or modern Python 3.11+ features (`match`/`case`, `Self` type, etc.) to existing code.
- When creating unit tests with `pytest` for Python business logic.
- When reviewing Python code for adherence to naming conventions, docstring standards, and type safety.
- When developing new Python projects where code structure, maintainability, and testability are priorities.
- When applying error handling patterns with proper logging and exception chaining.

## When Not to Use
- When executing quick one-off Python commands or inline scripts from the shell — use the **python-cli** skill for heredoc-based or `-c` one-liner execution.
- When managing Python dependencies or virtual environments — use the **pipenv** or **pipfile** skills instead.
- When writing Python that targets versions below 3.10 — this skill assumes modern Python features are available.
- When the task is purely about packaging or distribution (setup.py, pyproject.toml) — use dedicated packaging skills.
- When debugging Python runtime issues unrelated to code style/quality (e.g., segfaults, interpreter crashes) — those require platform-specific troubleshooting.

## Common Pitfalls
- Type hints do not enforce anything at runtime — they are purely for static analysis and documentation; never rely on them for input validation.
- Python 3.11+ features like `Self` type or `@dataclass(slots=True)` may not work in codebases targeting older versions — always check the project's minimum Python version.
- `pytest` discovery requires `test_` prefix or `_test` suffix in file/function names — incorrectly named test files are silently ignored.
- Mutable default arguments (e.g., `def foo(x=[])`) remain a classic pitfall — use `None` with a default factory pattern or `field(default_factory=list)` in dataclasses.
- Logging configuration can be silenced by parent loggers — always use `__name__` as the logger name and verify propagation settings.

Use this skill when developing Python code. For inline bash script Python execution, refer to the `python-cli` skill.

## Core Principles

- **Idiomatic Python**: Follow PEP 8 guidelines for code style. Use standard Python naming conventions.
- **Type Hinting**: Always use type hints (`typing` module) for function signatures and class attributes.
- **Modern Features**: Utilize modern Python 3.11+ features like `match`/`case`, dataclasses, and standard library enhancements when applicable.
- **Docstrings**: Document classes and functions using standard docstring formats (e.g., Google or Sphinx style) describing arguments, return types, and exceptions raised.
- **Testing**: Ensure all business logic is covered by unit tests (e.g., using `pytest`).

## Usage Patterns

### Dataclasses and Type Hints

Use dataclasses for robust data structures:

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class User:
    id: int
    username: str
    email: Optional[str] = None
    roles: List[str] = field(default_factory=list)

    def is_admin(self) -> bool:
        """Check if the user has the 'admin' role."""
        return 'admin' in self.roles
```

### Error Handling

Use explicit exception handling:

```python
import logging

logger = logging.getLogger(__name__)

def process_data(data: dict) -> None:
    try:
        value = data['key']
        # Process value
    except KeyError as e:
        logger.error(f"Missing required key: {e}")
        raise ValueError("Invalid data format") from e
```
