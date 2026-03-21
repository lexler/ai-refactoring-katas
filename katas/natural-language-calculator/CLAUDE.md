# Project Instructions

This is a Python refactoring kata. See REFACTORING_EXERCISE.md for the exercise description.

## Tools

- **yaks** (`yx`): A yak-shaving tracker for managing work breakdown. Use `yx ls` to see the map, `yx add` to add yaks, `yx start`/`yx done` to track progress.
- **bin/commit**: Runs tests then commits. Usage: `bin/commit "message"`
- **bin/show-yak-map**: Watch the yak map in real-time.

## Running Tests

```bash
python -m unittest tests.test_calculator -v
```

## Conventions

- Keep changes small and safe — one refactoring step at a time.
- Always run tests before committing (bin/commit does this automatically).
- Use descriptive commit messages.
