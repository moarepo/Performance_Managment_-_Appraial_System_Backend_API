import uuid
import enum
from sqlalchemy import Column, String, DateTime, Enum, Boolean, text, func, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Roles(str, enum.Enum):
    OD_DIRECTOR  = "Director Oganization Development"
    OD_SECRETARY = "Oganization Development Secretsry"
    OD_OFFICER = "Oganization Development Officer"
    HRM = "Human Resource Management"
    HRD = "Human Resource Development"


class Users(Base):
    __tablename__ = "users"

    user_Id = Column( 
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        nullable=False, 
        server_default=text("gen_random_uuid()")
    )
    username =  Column(String, unique=True, nullable=False)
    password =  Column(String, nullable=False)
    user_role = Column(Enum(Roles, name="user_user_role"), nullable=False)
    fristname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False, default= True)
    DateCreated = Column(DateTime(timezone=True), default=func.now())

class Divisions(Base):
    __tablename__ = "divisions"

    division_id = Column( 
        UUID(as_uuid=True), 
        index= True,
        primary_key=True, 
        default=uuid.uuid4, 
        nullable=False, 
        server_default=text("gen_random_uuid()")
    )
    division_name = Column(String, nullable=False, unique=True)
    DateCreated = Column(DateTime(timezone=True), default=func.now())

class JobTitles(Base):
    __tablename__="job_titles_table"

    job_title_id =  Column( 
        UUID(as_uuid=True), 
        index= True,
        primary_key=True, 
        default=uuid.uuid4, 
        nullable=False, 
        server_default=text("gen_random_uuid()")
    )
    job_title_name = Column(String,nullable=False,unique=True)
    DateCreated = Column(DateTime(timezone=True), default=func.now())

class PostGrades(Base):
    __tablename__="post_grades_table"

    post_grade_id = Column(
        UUID(as_uuid=True), 
        index= True,
        primary_key=True, 
        default=uuid.uuid4, 
        nullable=False, 
        server_default=text("gen_random_uuid()")
    )
    post_grade_name = Column(String,unique=True,nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=func.now())

class Employess(Base):
    __tablename__="employees"

    employee_Id = Column(
        UUID(as_uuid=True), 
        index= True,
        primary_key=True, 
        default=uuid.uuid4, 
        nullable=False, 
        server_default=text("gen_random_uuid()")
    )
    employee_number = Column(String,nullable=False,unique=True)
    fristname = Column(String,nullable=False)
    middlename = Column(String,nullable=True)
    lastname = Column(String,nullable=False)
    post_number = Column(String,nullable=True)
    job_title_id = Column(UUID(as_uuid=True), ForeignKey("job_titles_table.job_title_id"), nullable=False)
    post_title_id = Column(UUID(as_uuid=True),ForeignKey("job_titles_table.job_title_id"), nullable=False)
    post_grade_Id = Column(UUID(as_uuid=True), ForeignKey("post_grades_table.post_grade_id"), nullable=False)
    divivision_id = Column(UUID(as_uuid=True), ForeignKey("divisions.division_id"), nullable=False)
    is_active = Column(Boolean,default=True,nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=func.now())


class DocumentStatuses(Base):
    __tablename__="document_statuses_table"

    status_Id = Column(
        UUID(as_uuid=True),
        index=True,
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )
    status_name = Column(String,unique=True,nullable=False)
    is_initial_status= Column(Boolean,nullable=False)
    is_terminal_status = Column(Boolean,nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=func.now())

class PERs_table(Base):
    __tablename__="pers_table"

    per_id = Column(
        UUID(as_uuid=True),
        index=True,
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )
    employee_id = Column(UUID(as_uuid=True),ForeignKey("employees.employee_Id"),nullable=False)
    period_of_evaluation = Column(String,nullable=False)
    performance_scores = Column(Numeric(precision=5, scale=2), nullable=True)
    pmas_scores = Column(Numeric(precision=5, scale=2), nullable=True)
    training_needs = Column(String, nullable=True)
    CareerAspirations = Column(String, nullable=True)
    RatingOfficerComments = Column(String, nullable=True)
    DocumentShearePointLink = Column(String,nullable=False)
    DateOfSubmission = Column(DateTime(timezone=True), nullable=False)
    ProcessingSatus = Column(UUID(as_uuid=True), ForeignKey("document_statuses_table.status_Id"), nullable=False)
    AssignedTo = Column(UUID(as_uuid=True),ForeignKey("users.user_Id"),nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=func.now())
    UpdatedAt = Column(DateTime,nullable=True)