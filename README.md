# Monitor — File System Watcher

A small CLI utility that watches a directory for file system events and appends a timestamped log to a tab-separated CSV file. Useful for lightweight ops/auditing (seeing what changed and when) and for build/release workflows.

## Features
- Watches a chosen directory for **create**, **modify**, **delete**, and **move** events.
- Logs each event as a row in `logger/logger.csv` (tab-separated).
- Uppercases the action and truncates a leading `./` from paths for readability.
- Clean shutdown with `Ctrl-C` (SIGINT).

> **Current scope**
> - Non-recursive (subdirectories are **not** watched).  
> - `move` logs the **source** path only.  
> - `logger/` folder must exist before running.

## Requirements
- Python 3.8+
- Packages: `watchdog`

Install dependencies:
```bash
pip install watchdog
