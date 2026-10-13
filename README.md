# Python Learning Journey & Projects

A record of how my Python work has developed—from small programming exercises to modular command-line tools and a larger academic analytics application.

I am a student developer interested in using software to solve practical problems, especially problems involving data, analysis, and education. This repository keeps both my early learning exercises and the projects I built as I learned to organize larger programs.

## Featured work

| Project | What it does | Tools | Status |
| --- | --- | --- | --- |
| [Bangladesh Academic Analytics System](academics_analytics_system/) | Explores student records, academic trends, and performance insights through Python and a Flask interface. | Python, Flask, JSON | **In active development** |
| [Student Performance Tracker](day13_Mini_Projects/student-performance-tracker/) | Manages student records, analyzes rankings and class performance, generates charts, and exports a leaderboard. | Python, JSON, Matplotlib, CSV | Educational CLI project |
| [Expense Tracker CLI](day13_Mini_Projects/expense-tracker-cli/) | Records expenses locally, filters entries, and summarizes spending by category. | Python, JSON | Educational CLI project |

> **Development note:** The published Academic Analytics System is a GitHub snapshot. Development continues separately, so this repository may not yet reflect the latest local work. Its code and documentation have deliberately been left unchanged during the portfolio documentation update.

## Explore the smaller projects

### Student Performance Tracker

A menu-driven terminal program for recording student marks and turning them into class-level summaries. It includes section comparisons, pass/fail analysis, grade-distribution charts, and CSV leaderboard export.

[Read the project documentation →](day13_Mini_Projects/student-performance-tracker/README.MD)

![Student Performance Tracker demonstration](day13_Mini_Projects/student-performance-tracker/Demo/Demo_project.gif)

### Expense Tracker CLI

A local expense-management tool built to practice modular Python design. It separates the command-line interface, expense operations, JSON storage, and analytics.

[Read the project documentation →](day13_Mini_Projects/expense-tracker-cli/README.md)

![Expense Tracker category analysis](day13_Mini_Projects/expense-tracker-cli/assets/analytics.png)

## Python fundamentals archive

The `day01_*` through `day12_*` folders are a learning archive, not polished standalone applications. They contain exercises in topics including:

- Basic Python syntax, conditionals, loops, functions, collections, and strings
- File operations and structured data (CSV and JSON)
- Recursion and progressively more involved problem-solving exercises

The progression into larger CLI applications is collected under [`day13_Mini_Projects/`](day13_Mini_Projects/).

I have kept the earlier exercises because they show the process of learning, experimenting, and gradually writing more structured code.

## Run a project

Clone this repository:

```bash
git clone https://github.com/Rafidabd/python-phase-1.git
cd python-phase-1
```

**Expense Tracker** — run from the **repository root** (its current storage path is relative to that directory):

```bash
python day13_Mini_Projects/expense-tracker-cli/main.py
```

**Student Performance Tracker** — first enter its project directory so its data and report paths resolve correctly:

```bash
cd day13_Mini_Projects/student-performance-tracker
python -m pip install -r requirements.txt
python main.py
```

For full features, screenshots, and usage details, follow the individual project READMEs above. These are learning projects, not production-hosted services.

## About the repository

My approach has been to build on what I learned in each exercise: first getting a program to work, then thinking about reusable modules, data storage, input validation, analysis, and how other people can understand the result.

The academic analytics project is an ongoing step in that progression. I will document its up-to-date architecture and development status when the next stable milestone is ready.
