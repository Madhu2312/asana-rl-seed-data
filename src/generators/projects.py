import uuid
import random
from src.utils.dates import random_past_datetime
from src.utils.distributions import PROJECT_TYPES

# ---------------------------------------
# PROJECT GENERATOR
# ---------------------------------------

def generate_projects(conn, teams):
    """
    Generate projects per team with behavior-driven project types.
    """
    cursor = conn.cursor()
    projects = []

    for team_id, department in teams:
        # Each team runs multiple projects
        project_count = random.randint(3, 8)

        for _ in range(project_count):
            project_type = random.choice(list(PROJECT_TYPES.keys()))
            project_id = str(uuid.uuid4())

            name = generate_project_name(project_type, department)
            created_at = random_past_datetime()

            cursor.execute(
                """
                INSERT INTO projects (project_id, team_id, name, project_type, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (project_id, team_id, name, project_type, created_at)
            )

            sections = create_sections(cursor, project_id, project_type)
            projects.append((project_id, project_type, sections))

    conn.commit()
    return projects


# ---------------------------------------
# PROJECT NAME LOGIC
# ---------------------------------------

def generate_project_name(project_type, department):
    if project_type == "Engineering Sprint":
        return f"{department} Sprint {random.randint(10, 99)}"
    if project_type == "Bug Tracking":
        return f"{department} Bug Tracker"
    if project_type == "Marketing Campaign":
        return f"Campaign Q{random.randint(1,4)} Launch"
    if project_type == "Operations":
        return f"{department} Ops Backlog"
    return "General Project"


# ---------------------------------------
# SECTION GENERATOR
# ---------------------------------------

def create_sections(cursor, project_id, project_type):
    sections = PROJECT_TYPES[project_type]["sections"]
    section_ids = []

    for idx, section_name in enumerate(sections):
        section_id = str(uuid.uuid4())
        cursor.execute(
            """
            INSERT INTO sections (section_id, project_id, name, position)
            VALUES (?, ?, ?, ?)
            """,
            (section_id, project_id, section_name, idx)
        )
        section_ids.append(section_id)

    return section_ids
