# Python Mini Projects

These two command-line projects mark my transition from individual Python exercises to programs with separate modules, persistent data, and user-facing features.

| Project | Focus | Demo / screenshots |
| --- | --- | --- |
| [Expense Tracker CLI](expense-tracker-cli/) | Local expense records, input validation, JSON storage, and spending summaries | [Menu](expense-tracker-cli/assets/menu.png) · [Category analysis](expense-tracker-cli/assets/analytics.png) |
| [Student Performance Tracker](student-performance-tracker/) | Student records, rankings, class statistics, visualizations, and CSV exports | [Animated demo](student-performance-tracker/Demo/Demo_project.gif) · [Example charts](student-performance-tracker/Reports/) |

## How to explore

### Expense Tracker CLI

From the **root of `python-phase-1`**, run:

```bash
python day13_Mini_Projects/expense-tracker-cli/main.py
```

The current expense storage location is resolved relative to the repository root. See the [Expense Tracker README](expense-tracker-cli/README.md) for features and examples.

### Student Performance Tracker

From the **root of `python-phase-1`**, run:

```bash
cd day13_Mini_Projects/student-performance-tracker
python -m pip install -r requirements.txt
python main.py
```

See the [Student Performance Tracker README](student-performance-tracker/README.MD) for chart examples and configuration details.

## Why these projects matter to me

Both started as Python learning exercises. I used them to practice breaking a program into manageable parts, keeping data between sessions, validating input, and providing useful output rather than only writing isolated scripts.

They are intentionally documented as educational projects. The larger [Academic Analytics System](../academics_analytics_system/) is a separate, ongoing development effort.
