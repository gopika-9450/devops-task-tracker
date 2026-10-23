from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="DevOps Task Tracker API", version="1.0.0",
              description="Demo API for Docker and CI/CD practice.")

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    completed: bool = False

class Task(TaskCreate):
    id: int

tasks: dict[int, Task] = {}
next_id = 1

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

@app.get("/tasks", response_model=list[Task], tags=["tasks"])
def list_tasks():
    return list(tasks.values())

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(payload: TaskCreate):
    global next_id
    task = Task(id=next_id, title=payload.title, completed=payload.completed)
    tasks[next_id] = task
    next_id += 1
    return task

@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.patch("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, payload: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    task = Task(id=task_id, title=payload.title, completed=payload.completed)
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
