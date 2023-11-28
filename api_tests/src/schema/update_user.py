from pydantic import BaseModel, Field


class UserUpdated(BaseModel):
    name: str = Field(max_length=50)
    job: str = Field(max_length=100)
    updatedAt: str
