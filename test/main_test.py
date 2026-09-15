from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_get_all_students():

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) >= 1



def test_get_single_student():

    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1



def test_get_nonexistent_student():

    response = client.get("/students/999")

    assert response.status_code == 404



def test_create_student():

    new_student = {
        "id": 10,
        "name": "Sabbir",
        "department": "CSE",
        "cgpa": 3.90,
        "semester": 6
    }


    response = client.post(
        "/students",
        json=new_student
    )


    assert response.status_code == 201
    assert response.json()["name"] == "Sabbir"



def test_create_duplicate_student():

    new_student = {
        "id": 1,
        "name": "Another Student",
        "department": "CSE",
        "cgpa": 3.20,
        "semester": 2
    }


    response = client.post(
        "/students",
        json=new_student
    )


    assert response.status_code == 400



def test_update_student():

    updated_student = {
        "id": 1,
        "name": "Rahim Updated",
        "department": "CSE",
        "cgpa": 3.85,
        "semester": 6
    }


    response = client.put(
        "/students/1",
        json=updated_student
    )


    assert response.status_code == 200
    assert response.json()["name"] == "Rahim Updated"



def test_update_nonexistent_student():

    updated_student = {
        "id": 999,
        "name": "Unknown",
        "department": "Unknown",
        "cgpa": 2.0,
        "semester": 1
    }


    response = client.put(
        "/students/999",
        json=updated_student
    )


    assert response.status_code == 404



def test_delete_student():

    response = client.delete("/students/2")


    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"



def test_delete_nonexistent_student():

    response = client.delete("/students/999")


    assert response.status_code == 404