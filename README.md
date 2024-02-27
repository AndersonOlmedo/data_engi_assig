# Duplicate Checker

A utility to count and sample duplicate rows in a pandas DataFrame based on specified columns.

## Installation

To set up a virtual environment and install dependencies, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```python
import pandas as pd
from duplicate_checker.duplicate_checker import count_and_sample_duplicates_by_columns


df_1 = pd.DataFrame(
    data=[
        ['A','a', 'x', 1],
        ['A','b', 'x', 1],
        ['A','c', 'x', 1],
        ['B','a', 'x', 1],
        ['B','b', 'x', 1],
        ['B','c', 'x', 1],
        ['A','a', 'y', 1],
    ],
    columns=['col_1', 'col_2', 'col_3', 'col_4']
)

# Example usage
print("Checking for duplicates on ['col_1']:")
print(count_and_sample_duplicates_by_columns(df_1, ['col_1']))

print("\nChecking for duplicates on ['col_1', 'col_2']:")
print(count_and_sample_duplicates_by_columns(df_1, ['col_1', 'col_2']))

print("\nChecking for duplicates on ['col_1', 'col_2', 'col_3']:")
print(count_and_sample_duplicates_by_columns(df_1, ['col_1', 'col_2', 'col_3']))
```


## Running Tests

Execute the tests with:

```bash
python -m unittest
```