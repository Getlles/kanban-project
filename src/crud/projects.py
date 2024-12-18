from models.projects.createProjects import CreateProject
from models.projects.projects import Project
from src.database import fetch_query, execute_query


projects_list = []

def create_project(project: CreateProject):
    query = """
    INSERT INTO projects (name, description) VALUES (%s, %s);
    """
    execute_query(query, (project.name, project.description))

def get_projects() -> list[Project]:
    query = "SELECT * FROM projects"
    rows = fetch_query(query)
    return [Project(id=row[0], name=row[1], description=row[2], created_at=row[3], updated_at=row[4]) for row in rows]

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