from src.models.projects import CreateProject, Project
from src.database import fetch_query, execute_query

def create_project(project: CreateProject):
    query = """
    INSERT INTO projects (name, description) VALUES (%s, %s) RETURNING id;
    """
    project_id = execute_query(query, (project.name, project.description))
    return project_id

def add_user_to_project(project_id):
    query = """
    INSERT INTO project_users (project_id) VALUES (%s);
    """
    execute_query(query, (project_id))

def update_project(project_id, new_data):
    query = """
    UPDATE projects
    SET 
        name = COALESCE(%s, name),
        description = COALESCE(%s, description),
        updated_at = NOW()
    WHERE id = %s ;
    """
    params = (new_data['name'], new_data['description'], project_id)
    execute_query(query, params)

def delete_project(project_id):
    query = """
    DELETE FROM projects
    WHERE id = %s ;
    """
    params = (project_id,)
    execute_query(query, params)