from src.models.columns.columnsModel import Columns
from src.models.columns.createColumnsModel import CreateColumns
from src.database import fetch_query, execute_query

columns_list = []

def create_column(column: CreateColumns):
    update_query = """
    UPDATE columns
    SET position = position + 1
    WHERE project_id = %s AND position >= %s ;
    """
    execute_query(update_query, (column.project_id, column.position))
    query = """
    INSERT INTO columns (project_id, name, position) VALUES (%s, %s, %s) ;
    """
    execute_query(query, (column.project_id, column.name, column.position))

def get_columns() -> list[Columns]:
    query = "SELECT id, project_id, name, position FROM columns ;"
    rows = fetch_query(query)
    return [Columns(id=row[0], project_id=row[1], name=row[2], position=row[3]) for row in rows]

def update_column(column_id, new_data):
    query = """
    UPDATE columns
    SET 
        name = COALESCE(%s, name),
        position = COALESCE(%s, position)
    WHERE id = %s;
    """
    execute_query(query, (new_data['name'], new_data['position'], column_id))

def delete_column(column_id):
    query = "SELECT project_id, position FROM columns WHERE id = %s"
    column_info = fetch_query(query, (column_id,))

    if column_info is None or len(column_info) == 0:
        raise Exception("Column not found")

    project_id, position = column_info[0]

    delete_query = """
    DELETE FROM columns
    WHERE id = %s
    """
    execute_query(delete_query, (column_id,))

    update_query = """
    UPDATE columns
    SET position = position - 1
    WHERE project_id = %s AND position > %s
    """
    execute_query(update_query, (project_id, position))