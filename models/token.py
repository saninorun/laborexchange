from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_string: str

class Login(BaseModel):
    email: EmailStr
    password: str
