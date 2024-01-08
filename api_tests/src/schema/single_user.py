from pydantic import BaseModel, field_validator, Field


class Data(BaseModel):
    id: int
    email: str
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=100)
    avatar: str

    @field_validator('email')
    def check_correct_email(cls, email):
        if '@reqres.in' in email:
            return email
        else:
            raise ValueError('Your domain does not meet the requirements')

    @field_validator('avatar')
    def check_correct_image_format(cls, avatar):
        if '.jpg' in avatar:
            return avatar
        else:
            raise ValueError('This is the wrong image format')


class Support(BaseModel):
    url: str
    text: str

    @field_validator('url')
    def check_correct_url(cls, url):
        if 'https' in url:
            return url
        else:
            raise ValueError('Url dose not found')


class SingleUser(BaseModel):
    data: Data
    support: Support
