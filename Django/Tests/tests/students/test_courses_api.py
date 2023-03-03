import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_course(client, courses_factory):
    course = courses_factory()

    response = client.get(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 200

    response_json = response.json()
    assert course.id == response_json.get("id")

@pytest.mark.django_db
def test_courses(client, courses_factory):
    courses = courses_factory(_quantity=20)

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200

    response_json = response.json()

    for i, course in enumerate(courses):
        assert course.id == response_json[i].get("id")

@pytest.mark.django_db
def test_courses_filter_by_id(client, courses_factory):
    courses = courses_factory(_quantity=20)

    response = client.get(f'/api/v1/courses/', data={"id": courses[0].id})
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) > 0

    for course in response_json:
        assert courses[0].id == course.get("id")

@pytest.mark.django_db
def test_courses_filter_by_name(client, courses_factory):
    courses = courses_factory(_quantity=20)

    response = client.get(f'/api/v1/courses/', data={"name": courses[0].name})
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) > 0

    for course in response_json:
        assert courses[0].name == course.get("name")

@pytest.mark.django_db
def test_create_course(client):
    test_data = {
        "name": "My Test Course",
    }

    response = client.post(f'/api/v1/courses/', data=test_data, format="json")
    assert response.status_code == 201

    response_json = response.json()
    assert response_json.get("name") == test_data.get("name")

@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory()

    test_data = {
        "name": "Second name",
    }

    response = client.patch(f'/api/v1/courses/{course.id}/', data=test_data, format="json")
    assert response.status_code == 200

    response_json = response.json()
    assert course.id == response_json.get("id")
    assert response_json.get("name") == test_data.get("name")

@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory()

    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 204