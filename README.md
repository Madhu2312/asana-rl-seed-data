\# Asana RL Seed Data Generator



This repository contains a \*\*realistic, behavior-driven seed data generator\*\* for simulating an enterprise-scale Asana workspace.  

The generated dataset is designed for \*\*reinforcement learning environments\*\* that evaluate computer-use AI agents on real project management workflows.



The goal is \*\*not\*\* to generate random synthetic data, but to create \*\*distributionally realistic, temporally consistent, and relationally coherent\*\* Asana-like data suitable for model training and evaluation.



---



\##  Key Design Principles



\- \*\*Behavioral realism over randomness\*\*  

&nbsp; Task volumes, completion rates, deadlines, and discussion patterns vary by project type and team function.



\- \*\*Enterprise-scale structure\*\*  

&nbsp; Simulates a B2B SaaS organization with thousands of users, hundreds of teams, and thousands of projects.



\- \*\*Temporal consistency\*\*  

&nbsp; All timestamps respect causal ordering (creation → due date → completion → comments).



\- \*\*Relational integrity\*\*  

&nbsp; Strict foreign-key relationships ensure realistic organizational structure and workflows.



---



\##  What This Generates



\- 1 organization

\- ~200 teams across Engineering, Product, Marketing, Sales, and Operations

\- Thousands of users with department-aware roles

\- ~1,000 projects with workflow-specific sections

\- ~40k+ tasks with realistic deadlines and completion behavior

\- ~130k+ subtasks

\- ~140k+ comments with manager-heavy discussion patterns



All data is stored in a single \*\*SQLite database\*\*.



---



\##  How to Run



\### 1. Setup environment

```bash

python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate

pip install -r requirements.txt



