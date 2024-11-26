from src.models.tasksModel import Tasks
from src.database import fetch_query, execute_query

tasks_list = []

def create_task(task: Tasks):
    query = """
    INSERT INTO tasks (column_id, title, description, status) VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (task.column_id, task.title, task.description, task.status))

def get_tasks() -> list[Tasks]:
    query = "SELECT id, column_id, title, description, created_at, updated_at FROM tasks"
    rows = fetch_query(query)
    return [Tasks(id=row[0], column_id=row[1], title=row[2], description=row[3], created_at=row[4], updated_at=row[5], status=row[6]) for row in rows]

def update_task(task_id, new_data):
    query = """
    UPDATE tasks
    SET 
        title = COALESCE(%s, title),
        description = COALESCE(%s, description),
        updated_at = NOW()
        status = COALESCE(%s, status)
    WHERE id = %s
    """
    params = (new_data('column_id'), new_data('title'), new_data('description'), new_data('status'), task_id)
    execute_query(query, params)

def delete_task(task_id):
    query = """
    DELETE FROM tasks
    WHERE id = %s
    """
    params = (task_id,)
    execute_query(query, params)