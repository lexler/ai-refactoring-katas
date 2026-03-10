# Refactoring Log

## What was refactored

### Eliminating duplication through data-driven design

The original `processor.py` contained 8 nearly identical branches handling compound expressions (`plus the result of`, `minus the result of`, etc.) with and without comma separators. Each branch duplicated the same split-evaluate-combine pattern. A similar 4-branch duplication existed for simple operations.

This was replaced with a single `OPERATIONS` dictionary mapping operation names to `operator` functions. Two pattern lists — `SIMPLE_OPERATIONS` and `COMPOUND_OPERATIONS` — are derived from it. The 12 branches collapsed into two evaluation functions and one shared `find_operation` pattern matcher.

Before:
```
if ' plus the result of ' in expression:
    parts = expression.split(' plus the result of ')
    left = evaluate_expression(parts[0])
    right = evaluate_expression(parts[1])
    return left + right
elif ', plus the result of ' in expression:
    ...  # same thing, 6 more times
```

After:
```
delimiter, op_func = find_operation(expression, COMPOUND_OPERATIONS)
if delimiter:
    return evaluate_compound_operation(expression, delimiter, op_func)
```

### Renaming to domain language

- `processor.py` → `calculator.py` (domain name, not implementation role)
- `utils.py` → `number_words.py` (says what it contains)
- `process` → `calculate`, `calc_simple` → `evaluate_simple_operation`, `calc_nested` → `evaluate_compound_operation`
- Parameters renamed from implementation terms (`line`) to domain terms (`expression`)
- Dead scaffolding file `main.py` deleted

### Error handling

- `apply_comma_precedence` silently returned `None` on unrecognized operators, causing a confusing `TypeError` downstream. Now raises `ValueError` with a domain-language message.
- `parse_number` leaked Python's `int()` error (`"invalid literal for int() with base 10"`) to callers. Now raises `ValueError("Unknown number: '...'")`.
- `main()` had generic `"Error"` messages. Replaced with context-specific messages: `"Could not read"`, `"Invalid expression"`, `"Could not write"`.

### Test organization

- Aligned test file boundaries with module boundaries: extracted `TestParseNumber` from `test_calculator.py` into `test_number_words.py`
- Removed `TestCompleteExamples` that duplicated individually tested cases
- Folded `TestEdgeCases` into `TestCalculate` — it was named by exclusion, not by what it tested
- Replaced hand-rolled temp directory fixture with pytest's built-in `tmp_path`
- Tests import `output_filepath` instead of re-deriving the path computation
- Replaced mock-based write error test with real filesystem permissions (`os.chmod`)

### Structural cleanup

- Narrative ordering: entry points (`calculate`, `main`) at the top of their files, helpers below
- Inlined `RESULT_PREFIX` constant — used once where the literal `'the result of '` is self-evident
- PEP 8 formatting: blank lines between top-level definitions, import ordering


## Current problems

- `output_filepath` uses `str.replace('.txt', '_results.txt')` which breaks if the path contains `.txt` elsewhere (e.g., `data.txt.bak/input.txt`)
- Division by zero is unhandled — `calculate('five divided by zero')` raises an uncontrolled `ZeroDivisionError`
- The string-splitting parser is fragile: `split(' plus ')` would misparse an expression containing a word like "surplus" if number words were extended
- All three test files use `sys.path.insert` to find the `src` directory — a workaround for missing package structure


## Future improvements

- Use `pathlib` for file path manipulation — `Path.stem` and `Path.with_stem()` would make output naming robust
- Add a proper Python package with `__init__.py` so tests can import without `sys.path` hacking
- Handle division by zero with a clear error message
- Support numbers beyond zero-ten (eleven through twenty, hundred, thousand, etc.)
- Consider a recursive descent parser if the expression grammar grows — string splitting becomes increasingly fragile with more operators or nesting levels
