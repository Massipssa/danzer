# Architecture

## Target layout

```text
danzer/anonymizer/
  api/
  application/
    dto/
    use_cases/
    validators/
  cli/
  domain/
    models/
    rules/
  infrastructure/
    connectors/
    engines/
    readers/
    writers/
```

## Layer responsibilities

- `domain`: pure business rules and job models; no pandas, Spark, filesystem, or CLI dependencies.
- `application`: orchestration use cases that validate config, build jobs, and coordinate infrastructure.
- `infrastructure`: concrete adapters for filesystem, datasource connectors, datasets, pandas, Spark, JSON readers, and output writers.
- `api`: simple facade for programmatic callers.
- `cli`: command-line entrypoints and argument parsing.

## Package relocation

- legacy `dataset/` now maps to `infrastructure/datasets/`
- legacy `datasource/` now maps to `infrastructure/sources/` and `infrastructure/connectors/`
- legacy `core/` business contracts now map to `domain/`; pandas-specific helpers remain infrastructure concerns

The legacy packages are kept as compatibility wrappers during migration so existing imports continue to work.

## Migration plan

1. Keep legacy `core`, `engine`, `runner`, and `datasource` modules working while new flows land.
2. Move new features into `domain` + `application` first.
3. Gradually migrate the legacy runner to the `api` and `cli` flow.
4. Delete compatibility shims only after imports and tests are migrated.

## First implemented slice

The codebase now includes a first vertical slice:
- JSON job config reader
- application DTO + validator
- `RunAnonymizationUseCase`
- domain `ColumnSuppressionRule`
- pandas and Spark execution engines
- API facade and CLI entrypoint

This keeps the current tests intact while giving the project a cleaner destination architecture.
