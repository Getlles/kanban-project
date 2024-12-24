from src.models.projects import Project
from src.database import fetch_query, execute_query
from typing import List

def get_projects_by_user(user_id: int) -> List[Project]:
    query = """
    SELECT p.id, p.name, p.description, p.created_at, p.updated_at
    FROM projects p
    JOIN project_users pu ON p.id = pu.project_id
    WHERE pu.user_id = %s;
    """
    rows = fetch_query(query, (user_id,))
    return [Project(id=row[0], name=row[1], description=row[2], created_at=row[3], updated_at=row[4]) for row in rows]

def add_user_to_project(project_id, user_id):
    query = """
    INSERT INTO project_users (project_id, user_id) VALUES (%s, %s);
    """
    execute_query(query, (project_id, user_id))

def delete_user_from_project(user_id, project_id):
    query = """
    DELETE FROM project_users
    WHERE user_id = %s AND project_id = %s;
    """
    execute_query(query, (user_id, project_id))