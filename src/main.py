from src.utils.db import get_connection
from src.generators.teams import (
    generate_organization,
    generate_teams,
    assign_users_to_teams
)
from src.generators.users import generate_users
from src.generators.projects import generate_projects
from src.generators.tasks import generate_tasks

from src.generators.comments import generate_subtasks_and_comments

def main():
    conn = get_connection()

    print("▶ Creating organization...")
    org_id = generate_organization(conn)

    print("▶ Creating teams...")
    teams = generate_teams(conn, org_id)

    print("▶ Creating users...")
    users = generate_users(conn, org_id)

    print("▶ Assigning users to teams...")
    assign_users_to_teams(conn, teams, users)

    print("▶ Creating projects and sections...")
    projects = generate_projects(conn, teams)

    print("▶ Creating tasks...")
    generate_tasks(conn, projects, users)
	
    print("▶ Creating subtasks and comments...")
    generate_subtasks_and_comments(conn)


    conn.close()
    print("✅ Organization, teams, projects, and tasks created successfully")


if __name__ == "__main__":
    main()
