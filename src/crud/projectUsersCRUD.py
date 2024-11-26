from src.models.projectUsersModel import Project_users
from src.database import fetch_query, execute_query

project_users_list = []

def create_Project_user(project_user: Project_users):
    query = """
    INSERT INTO project_users (project_id, user_id) VALUES (%s, %s)
    """
    execute_query(query, (project_user.project_id, project_user.user_id))

def get_project_users() -> list[Project_users]:
    query = "SELECT id, project_id, user_id FROM project_users"
    rows = fetch_query(query)
    return [Project_users(id=row[0], project_id=row[1], user_id=row[2]) for row in rows]

def delete_project_user(project_user_id):
    query = """
    DELETE FROM project_users
    WHERE id = %s
    """
    params = (project_user_id)
    execute_query(query, params)