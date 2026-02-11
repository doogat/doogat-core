# CLAUDE.md

Core domain library for the Doogat zettelkasten system. Provides entities, use cases, value objects, and infrastructure for zettel management.

## Quick Start

```bash
uv sync --all-groups                        # install deps
pre-commit install --hook-type pre-commit --hook-type post-commit  # setup hooks
uv run pytest                               # run tests
./dev/bin/refresh-docs                      # rebuild docs (strict)
release                                     # trigger release workflow (TUI)
```

## Architecture

```text
src/doogat/core/
├── application/         # Use cases (PrintZettel, ReadDoogat)
├── domain/
│   ├── entities/        # Zettel, Project (with consistency/migration services)
│   ├── interfaces/      # ZettelRepository, ZettelFormatter (abstract)
│   ├── services/        # DoogatFactory
│   └── value_objects/   # ZettelData
└── infrastructure/
    ├── formatting/      # MarkdownZettelFormatter
    └── persistence/     # File parsers, MarkdownZettelRepository
```

**Key patterns:**

- **Clean Architecture / DDD**: application → domain → infrastructure dependency flow
- **Consistency services**: chain of fixers that enforce zettel invariants
- **Migration services**: chain of upgrades that evolve zettel format across versions
- **Fixer / upgrade pattern**: small single-purpose classes, each handling one concern

## Code Conventions

**Type hints** - modern style, no `Optional`:

```python
from __future__ import annotations
def foo(path: Path | None = None) -> list[str]: ...
```

**Imports**:

- Explicit `__all__` in `__init__.py`
- `TYPE_CHECKING` guards for type-only imports
- Platform-specific conditional imports in adapters

**Docstrings**: Google format

## Testing

- pytest + pytest-mock
- Tests in `tests/` mirror `src/` structure
- Mock subprocess calls heavily
- Class-based test organization
- **No unused imports/variables**: don't add `noqa: F401` or `noqa: F841` - either use the import/variable or remove it
- If a test creates an object just for side effects (e.g., testing `__init__`), add an assertion to use it: `assert issubclass(Foo, Base)`

```python
@pytest.fixture
def zettel():
    zettel = MagicMock(spec=doogat_entities.Zettel)
    zettel.get_data = MagicMock(return_value={"some": "data"})
    return zettel

class TestDoogatFactory:
    def test_create_with_generic_type(self, zettel): ...
```

## Release

```bash
release  # TUI: pick release type, bump level, confirm, watch
```

Triggers the GitHub Actions release workflow. Alternative: Actions tab → Release → Run workflow.

Version determined from conventional commits (`feat:` → minor, `fix:` → patch).

See `dev/docs/versioning.md` for details.
