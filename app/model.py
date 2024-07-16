from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Rimma",
                "email": "rimma@gmail.com",
                "password": "admin"
            }
    }

class PostSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    author: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Cats",
                "description": "All about cats",
                "author": "Zhansaya"
            }
    }




class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

class Config:
    schema_extra = {
         "example": {
        "email": "zhans@gmail.com",
        "password": "admin"
        }
    }