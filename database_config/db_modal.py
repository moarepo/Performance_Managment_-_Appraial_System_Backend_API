import uuid
import enum

from sqlalchemy import Enum, Column, String, DateTime, ForeignKey, Boolean, false
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

class Roles(str, enum.Enum):
    OD_DIRECTOR  = "Director Oganization Development"
    OD_SECRETARY = "Oganization Development Secretsry"
    OD_OFFICER = "Oganization Development Officer"
    HRM = "Human Resource Management"
    HRD = "Human Resource Development"
