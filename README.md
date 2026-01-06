\# Asana RL Seed Data Generator



This repository contains a \*\*realistic, behavior-driven seed data generator\*\* for simulating an enterprise-scale Asana workspace.  

The generated dataset is designed for \*\*reinforcement learning environments\*\* that evaluate computer-use AI agents on real project management workflows.



The goal is \*\*not\*\* to generate random synthetic data, but to create \*\*distributionally realistic, temporally consistent, and relationally coherent\*\* Asana-like data suitable for model training and evaluation.



---



\## Key Design Principles



\- \*\*Behavioral realism over randomness\*\*  

&nbsp; Task volumes, completion rates, deadlines, and discussion patterns vary by project type and team function.



\- \*\*Enterprise-scale structure\*\*  

&nbsp; Simulates a B2B SaaS organization with thousands of users, hundreds of teams, and thousands of projects.



\- \*\*Temporal consistency\*\*  

&nbsp; All timestamps respect causal ordering (creation → due date → completion → comments → attachments).



\- \*\*Relational integrity\*\*  

&nbsp; Strict foreign-key relationships ensure realistic organizational structure and workflows.



---



\## What This Generates



\- 1 organization

\- ~200 teams across Engineering, Product, Marketing, Sales, and Operations

\- Thousands of users with department-aware roles

\- ~1,000 projects with workflow-specific sections

\- ~40k+ tasks with realistic deadlines and completion behavior

\- ~45k+ subtasks

\- ~50k+ comments with manager-heavy discussion patterns

\- Attachments metadata (file type, uploader, timestamp)

\- Semantic tags with many-to-many task mappings

\- Structured custom fields and per-task field values



All data is stored in a single \*\*SQLite database\*\*.



---



\## Extended Metadata Support



The dataset includes additional metadata tables to more closely model real-world task management systems:



\- Tags and task–tag mappings for semantic task categorization

\- Custom fields and values for structured task attributes (e.g., priority, effort)

\- Attachments metadata capturing file type, uploader, and timestamp



All metadata is generated deterministically using scripted generators, ensuring reproducibility while providing rich contextual signals for downstream reinforcement learning and LLM-based agents.



---



\## How to Run



\### 1. Set up the environment

```bash

python -m venv venv

venv\\Scripts\\activate    # Windows

pip install -r requirements.txt



