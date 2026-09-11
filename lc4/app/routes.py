from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import Task, TaskCreate, TaskPublic

router = APIRouter()


@router.post("/tasks", response_model=TaskPublic, status_code=201)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.get("/tasks", response_model=list[TaskPublic])
def list_tasks(
    done: bool | None = None,
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session),
):
    query = select(Task)
    if done is not None:
        query = query.where(Task.done == done)
    return session.exec(query.offset(skip).limit(limit)).all()


@router.get("/tasks/search", response_model=list[TaskPublic])
def search_tasks(q: str, session: Session = Depends(get_session)):
    query = select(Task).where(Task.title.contains(q))
    return session.exec(query).all()


@router.get("/tasks/{task_id}", response_model=TaskPublic)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskPublic)
def update_task(
    task_id: int,
    new_data: TaskCreate,
    session: Session = Depends(get_session),
):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = new_data.title
    task.done = new_data.done
    task.priority = new_data.priority
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
