# Failed Login Log Analyzer

## Project Objective
This project is a Python security automation script that analyzes a sample log file for failed login attempts. The goal is to make log review faster by finding failed SSH login attempts, counting them by IP address, and showing a simple summary.

## Features
- Reads a sample log file
- Detects failed login attempts
- Extracts IP addresses from failed login lines
- Counts how many failed attempts came from each IP address
- Displays a simple summary report
- Shows an alert when an IP address has 3 or more failed attempts

## Files
- `login_analyzer.py` - Python script that analyzes the log file
- `sample.log` - Sample log file used for testing

## How to Run
1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run this command:

```bash
python3 login_analyzer.py