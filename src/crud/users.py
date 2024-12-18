from models.users.createUsers import CreateUsers
from models.users.users import Users
from src.database import fetch_query, execute_query


users_list = []

def create_user(user: CreateUsers):
    query = """
    INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s);
    """
    execute_query(query, (user.username, user.email, user.password_hash))

def get_users() -> list[Users]:
    query = "SELECT * FROM users"
    rows = fetch_query(query)
    print(query)
    return [Users(id=row[0], username=row[1], email=row[2], password_hash=row[3]) for row in rows]

def delete_user(user_id):
    query = """
    DELETE FROM users
    WHERE id = %s ;
    """
    params = (user_id,)
    execute_query(query, params)