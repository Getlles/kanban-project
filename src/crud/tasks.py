from src.models.tasks.tasks import Tasks
from src.models.tasks.createTasks import CreateTasks
from src.database import fetch_query, execute_query

tasks_list = []

def create_task(task: CreateTasks):
    query = """
    INSERT INTO tasks (column_id, title, description) VALUES (%s, %s, %s)
    """
    execute_query(query, (task.column_id, task.title, task.description))

def get_tasks() -> list[Tasks]:
    query = "SELECT * FROM tasks ;"
    rows = fetch_query(query)
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
    params = (new_data['column_id'], new_data['title'], new_data['description'], task_id)
    execute_query(query, params)

def delete_task(task_id):
    query = """
    DELETE FROM tasks
    WHERE id = %s
    """
    params = (task_id,)
    execute_query(query, params)