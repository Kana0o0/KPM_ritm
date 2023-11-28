from pydantic import BaseModel, Field


class UserCreated(BaseModel):
    name: str = Field(max_length=50)
    job: str = Field(max_length=100)
    id: str
    createdAt: str
