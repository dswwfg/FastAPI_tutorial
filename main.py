from typing import Optional

from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from uuid import uuid4  # for fake token

class TransactionManager:
    pass




fake_users_db = [
    {
        'email': 'fake_ciphered_email_1',
        'password': 'fake_ciphered_password_1',

    },
    {
        'email': 'fake_ciphered_email_2',
        'password': 'fake_ciphered_password_2'
    }
]


app = FastAPI()


class User(BaseModel):
    hashed_email: Optional[str] = 'fake_ciphered_email_1'
    hashed_password: Optional[str] = 'fake_ciphered_password_1'


def validate_user_account(user):

    for p in fake_users_db:
        if p['email'] == user.hashed_email and p['password'] == user.hashed_password:
            return True
        elif p['email'] != user.hashed_email:
            print('Please email check')
            return False
        elif p['password'] != user.hashed_password:
            print('Password check')
            return False
        else:
            print('Your account is not registered')
            return False


def generate_token(user):
    # Todo :
    rand_token = uuid4()
    return rand_token


def login_func(user):
    bool_res = validate_user_account(user)
    token = ''

    if bool_res:
        token = generate_token(user)

    return bool_res, token


# Todo : login 이전에 Public key, otid를 생성 후 client에 제공
@app.post('/login')
def login(user: User):
    bool_login, token = login_func(user)

    return {'login_success': bool_login, 'token': token}


@app.post('/upload/')
async def upload_file(file: UploadFile = File(...), token: str = Form(...)):

    # object indicator 요청해서 location 정보 받아옴


    return {"filename": file.filename}
