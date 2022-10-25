from fastapi import FastAPI
import json
import decimal, datetime
from pydantic import BaseModel
from matdb import Database

app = FastAPI()

db_string = "mysql://vijay:Vinisha329$@localhost:3306/test"
database = Database(db_string)

class Emp(BaseModel):
    emp_id : int
    emp_name: str



@app.on_event("startup")
async def startup():
    database.connect()

@app.on_event("shutdown")
async def shutdown():
    database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/dbtest")
async def dbtest():
    rows = database.fetch_all(query="select * from brands")
    #print(rows)
    jsonStr = json.dumps([dict(r) for r in rows], default=alchemyencoder)
    return jsonStr

@app.post("/emp")
async def addEmp(emp : Emp):
    query = "INSERT INTO emp(emp_id, emp_name) VALUES (:emp_id, :emp_name)"
    values = {"emp_id": emp.emp_id, "emp_name": emp.emp_name}
    database.execute(query=query, values=values)
    print("Employee inserted...")
    return "ok"


