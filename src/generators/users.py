import uuid
import random
from faker import Faker
from src.utils.dates import random_past_datetime
from src.utils.distributions import TEAM_DISTRIBUTION

fake = Faker()

# ---------------------------------------
# ROLE DEFINITIONS BY DEPARTMENT
# ---------------------------------------

DEPARTMENT_ROLES = {
    "Engineering": ["Software Engineer", "Senior Engineer", "Engineering Manager"],
    "Product": ["Product Manager", "Senior Product Manager"],
    "Marketing": ["Marketing Specialist", "Growth Manager"],
    "Sales": ["Sales Executive", "Account Manager"],
    "Operations": ["Operations Analyst", "HR Manager"]
}

ROLE_WEIGHTS = {
    "Engineering Manager": 0.15,
    "Senior Engineer": 0.25,
    "Software Engineer": 0.60
}

# ---------------------------------------
# USER GENERATOR
# ---------------------------------------

def generate_users(conn, org_id):
    """
    Generate realistic users with department-aware roles.
    """
    cursor = conn.cursor()
    users = []

    for department, config in TEAM_DISTRIBUTION.items():
        team_count = config["team_count"]
        avg_min, avg_max = config["avg_size"]

        total_users = team_count * random.randint(avg_min, avg_max)

        for _ in range(total_users):
            user_id = str(uuid.uuid4())
            name = fake.name()
            email = name.lower().replace(" ", ".") + "@examplecorp.com"

            if department == "Engineering":
                role = random.choices(
                    population=["Software Engineer", "Senior Engineer", "Engineering Manager"],
                    weights=[0.6, 0.25, 0.15]
                )[0]
            else:
                role = random.choice(DEPARTMENT_ROLES[department])

            created_at = random_past_datetime()

            cursor.execute(
                """
                INSERT INTO users (user_id, org_id, full_name, email, role, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_id, org_id, name, email, role, created_at)
            )

            users.append((user_id, department))

    conn.commit()
    return users
