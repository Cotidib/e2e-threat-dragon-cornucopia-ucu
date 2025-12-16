# E2E Tests

End-to-end automated testing project

## Description


## Technologies and Frameworks

- **Python 3.12+**: Base programming language
- **Playwright**: Web browser automation framework
- **Behave**: BDD framework for writing tests in natural language (Gherkin)
- **Pytest**: Additional testing framework

## Project Structure

```
pruebas_e2e/
|
├── features/              # BDD feature files
│   └── steps/            # Behave step implementations
├── pages/                # Page Object Model (POM)
│   └── base_page.py      # Base class with common methods
├── environment.py        # Behave hooks configuration
├── behave.ini           # Behave configuration
└── requirements.txt     # Project dependencies
```

### Page Object Model (POM) Pattern

The project uses the POM pattern to keep code organized and maintainable:

- **BasePage**: Base class containing common methods (click, search, take_screenshot, etc.)

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

4. Run threat-dragon-cornucopia project locally
For windows:
```bash
 npm run dev:server
 npm run dev:vue
 ```
 For linux:
 ```bash
 npm start
 ```

## Running Tests

### Run all tests

From the root directory:
```bash
behave
```

### Run a specific feature

```bash
behave features/create_model.feature
```

### Run with specific format

```bash
behave --format pretty
```

### Run in headless mode

By default, tests run in non-headless mode (you can see the browser). To run in headless mode change:
```python
context.browser = playwright.chromium.launch(headless=False)
```
to:
```python
context.browser = playwright.chromium.launch(headless=True)
```

## Configuration

### behave.ini

The `behave.ini` file contains Behave configuration:
- **format**: Output format (pretty, progress, json, etc.)
- **show_timings**: Show execution times
- **show_skipped**: Show skipped scenarios