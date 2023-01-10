from sqlalchemy.orm import Session
from app.model import Post, PostSchema


def get_post(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(db: Session, post: PostSchema, user_id: int):
    _post = Post(title=post.title, description=post.content, creater=user_id)
    db.add(_post)
    db.commit()
    db.refresh(_post)
    return _post


def remove_post(db: Session, post_id: int):
    _post = get_post_by_id(db=db, post_id=post_id)
    db.delete(_post)
    db.commit()


def update_post(db: Session, post_id: int, title: str, description: str, ):
    _post = get_post_by_id(db=db, post_id=post_id)
    _post.title = title
    _post.description = description

    db.commit()
    db.refresh(_post)
    return _post


def likeornot(db: Session, post_id: int, creater: int, user_id, like: int):
    _post = get_post_by_id(db=db, post_id=post_id)
    if creater == user_id:
        pass
    else:
        if like > 0:
            _post.like = _post.like + 1
        else:
            _post.dislike = _post.dislike + 1

        db.commit()
        db.refresh(_post)
