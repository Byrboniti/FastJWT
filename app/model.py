from pydantic import BaseModel, Field, EmailStr
from app.config import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    like = Column(Integer)
    dislike = Column(Integer)
    creater = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    fullname = Column(String)
    password = Column(String)


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "123",
                "title": "Александр",
                "content": "Лебедченко"
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestPost(BaseModel):
    parameter: PostSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
