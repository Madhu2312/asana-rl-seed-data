import uuid
import random

TAGS = [
    "urgent",
    "backend",
    "frontend",
    "bug",
    "review",
    "design",
    "marketing",
    "documentation",
    "testing"
]

def generate_tags(conn):
    cursor = conn.cursor()

    # Insert tags
    tag_ids = {}
    for tag in TAGS:
        tag_id = str(uuid.uuid4())
        tag_ids[tag] = tag_id
        cursor.execute(
            "INSERT INTO tags (tag_id, name) VALUES (?, ?)",
            (tag_id, tag)
        )

    # Fetch tasks
    tasks = cursor.execute(
        "SELECT task_id FROM tasks"
    ).fetchall()

    # Assign tags to tasks
    for (task_id,) in tasks:
        if random.random() < 0.7:  # Most tasks have tags
            selected = random.sample(
                list(tag_ids.values()),
                random.randint(1, 3)
            )
            for tag_id in selected:
                cursor.execute(
                    "INSERT INTO task_tags (task_id, tag_id) VALUES (?, ?)",
                    (task_id, tag_id)
                )

    conn.commit()
