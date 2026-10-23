import app.main as main_module
from fastapi.testclient import TestClient

client = TestClient(main_module.app)

def setup_function():
    main_module.tasks.clear()
    main_module.next_id = 1

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_list():
    response = client.post("/tasks", json={"title": "Learn Docker"})
    assert response.status_code == 201
    assert response.json()["title"] == "Learn Docker"
    assert len(client.get("/tasks").json()) == 1

def test_missing_task_returns_404():
    assert client.get("/tasks/999").status_code == 404

def test_update_and_delete():
    created = client.post("/tasks", json={"title": "First"}).json()
    task_id = created["id"]
    updated = client.patch(f"/tasks/{task_id}", json={"title": "Updated", "completed": True})
    assert updated.status_code == 200
    assert updated.json()["completed"] is True
    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404
