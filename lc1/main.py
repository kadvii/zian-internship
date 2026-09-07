from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "John Doe",
         "age": 20,
         "major": "Computer Science"},
}


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/get_student/{student_id}")
async def get_student(student_id: int):
    return students.get(student_id, {"error": "Student not found"}) 