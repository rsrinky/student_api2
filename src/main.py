from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Student Management API")


class Student(BaseModel):
    id: int
    name: str
    department: str
    cgpa: float
    semester: int


students = [
    Student(
        id=1,
        name="Rahim",
        department="CSE",
        cgpa=3.75,
        semester=5
    ),
    Student(
        id=2,
        name="Karim",
        department="EEE",
        cgpa=3.50,
        semester=4
    )
]


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.post("/students", status_code=201)
def create_student(student: Student):

    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student)

    return student


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == student_id:

            students[index] = updated_student

            return updated_student


    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:
            students.pop(index)

            return {
                "message": "Student deleted successfully"
            }


    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )