from src.database import fetch_query, execute_query
from src.models.logs import Logs
from typing import List

def create_log(username: str, project_id: int, column_id: int, task_id: int, action: str, message: str):
    query = """
    INSERT INTO logs (username, project_id, column_id, task_id, action, message)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    params = (username, project_id, column_id, task_id, action, message)
    execute_query(query, params)

def get_logs_by_project(project_id: int):
    query = "SELECT message FROM logs WHERE project_id = %s ;"
    rows = fetch_query(query, (project_id,))
    if rows is None:
        return []
    return [row[0] for row in rows]