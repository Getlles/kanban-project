from typing import Optional
from src.models.users import SignUsers, Users
from src.database import fetch_query, execute_query

def create_user(user: SignUsers):
    query = """
    INSERT INTO users (username, email, password) VALUES (%s, %s, %s);
    """
    execute_query(query, (user.username, user.email, user.password))

def get_users() -> list[Users]:
    query = "SELECT * FROM users"
    rows = fetch_query(query)
    print(query)
    return [Users(id=row[0], username=row[1], email=row[2], password=row[3]) for row in rows]

def delete_user(user_id):
    query = """
    DELETE FROM users
    WHERE id = %s ;
    """
    params = (user_id,)
    execute_query(query, params)


def get_user_by_email(email) -> Optional[Users]:
    query = "SELECT * FROM users WHERE email = %s;"
    rows = fetch_query(query, (email,))
    if rows:
        return Users(id=rows[0][0], username=rows[0][1], email=rows[0][2], password=rows[0][3])
    return

def get_user_by_username(username) -> Optional[Users]:
    query = "SELECT * FROM users WHERE username = %s;"
    rows = fetch_query(query, (username,))
    if rows:
        return Users(id=rows[0][0], username=rows[0][1], email=rows[0][2], password=rows[0][3])
    return

def check_user(username, email) -> Optional[Users]:
    query = "SELECT * FROM users WHERE username = %s AND email = %s;"
    rows = fetch_query(query, (username, email))
    if rows:
        return Users(id=rows[0][0], username=rows[0][1], email=rows[0][2], password=rows[0][3])
    return