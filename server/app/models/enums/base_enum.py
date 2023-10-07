from enum import Enum


class TicketPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class UserProfile(Enum):
    USER = "USER"
    MODERADOR = "MODERADOR"
    ADMIN = "ADMIN"
