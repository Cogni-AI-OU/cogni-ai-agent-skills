---
name: python
description: >-
  Expert Python language skill for writing, refactoring, and testing idiomatic Python 3 code.
  You MUST load this skill when developing Python modules, classes, or scripts.
license: MIT
---

# Skill: python

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use this skill when developing Python code. For inline bash script Python execution, refer to the `python-cli` skill.

## When to Use

- Writing new Python 3 scripts, modules, or classes.
- Refactoring existing Python code for performance, readability, or modern syntax.
- Writing unit tests using `pytest` or `unittest`.
- Debugging complex Python tracebacks or logic errors.

## When Not to Use

- When executing one-off shell pipeline data transformations (use `python-cli` instead).
- For writing shell scripts (`bash`) or other languages (`JS/TS`, `Go`, `Rust`).
- When managing project dependencies or virtual environments (use `pipenv` or `pipfile` skills instead).

## Common Pitfalls

- **Ignoring Type Hints**: Writing naked functions without `typing` module annotations, making the code harder to maintain and refactor.
- **Mutable Default Arguments**: Using `def foo(items=[])` instead of `def foo(items=None)`.
- **Catch-All Exceptions**: Using a bare `except:` or `except Exception:` without logging the traceback or re-raising, swallowing critical errors silently.

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
