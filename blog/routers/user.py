from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, models, hashing, database
from sqlalchemy.orm import Session
from ..repository import user

get_db = database.get_db


router = APIRouter(
    prefix="/user",
    tags = ['users']
    )

#user creation and hashing 

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/')
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)