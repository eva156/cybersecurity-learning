# Exercise 1: Log Processing

## Objective
Process a list of usernames extracted from simplified authentication logs to identify unique users and calculate basic login statistics.

This exercise uses a simplified dataset rather than reading an actual log file. The aim is to practise using Python lists and sets to process and analyse data, while developing good coding practices.

This is mostly just a brief revision of concepts. 

## Requirements
The program must:
- Take a list of usernames that may contain duplicates as input.
- Process the list to produce a collection of unique usernames.
- Calculate the total number of login attempts recorded.
- Calculate the number of unique users who attempted to log in. 
- Display the results in a clear, readable format.

Additional data-cleaning requirements:
- Remove leading and trailing whitespace from usernames.
- Exclude empty or whitespace-only usernames from the collection of unique users.

Note: All entries in the original list are counted as login attempts, including entries with empty usernames. Only valid, non-empty usernames are included in the unique-user count.

### Example input
```bash
usernames = [
    "alice",
    "bob",
    "alice",
    "charlie",
    "bob",
    "alice",
    "david"
]
```
### Expected output
```bash
Total login attempts: 7
Unique users: 4
Unique usernames: {'alice', 'bob', 'charlie', 'david'}
```

## Approach
The solution is divided into several functions, each responsible for a specific task
- `get_sample_data()`: provides sample list of usernames
- `get_unique_usernames()`: uses a set comprehension to remove duplicates, strips whitespace and excludes empty usernames
- `get_login_statistics()`: calculates the total number of login attempts and unique users, returning the results in a dictionary
- `display_results()`: displays the calculated statistics

## Data Structures and Techniques
- Lists: Store the original usernames and preserve duplicate entries
- Sets: Identify unique usernames and eliminate duplicates
- Dictionaries: Store the calculate login statistics using descriptive keys
- Set comprehension: provide a concise way to clean usernames and create a set of unqiue values
- Built-in functions: use `len()` to caluclate no. of login attempts, and `strip()` to remove whitespase

## Code Organisation
The prgram follows the principle of separation of concerns by dividing functionality into small, resusable functions.

Type hints and docstrings are included to improve readability and maintainability. A `main()` function and and `if __name__ == __"main__"` entry point are used to control program execution. 

## How to Run
Ensure Python 3.9 or later is installed
Navigate to the exrcise directory and run
```bash
python main.py
```

### Running Tests
Unit tests are implemented using Python's built-in `unittest` framework.

Run the tests directly from the exercise directory using:
```bash
python -m unittest -v
```

The tests cover:
- Duplicate username removal.
- Empty input.
- Lists containing only unique usernames.
- Correct calculation of login statistics.
- Statistics for empty input.
- Leading and trailing whitespace handling.
- Empty and whitespace-only usernames.

## Concepts Revised
- Using lists and sets to process and analyse data.
- Understanding the difference between total entries and unique values.
- Using set comprehensions and built-in Python functions.
- Structuring programs using small, reusable functions.
- Writing unit tests using unittest and the Arrange–Act–Assert pattern.
- Handling edge cases and cleaning input data.
- Using type hints and docstrings to improve code readability.

## Possible Improvements
- Read usernames directly from an authentication log file rather than using hardcoded sample data.
- Extend the program to analyse additional authentication information, such as IP addresses and login timestamps.
- Add input validation and more robust error handling.
