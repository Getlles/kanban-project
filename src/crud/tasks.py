from src.models.tasks import Tasks, CreateTasks
from src.database import fetch_query, execute_query

def create_task(task: CreateTasks):
    query = """
    INSERT INTO tasks (column_id, title, description) VALUES (%s, %s, %s) RETURNING id;
    """
    task_id = execute_query(query, (task.column_id, task.title, task.description))
    return task_id

def get_tasks(column_id) -> list[Tasks]:
    query = "SELECT * FROM tasks WHERE column_id = %s;"
    rows = fetch_query(query, (column_id,))
    if rows is None:
        return []
    return [Tasks(id=row[0], column_id=row[1], title=row[2], description=row[3], created_at=row[4], updated_at=row[5]) for row in rows]

def update_task(task_id, new_data):
    query = """
    UPDATE tasks
    SET
        column_id = COALESCE(%s, column_id),
        title = COALESCE(%s, title),
        description = COALESCE(%s, description),
        updated_at = NOW()
    WHERE id = %s
    """
    params = (new_data['new_column_id'], new_data['title'], new_data['description'], task_id)
    execute_query(query, params)

def delete_task(task_id):
    query = """
    DELETE FROM tasks
    WHERE id = %s ;
    """
    execute_query(query, (task_id,))