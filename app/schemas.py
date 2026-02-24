from pydantic import BaseModel


class Base(BaseModel):
    username: str
    email: str
    fullname: str
    gender: str

class CreateUser(Base):
    password: str

class UserResponce(Base):
    pass