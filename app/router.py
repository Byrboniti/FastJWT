from fastapi import APIRouter, Depends
from app.config import SessionLocal
from sqlalchemy.orm import Session
from app.model import Response, RequestPost

import app.crud as crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_post_service(request: RequestPost, db: Session = Depends(get_db)):
    crud.create_post(db, post=request.parameter, user_id=request.parameter.id)
    return Response(status="Ok",
                    code="200",
                    message="Post created successfully").dict(exclude_none=True)


@router.get("/")
async def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _posts = crud.get_post(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_posts)


@router.patch("/update")
async def update_post(request: RequestPost, db: Session = Depends(get_db)):
    _post = crud.update_post(db, post_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.content)
    return Response(status="Ok", code="200", message="Success update data", result=_post)


@router.delete("/delete")
async def delete_post(request: RequestPost, db: Session = Depends(get_db)):
    crud.remove_post(db, post_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
