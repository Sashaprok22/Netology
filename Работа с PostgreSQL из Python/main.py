import psycopg2

def create_db(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE Phones;")
    cursor.execute("DROP TABLE Clients;")
    cursor.execute("CREATE TABLE IF NOT EXISTS Clients(client_id SERIAL PRIMARY KEY, first_name VARCHAR(60), last_name VARCHAR(60), email TEXT UNIQUE);")
    cursor.execute("CREATE TABLE IF NOT EXISTS Phones(number INT PRIMARY KEY, client INT NOT NULL REFERENCES Clients(client_id));")
    conn.commit()
    cursor.close()

def add_client(conn, first_name, last_name, email, phones=None):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clients(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING client_id;", (first_name, last_name, email))
    id = cursor.fetchone()[0]

    for number in phones:   
        cursor.execute("INSERT INTO Phones(number, client) VALUES(%s, %s);", (number, id))
    
    conn.commit()
    cursor.close()

def add_phone(conn, client_id, phone):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Phones(number, client) VALUES(%s, %s);", (phone, client_id))
    conn.commit()
    cursor.close()

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cursor = conn.cursor()

    if first_name is not None:
        cursor.execute("UPDATE Clients SET first_name=%s WHERE client_id=%s;", (first_name, client_id))

    if last_name is not None:
        cursor.execute("UPDATE Clients SET last_name=%s WHERE client_id=%s;", (last_name, client_id))

    if email is not None:
        cursor.execute("UPDATE Clients SET email=%s WHERE client_id=%s;", (email, client_id))

    if phones is not None:
        cursor.execute("DELETE FROM Phones WHERE client_id=%s;", (client_id,))
        for number in phones:   
            cursor.execute("INSERT INTO Phones(number, client) VALUES(%s, %s);", (number, client_id))

    conn.commit()
    cursor.close()

def delete_phone(conn, client_id, phone):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Phones WHERE number=%s AND client=%s;", (phone, client_id))
    conn.commit()
    cursor.close()


def delete_client(conn, client_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Phones WHERE client=%s;", (client_id,))
    cursor.execute("DELETE FROM Clients WHERE client=%s;", (client_id,))
    conn.commit()
    cursor.close()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cursor = conn.cursor()

    if phone is not None:
        cursor.execute("SELECT client FROM Phones WHERE number=%s LIMIT 1;", (phone,))
    else:
        cursor.execute("SELECT client_id FROM Clients WHERE first_name=%s AND last_name=%s AND email=%s LIMIT 1;", (first_name, last_name, email))

    id = cursor.fetchone()[0]
    cursor.close()
    return id



with psycopg2.connect(database="clients_db", user="postgres", password="123123") as conn:
    create_db(conn)
    add_client(conn, "Sasha", "Prok", "sashaprok22@gmail.com", (666,))
    id = find_client(conn, phone=666)
    add_phone(conn, id, 888)
    change_client(conn, id, "Sashaprok", "")
    delete_phone(conn, id, 666)