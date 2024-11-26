from src.models.columnsModel import Columns
from src.database import fetch_query, execute_query

columns_list = []

def create_column(column: Columns):
    query = """
    INSERT INTO columns (name) VALUES (%s)
    """
    execute_query(query, (column.name))

def get_columns() -> list[Columns]:
    query = "SELECT id, column_id, name, position FROM columns"
    rows = fetch_query(query)
    return [Columns(id=row[0], column_id=row[1], name=row[2], position=row[3]) for row in rows]

def update_column(column_id, new_data):
    query = """
    UPDATE columns
    SET 
        name = COALESCE(%s, name),
    WHERE id = %s
    """
    params = (new_data['name'],column_id)
    execute_query(query, params)

def delete_column(column_id):
    query = """
    DELETE FROM columns
    WHERE id = %s
    """
    params = (column_id,)
    execute_query(query, params)