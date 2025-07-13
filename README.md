

A command-line tool to fetch PubMed research papers with at least one **non-academic (pharmaceutical or biotech)** author and export the results to a CSV file.

---

## Project Structure

aganitha\_papers/
├── pyproject.toml               # Poetry configuration
├── poetry.lock                  # Dependency lock file
├── README.md                    # This file
└── src/
└── aganitha\_papers/
├── scripts/
│   └── get\_papers\_list.py     # CLI entry point
└── get\_papers/
├── **init**.py
├── fetch.py              # Fetches PubMed data using Entrez
├── filter.py             # Parses and filters non-academic authors
├── export.py             # CSV export and print formatter
├── utils.py              # Shared utilities (debug printing)
└── tests/
└── test\_basic.py         # Pytest unit tests



---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/aganitha-papers.git
cd aganitha-papers
````

### 2. Install dependencies using Poetry

Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

```bash
poetry install
```

### 3. Run the CLI tool

```bash
poetry run get-papers-list "covid vaccine"
```

---

## Command-Line Options

| Option      | Description                        |
| ----------- | ---------------------------------- |
| `QUERY`     | (required) The PubMed search query |
| `-f <file>` | Save output to CSV file            |
| `-d`        | Enable debug output                |
| `--help`    | Show usage instructions            |

### Examples:

```bash
# Print results to console
poetry run get-papers-list "covid vaccine"

# Save to CSV file
poetry run get-papers-list "covid vaccine" -f results.csv

# Debug mode
poetry run get-papers-list "covid vaccine" -d
```

---

## Features

* Fetches papers via **PubMed E-utilities API**
* Filters only papers with **at least one non-academic author**
* Supports `--file` to export results as `.csv`
* Clean and pretty console output using `pprint`
* Typed Python & modular structure
* Tested with **pytest**

---

## How Non-Academic Authors Are Detected

We consider affiliations **non-academic** if:

* They contain terms like: `pharma`, `biotech`, `inc`, `ltd`, `therapeutics`, `llc`
* And **do not** contain terms like: `university`, `hospital`, `institute`, `school`, etc.

---

## Tools Used

| Tool                                                    | Purpose                                   |
| ------------------------------------------------------- | ----------------------------------------- |
| [Poetry](https://python-poetry.org/)                    | Dependency management & packaging         |
| [Click](https://click.palletsprojects.com/)             | Command-line interface                    |
| [Requests](https://docs.python-requests.org/)           | API calls to PubMed                       |
| [pprint](https://docs.python.org/3/library/pprint.html) | Pretty console output                     |
| [pytest](https://docs.pytest.org/)                      | Unit testing                              |
| [ChatGPT](https://chat.openai.com/)                     | Helped resolve bugs and errors during dev |

---

## 🤖 LLM Usage (Required)

I used ChatGPT to:

* Plan the project structure
* Debug errors with Poetry and CLI
* Fix import path/module errors
* Write regex & XML parsing logic
* Generate test cases and debug `__pycache__`/module conflicts

👉 [See my full ChatGPT conversation here]([https://chat.openai.com/share/your-thread-link](https://chatgpt.com/share/6874242a-5a0c-800a-8730-517ef9dd1e09))

---

## 📝 Author

**Aditya Saxena**
`saxena.aditya.2807@gmail.com`

