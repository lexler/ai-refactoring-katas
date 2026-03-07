# Natural Language Calculator - Refactoring Exercise

A refactoring kata using a natural language calculator as the subject code.

See [REFACTORING_EXERCISE.md](REFACTORING_EXERCISE.md) for the exercise instructions.

## Setup

This project uses [devenv](https://devenv.sh) to manage development dependencies (Python, tools, etc.) and [direnv](https://direnv.net) to automatically activate the environment when you `cd` into the project.

### Prerequisites

1. **Install Nix** (package manager):
   https://nixos.org/download

2. **Install devenv**:
   https://devenv.sh/getting-started/

3. **Install direnv**:
   https://direnv.net/docs/installation.html

### Activating the environment

Once the prerequisites are installed:

```bash
# Allow direnv to activate the environment for this project
direnv allow
```

This will automatically install and make available:
- Python 3.12
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- [bat](https://github.com/sharkdp/bat) (syntax-highlighted file viewer)
- [viddy](https://github.com/sachaos/viddy) (modern watch command)
- [yaks](https://github.com/mattwynne/yaks) (yak shaving tracker)
- [pi](https://github.com/numtide/llm-agents.nix) (AI coding agent)

Alternatively, you can activate the environment manually:

```bash
devenv shell
```

## Running the Program

```bash
cd src
python natural_language_calculator.py sample_expressions.txt
```

This will create a file called `sample_expressions_results.txt` with the calculated results.

## Running the Tests

```bash
# Run all tests
python -m unittest discover -v

# Run just unit tests
python -m unittest tests.test_calculator -v
```
