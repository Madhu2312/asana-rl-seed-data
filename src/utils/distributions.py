"""
Centralized behavioral distributions for Asana simulation.
All generators must reference this file.
This is intentional to enforce realism and consistency.
"""

# -------------------------------
# ORGANIZATION LEVEL
# -------------------------------

ORG_CONFIG = {
    "employee_count": 7500,
    "history_days": 180
}

# -------------------------------
# TEAM DISTRIBUTIONS
# -------------------------------

TEAM_DISTRIBUTION = {
    "Engineering": {
        "team_count": 90,
        "avg_size": (8, 12)
    },
    "Product": {
        "team_count": 25,
        "avg_size": (6, 10)
    },
    "Marketing": {
        "team_count": 30,
        "avg_size": (5, 9)
    },
    "Sales": {
        "team_count": 25,
        "avg_size": (6, 12)
    },
    "Operations": {
        "team_count": 30,
        "avg_size": (5, 10)
    }
}

# -------------------------------
# PROJECT BEHAVIOR
# -------------------------------

PROJECT_TYPES = {
    "Engineering Sprint": {
        "sections": ["Backlog", "In Progress", "Code Review", "Done"],
        "completion_rate": (0.7, 0.85),
        "avg_tasks": (40, 80)
    },
    "Bug Tracking": {
        "sections": ["Open", "Investigating", "Fixing", "Closed"],
        "completion_rate": (0.6, 0.7),
        "avg_tasks": (30, 60)
    },
    "Marketing Campaign": {
        "sections": ["Ideas", "Design", "Execution", "Launched"],
        "completion_rate": (0.5, 0.65),
        "avg_tasks": (20, 40)
    },
    "Operations": {
        "sections": ["To Do", "In Progress", "Blocked", "Done"],
        "completion_rate": (0.4, 0.55),
        "avg_tasks": (15, 30)
    }
}

# -------------------------------
# TASK BEHAVIOR
# -------------------------------

TASK_DISTRIBUTION = {
    "unassigned_rate": 0.15,
    "no_due_date_rate": 0.10,
    "overdue_rate": 0.05,
    "subtask_rate": 0.35,
    "comment_probability": 0.45
}

# -------------------------------
# TEMPORAL BEHAVIOR
# -------------------------------

TIME_BEHAVIOR = {
    "weekday_weight": {
        "Mon": 1.3,
        "Tue": 1.3,
        "Wed": 1.2,
        "Thu": 0.8,
        "Fri": 0.6
    },
    "avoid_weekends": 0.85
}
