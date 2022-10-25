import logging
from matdb import Database
import json

import decimal, datetime

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

logging.basicConfig(level=logging.DEBUG)
logging.debug("Welcome")
db_string = "mysql://vijay:Vinisha329$@localhost:3306/test"
database = Database(db_string)
database.connect()
print("Connection established....")
# rows = database.fetch_all(query="select * from brands")
# print(rows)
# print(json.dumps([dict(r) for r in rows], default=alchemyencoder))
json_str = database.fetch_all_as_json_string(query="select * from brands")

print(json_str)
query = "INSERT INTO emp(emp_id, emp_name) VALUES (:emp_id, :emp_name)"
#values = {}
values = {"emp_id":123, "emp_name":"Vijay"}
rowcnt = database.execute(query=query, values=values)
print(f"Row count == > {rowcnt}")