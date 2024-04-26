class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.prev, self.curr = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        else:
            result = self.prev
            self.prev, self.curr = self.curr, self.prev + self.curr
            self.count += 1
            return result

fib_sequence = Fibonacci(10)
for num in fib_sequence:
    print(num)



import psycopg2

host = 'localhost'
user = 'postgres'
password = '123'
database = 'postgres'
port = 5432

conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port
                        )
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS n42.M5 (
        id SERIAL PRIMARY KEY,
        year INTEGER,
        color VARCHAR(255),
        price int not null,
        model VARCHAR(255)
    )
""")

cur = conn.cursor()

insert_car_query = """
    insert into n42.M5 (year,color,price,model)
    values('2022','Black',100000000,'competition')
"""
conn.commit()

cur.execute("SELECT * FROM n42.M5")

rows = cur.fetchall()
for row in rows:
    print(row)

cur = conn.cursor()

cur.execute("""
    UPDATE n42.M5 
    SET price=1000000 
    WHERE year=2022 
""", (100100000,2024))

conn.commit()

cur.execute("""
    DELETE FROM n42.M5
    WHERE year=year
""", (2019,))

conn.commit()

cur = conn.cursor()
