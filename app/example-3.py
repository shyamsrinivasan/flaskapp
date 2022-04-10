from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


engine = create_engine("mysql+mysqldb://root:root@localhost/agridb")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM agridb.items"))
    print(result.all())

# commit as you go using SQLAlchemy
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 1, "y": 1}, {"x": 2, "y": 4}])
    conn.commit()

# "begin once"
with engine.begin() as conn:
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 6, "y": 8}, {"x": 9, "y": 10}])

# including (binding) parameters in SQL statements
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

# use Session (ORM) insead of Connection (Core)
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
