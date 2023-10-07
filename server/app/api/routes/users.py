from typing import Any, Dict, List
from fastapi import APIRouter, Body

from app.models.user import UserCreate, UserDelete, UserUpdate
from app.services.users import UserService


router = APIRouter()

user_service = UserService("users", "user")


@router.get(
    "/",
    response_description="Pegar todos os users emitidos",
    response_model=List[Dict[str, Any]],
)
def get_all_users():
    all_users = user_service.get_all_user()
    return all_users


@router.get(
    "/{contains}",
    response_description="Pegar todos os users emitidos com parâmetro",
    response_model=List[Dict[str, Any]],
)
def get_user_by(contains: str):
    users_by = user_service.get_by(contains)
    return users_by


@router.post(
    "/",
    response_description="Criar um novo user para o cliente",
    response_model=UserCreate,
)
def create_user(user: UserCreate = Body(...)):
    created_user = user_service.create_user(user)
    return created_user


@router.put(
    "/{id}", response_description="Atualizar um novo", response_model=UserUpdate
)
def update_user(id: str, user: UserUpdate = Body(...)):
    update_user = user_service.update_user(id, user)
    return update_user


@router.delete(
    "/{id}",
    response_description="Deletar um user criado",
    response_model=UserDelete,
)
def delete_user(id: str):
    delete_user = user_service.delete_user(id)
    return delete_user
