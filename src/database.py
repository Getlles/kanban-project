import psycopg2

#Подключение к бд
try:
    conn = psycopg2.connect(dbname="kanban", user="postgres", password="root", host="localhost", port="8835")
    cur = conn.cursor()

except Exception as e:
    print("Can't establish connection to database", e)



def execute_query(query, params=None): #Для изменения в бд
    try:
        cur.execute(query, params)
        if query.strip().startswith("INSERT") and "RETURNING" in query: #Для возвращения айди проекта
            return cur.fetchone()[0]
        conn.commit()
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")

def fetch_query(query, params=None): #Для селекта
    try:
        cur.execute(query, params)
        return cur.fetchall()
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")



def init_db():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS projects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        description VARCHAR(511),
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        );
                
        CREATE TABLE IF NOT EXISTS project_users (
        id SERIAL PRIMARY KEY,
        project_id INT REFERENCES projects(id) NOT NULL,
        user_id INT REFERENCES users(id) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS columns (
        id SERIAL PRIMARY KEY,
        project_id INT REFERENCES projects(id),
        name VARCHAR(255) UNIQUE NOT NULL,
        position INT NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        column_id INT REFERENCES columns(id),
        title VARCHAR(255),
        description TEXT,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        );
                
        CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) REFERENCES users(name),
        project_id INT REFERENCES projects(id),
        column_id INT,
        task_id INT,
        action VARCHAR(63) NOT NULL,
        time TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        message TEXT
        );
    ''')
    
    conn.commit()