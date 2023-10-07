from enum import Enum
from typing import Any, List, Dict
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pymongo.collection import Collection
from app.database.database import DatabaseConfig

from app.models.ticket import TicketCreate, TicketDelete, TicketUpdate


class TicketService(DatabaseConfig):
    def __init__(self, db_name, collection_name: Collection):
        super().__init__(db_name, collection_name)

    def get_all_ticket(self):
        all_tickets = []
        for tickets in self.collection.find():
            all_tickets.append(tickets)

        if len(all_tickets) == 0:
            raise HTTPException(
                status_code=404, detail="Não foi possivel encontrar os tickets"
            )
        return all_tickets

    def get_by(self, contains: str) -> List[Dict[str, Any]] or HTTPException:
        tickets_by = []
        for tickets in self.collection.find({"$text": {"$search": contains}}):
            tickets_by.append(tickets)

        if tickets_by:
            return tickets_by
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum ticket foi encontrado para o valor: {contains}",
        )

    # def get_by_priority(self, priority: str):
    #     tickets_priority = []
    #     for ticket in self.collection.find({"ticket_priority": priority}):
    #         tickets_priority.append(ticket)

    #     if tickets_priority:
    #         return tickets_priority
    #     raise HTTPException(
    #         status_code=404,
    #         detail=f"Nenhum ticket com a prioridade: {priority}, foi encontrado  ",
    #     )

    def create_ticket(self, ticket: TicketCreate) -> TicketCreate:
        ticket_data = jsonable_encoder(ticket)
        try:
            new_ticket = self.collection.insert_one(ticket_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar o ticket: {e}")

        created_ticket = self.collection.find_one({"_id": new_ticket.inserted_id})

        if created_ticket:
            return created_ticket
        else:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar o ticket: {e}")

    def update_ticket(self, id: str, ticket: TicketUpdate) -> TicketUpdate:
        ticket_data = {
            k: v.value if isinstance(v, Enum) else v
            for k, v in ticket.model_dump().items()
            if v is not None
        }

        if len(ticket_data) >= 1:
            update_ticket = self.collection.update_one(
                {"_id": id}, {"$set": ticket_data}
            )

            if update_ticket.matched_count == 0:
                raise HTTPException(status_code=404, detail="Ticket não encontrado")

        if (exists_ticket := self.collection.find_one({"_id": id})) is not None:
            return exists_ticket

        raise HTTPException(status_code=404, detail="Ticket não encontrado")

    def delete_ticket(self, id: str) -> dict:
        delete_ticket = self.collection.delete_one({"_id": id})

        if delete_ticket.deleted_count == 1:
            raise HTTPException(status_code=200, detail="Ticket deletado com sucesso")

        raise HTTPException(status_code=404, detail="Ticket não foi encontrado")
