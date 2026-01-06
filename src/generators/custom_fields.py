import uuid
import random

CUSTOM_FIELDS = [
    ("priority", "enum", ["low", "medium", "high"]),
    ("effort", "integer", ["1", "2", "3", "4", "5"]),
    ("sprint", "string", ["Sprint-1", "Sprint-2", "Sprint-3"])
]

def generate_custom_fields(conn):
    cursor = conn.cursor()

    # Insert custom field definitions
    field_ids = {}
    for name, field_type, values in CUSTOM_FIELDS:
        field_id = str(uuid.uuid4())
        field_ids[name] = (field_id, values)
        cursor.execute(
            """
            INSERT INTO custom_field_definitions (field_id, name, field_type)
            VALUES (?, ?, ?)
            """,
            (field_id, name, field_type)
        )

    # Fetch tasks
    tasks = cursor.execute(
        "SELECT task_id FROM tasks"
    ).fetchall()

    # Assign custom field values to some tasks
    for (task_id,) in tasks:
        if random.random() < 0.3:  # Only some tasks have custom fields
            for field_name, (field_id, values) in field_ids.items():
                if random.random() < 0.7:
                    value_id = str(uuid.uuid4())
                    cursor.execute(
                        """
                        INSERT INTO custom_field_values
                        (value_id, task_id, field_id, value)
                        VALUES (?, ?, ?, ?)
                        """,
                        (
                            value_id,
                            task_id,
                            field_id,
                            random.choice(values)
                        )
                    )

    conn.commit()
