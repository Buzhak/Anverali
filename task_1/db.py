from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import (
    declarative_base, declared_attr, relationship, Mapped
)


class PreBase():
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)
engine = create_engine('sqlite:///names.db')


class BaseModel:
    title: Mapped[str] = Column(String(100), unique=True, nullable=False)


class Gender(Base, BaseModel):
    names: Mapped[list["Name"]] = relationship(back_populates='gender')


class Name(Base, BaseModel):
    gender_id: Mapped[int] = Column(Integer, ForeignKey('gender.id'))
    gender: Mapped[list["Gender"]] = relationship(back_populates='names')


# Создаём базу
Base.metadata.create_all(engine, tables=[Gender.__table__, Name.__table__])
