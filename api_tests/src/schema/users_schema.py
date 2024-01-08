from pydantic import BaseModel, field_validator, Field


class Data(BaseModel):
    id: int = Field(le=12)
    email: str
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    avatar: str
    
    @field_validator('email')
    def check_correct_email(cls, email):
        if '@reqres.in' in email:
            return email
        else:
            raise ValueError('Your domain does not meet the requirements')


class Support(BaseModel):
    url: str
    text: str
            
    @field_validator('url')
    def check_correct_url(cls, url):
        if 'https' in url:
            return url
        else:
            raise ValueError('Url dose not found')


class UsersList(BaseModel):
    page: int = Field(le=2)
    per_page: int = Field(le=6)
    total: int = Field(le=12)
    total_pages: int = Field(le=2)
    data: list[Data]
    support: Support
