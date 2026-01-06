import uuid
import random
from src.utils.dates import (
    random_past_datetime,
    generate_due_date,
    generate_completion_timestamp
)
from src.utils.distributions import PROJECT_TYPES, TASK_DISTRIBUTION

# ---------------------------------------
# TASK GENERATOR
# ---------------------------------------

def generate_tasks(conn, projects, users):
    """
    Generate realistic tasks per project.
    Task volume, completion, and deadlines depend on project type.
    """
    cursor = conn.cursor()

    user_ids = [u[0] for u in users]

    for project_id, project_type, section_ids in projects:
        config = PROJECT_TYPES[project_type]

        min_tasks, max_tasks = config["avg_tasks"]
        task_count = random.randint(min_tasks, max_tasks)

        completion_low, completion_high = config["completion_rate"]
        completion_rate = random.uniform(completion_low, completion_high)

        for _ in range(task_count):
            task_id = str(uuid.uuid4())
            section_id = random.choice(section_ids)

            created_at = random_past_datetime()
            due_date = generate_due_date(created_at)

            completed = random.random() < completion_rate
            completed_at = (
                generate_completion_timestamp(created_at, due_date)
                if completed else None
            )

            assignee_id = (
                None
                if random.random() < TASK_DISTRIBUTION["unassigned_rate"]
                else random.choice(user_ids)
            )

            name = generate_task_name(project_type)

            cursor.execute(
                """
                INSERT INTO tasks (
                    task_id, project_id, section_id, assignee_id,
                    name, description, due_date,
                    completed, created_at, completed_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task_id,
                    project_id,
                    section_id,
                    assignee_id,
                    name,
                    None,
                    due_date,
                    completed,
                    created_at,
                    completed_at
                )
            )

    conn.commit()


# ---------------------------------------
# TASK NAMING LOGIC
# ---------------------------------------

def generate_task_name(project_type):
    if project_type == "Engineering Sprint":
        return f"Implement feature {random.randint(100,999)}"
    if project_type == "Bug Tracking":
        return f"Fix bug #{random.randint(1000,9999)}"
    if project_type == "Marketing Campaign":
        return f"Prepare asset {random.randint(1,50)}"
    if project_type == "Operations":
        return f"Review process {random.randint(1,20)}"
    return "General task"
