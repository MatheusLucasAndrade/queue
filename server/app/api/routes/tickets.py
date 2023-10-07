from typing import Any, Dict, List
from fastapi import APIRouter, Body, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from pymongo import MongoClient

from app.models.ticket import TicketCreate, TicketDelete, TicketUpdate
from app.services.ticket import TicketService


router = APIRouter()

ticket_service = TicketService("tickets", "ticket")


@router.get(
    "/",
    response_description="Pegar todos os tickets emitidos",
    response_model=List[Dict[str, Any]],
)
def get_all_tickets():
    all_tickets = ticket_service.get_all_ticket()
    return all_tickets


@router.get(
    "/{contains}",
    response_description="Pegar todos os tickets emitidos com parâmetro",
    response_model=List[Dict[str, Any]],
)
def get_ticket_by(contains: str):
    tickets_by = ticket_service.get_by(contains)
    return tickets_by


@router.post(
    "/",
    response_description="Criar um novo ticket para o cliente",
    response_model=TicketCreate,
)
def create_ticket(ticket: TicketCreate = Body(...)):
    created_ticket = ticket_service.create_ticket(ticket)
    return created_ticket


@router.put(
    "/{id}", response_description="Atualizar um novo", response_model=TicketUpdate
)
def update_ticket(id: str, ticket: TicketUpdate = Body(...)):
    update_ticket = ticket_service.update_ticket(id, ticket)
    return update_ticket


@router.delete(
    "/{id}",
    response_description="Deletar um ticket criado",
    response_model=TicketDelete,
)
def delete_ticket(id: str):
    delete_ticket = ticket_service.delete_ticket(id)
    return delete_ticket
