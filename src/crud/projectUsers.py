from src.models.project_users.projectUsers import Project_users
from src.database import fetch_query, execute_query

project_users_list = []

def create_project_user(project_user: Project_users):
    query = """
    INSERT INTO project_users (project_id, user_id) VALUES (%s, %s)
    """
    execute_query(query, (project_user.project_id, project_user.user_id))

def get_project_users() -> list[Project_users]:
    query = "SELECT * FROM project_users"
    rows = fetch_query(query)
    return [Project_users(id=row[0], project_id=row[1], user_id=row[2]) for row in rows]

def delete_project_user(name, username):
    query = """
    DELETE FROM project_users
    WHERE project_id = (SELECT id FROM projects WHERE name = %s )
    AND user_id = (SELECT id FROM users WHERE username = %s );
    """
    params = (name, username)
    execute_query(query, params)