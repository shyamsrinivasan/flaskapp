from sqlalchemy import create_engine
from sqlalchemy import text


engine = create_engine("mysql+mysqldb://root:root@localhost/taxdata")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM taxdata.clients"))
    print(result.all())
