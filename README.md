# doogat-core

Core domain library for the Doogat zettelkasten system. Provides entities, use cases, value objects, and infrastructure for zettel management.

## Install

```bash
pip install doogat-core
```

## Features

- **Entities** - Zettel, Project with consistency and migration services
- **Use cases** - PrintZettel, ReadDoogat
- **Value objects** - ZettelData
- **Infrastructure** - Markdown formatting and file-based persistence

## Development

```bash
uv sync --all-groups                        # install deps
pre-commit install --hook-type pre-commit --hook-type post-commit  # setup hooks
uv run pytest                               # run tests
```

## Release

Releases via GitHub Actions (manual trigger):

1. Go to Actions → Release workflow → Run workflow
2. Choose `prerelease` (test.pypi only) or `release` (both pypis + GitHub release)

Version determined from conventional commits (`feat:` → minor, `fix:` → patch).

```bash
uv run semantic-release version --print --noop  # preview next version
```

See [dev/docs/versioning.md](dev/docs/versioning.md) for details.

## License

GPL-3.0
