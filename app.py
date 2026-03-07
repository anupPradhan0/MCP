"""
Todo API with FastAPI (no Flask).
Run: uvicorn app:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from task import TaskStore

app = FastAPI(title="Todo API")
store = TaskStore()


class CreateTaskBody(BaseModel):
    title: str


@app.get("/tasks")
def list_tasks():
    return store.get_tasks()


@app.post("/tasks")
def create_task(body: CreateTaskBody):
    title = (body.title or "").strip()
    if not title:
        raise HTTPException(status_code=400, detail="title is required")
    return store.add_task(title)


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = store.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="not found")
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if not store.remove_task_by_id(task_id):
        raise HTTPException(status_code=404, detail="not found")
    return None


@app.post("/tasks/{task_id}/toggle")
def toggle_task(task_id: int):
    task = store.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="not found")
    idx = next(i for i, t in enumerate(store.get_tasks()) if t["id"] == task_id)
    store.toggle_done(idx)
    return store.get_task(idx)
