import uuid
import random
from datetime import datetime, timedelta

FILE_TYPES = ["pdf", "png", "docx", "xlsx"]

def generate_attachments(conn):
    cursor = conn.cursor()

    tasks = cursor.execute(
        "SELECT task_id FROM tasks"
    ).fetchall()

    users = cursor.execute(
        "SELECT user_id FROM users"
    ).fetchall()

    user_ids = [u[0] for u in users]

    for (task_id,) in tasks:
        # Only some tasks have attachments
        if random.random() < 0.2:
            attachment_id = str(uuid.uuid4())
            uploaded_by = random.choice(user_ids)
            uploaded_at = (
                datetime.now() - timedelta(days=random.randint(0, 30))
            ).isoformat()

            cursor.execute(
                """
                INSERT INTO attachments (
                    attachment_id,
                    task_id,
                    file_type,
                    uploaded_by,
                    uploaded_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    attachment_id,
                    task_id,
                    random.choice(FILE_TYPES),
                    uploaded_by,
                    uploaded_at
                )
            )

    conn.commit()
