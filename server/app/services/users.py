from enum import Enum
from typing import Any, List, Dict
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pymongo.collection import Collection
from app.database.database import DatabaseConfig

from app.models.user import UserCreate, UserDelete, UserUpdate


class UserService(DatabaseConfig):
    def __init__(self, db_name, collection_name: Collection):
        super().__init__(db_name, collection_name)

    def get_all_user(self):
        all_users = []
        for users in self.collection.find():
            all_users.append(users)

        if len(all_users) == 0:
            raise HTTPException(
                status_code=404, detail="Não foi possivel encontrar os users"
            )
        return all_users

    def get_by(self, contains: str) -> List[Dict[str, Any]] or HTTPException:
        users_by = []

        query = {
            "$or": [
                {"user_name": {"$regex": contains, "$options": "i"}},
                {"user_profile": {"$regex": contains, "$options": "i"}},
            ]
        }

        for users in self.collection.find(query):
            users_by.append(users)

        if users_by:
            return users_by
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum user foi encontrado para o valor: {contains}",
        )

    def create_user(self, user: UserCreate) -> UserCreate:
        user_data = jsonable_encoder(user)
        try:
            new_user = self.collection.insert_one(user_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar o user: {e}")

        created_user = self.collection.find_one({"_id": new_user.inserted_id})

        if created_user:
            return created_user
        else:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar o user: {e}")

    def update_user(self, id: str, user: UserUpdate) -> UserUpdate:
        user_data = {
            k: v.value if isinstance(v, Enum) else v
            for k, v in user.model_dump().items()
            if v is not None
        }

        if len(user_data) >= 1:
            update_user = self.collection.update_one({"_id": id}, {"$set": user_data})

            if update_user.matched_count == 0:
                raise HTTPException(status_code=404, detail="User não encontrado")

        if (exists_user := self.collection.find_one({"_id": id})) is not None:
            return exists_user

        raise HTTPException(status_code=404, detail="User não encontrado")

    def delete_user(self, id: str) -> dict:
        delete_user = self.collection.delete_one({"_id": id})

        if delete_user.deleted_count == 1:
            raise HTTPException(status_code=200, detail="User deletado com sucesso")

        raise HTTPException(status_code=404, detail="User não foi encontrado")
