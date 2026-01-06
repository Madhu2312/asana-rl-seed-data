import uuid
from src.utils.dates import random_past_datetime
from src.utils.distributions import TEAM_DISTRIBUTION

# ---------------------------------------
# ORGANIZATION GENERATOR
# ---------------------------------------

def generate_organization(conn):
    cursor = conn.cursor()

    org_id = str(uuid.uuid4())
    org_name = "ExampleCorp Technologies"
    created_at = random_past_datetime()

    cursor.execute(
        """
        INSERT INTO organizations (org_id, name, created_at)
        VALUES (?, ?, ?)
        """,
        (org_id, org_name, created_at)
    )

    conn.commit()
    return org_id


# ---------------------------------------
# TEAM GENERATOR
# ---------------------------------------

def generate_teams(conn, org_id):
    cursor = conn.cursor()
    teams = []

    for department, config in TEAM_DISTRIBUTION.items():
        for i in range(1, config["team_count"] + 1):
            team_id = str(uuid.uuid4())
            team_name = f"{department} Team {i}"

            cursor.execute(
                """
                INSERT INTO teams (team_id, org_id, name)
                VALUES (?, ?, ?)
                """,
                (team_id, org_id, team_name)
            )

            teams.append((team_id, department))

    conn.commit()
    return teams



import random
from src.utils.distributions import TEAM_DISTRIBUTION

# ---------------------------------------
# TEAM MEMBERSHIP ASSIGNMENT
# ---------------------------------------

def assign_users_to_teams(conn, teams, users):
    """
    Assign users to teams based on department.
    Each user is assigned to exactly one team.
    """
    cursor = conn.cursor()

    # Group users by department
    users_by_dept = {}
    for user_id, department in users:
        users_by_dept.setdefault(department, []).append(user_id)

    for department, config in TEAM_DISTRIBUTION.items():
        dept_users = users_by_dept.get(department, [])
        dept_teams = [t for t in teams if t[1] == department]

        random.shuffle(dept_users)

        min_size, max_size = config["avg_size"]
        team_index = 0

        for user_id in dept_users:
            team_id, _ = dept_teams[team_index]

            cursor.execute(
                """
                INSERT INTO team_memberships (team_id, user_id)
                VALUES (?, ?)
                """,
                (team_id, user_id)
            )

            # Move to next team after reaching max size
            if cursor.execute(
                "SELECT COUNT(*) FROM team_memberships WHERE team_id = ?",
                (team_id,)
            ).fetchone()[0] >= random.randint(min_size, max_size):
                team_index = (team_index + 1) % len(dept_teams)

    conn.commit()
