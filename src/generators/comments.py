import uuid
import random
from datetime import timedelta, datetime
from src.utils.distributions import TASK_DISTRIBUTION

# ---------------------------------------
# SUBTASKS + COMMENTS GENERATOR
# ---------------------------------------

def generate_subtasks_and_comments(conn):
    cursor = conn.cursor()

    # Fetch tasks
    tasks = cursor.execute(
        "SELECT task_id, created_at FROM tasks"
    ).fetchall()

    # Fetch users and roles
    users = cursor.execute(
        "SELECT user_id, role FROM users"
    ).fetchall()

    user_ids = [u[0] for u in users]
    managers = [u[0] for u in users if "Manager" in u[1]]

    for task_id, created_at in tasks:

        # 🔴 CRITICAL FIX: SQLite returns strings → convert to datetime
        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at)

        # -----------------------------
        # SUBTASKS
        # -----------------------------
        if random.random() < TASK_DISTRIBUTION["subtask_rate"]:
            subtask_count = random.randint(1, 5)

            for i in range(subtask_count):
                subtask_id = str(uuid.uuid4())
                assignee_id = random.choice(user_ids)

                cursor.execute(
                    """
                    INSERT INTO subtasks (
                        subtask_id, parent_task_id, assignee_id,
                        name, completed, created_at, completed_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        subtask_id,
                        task_id,
                        assignee_id,
                        f"Subtask {i+1}",
                        random.choice([0, 1]),
                        created_at,
                        None
                    )
                )

        # -----------------------------
        # COMMENTS
        # -----------------------------
        if random.random() < TASK_DISTRIBUTION["comment_probability"]:
            comment_count = random.randint(1, 4)

            for _ in range(comment_count):
                comment_id = str(uuid.uuid4())

                # Managers comment more often
                if managers and random.random() < 0.6:
                    commenter = random.choice(managers)
                else:
                    commenter = random.choice(user_ids)

                comment_time = created_at + timedelta(
                    days=random.randint(0, 14)
                )

                cursor.execute(
                    """
                    INSERT INTO comments (
                        comment_id, task_id, user_id, content, created_at
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        comment_id,
                        task_id,
                        commenter,
                        generate_comment_text(),
                        comment_time
                    )
                )

    conn.commit()


def generate_comment_text():
    phrases = [
        "Please take a look.",
        "Any updates on this?",
        "Let's prioritize this.",
        "This is blocked right now.",
        "Reviewed and approved.",
        "Needs further discussion."
    ]
    return random.choice(phrases)
