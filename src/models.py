from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    subscription_date : Mapped[str] = mapped_column(nullable=False)

    favorites = relationship("Favorite", back_populates="users")

class Character(Base):
    __tablename__ = 'characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    height: Mapped[int]
    gender: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(nullable=False)
    species: Mapped[str] = mapped_column(nullable=False)

    favorites = relationship("Favorite", back_populates="characters")
    
class Planet(Base):
    __tablename__ = 'planets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)

    favorites = relationship("Favorite", back_populates="planets")

class Favorite(Base):
    __tablename__ = 'favorites'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('users.id'))
    character_id : Mapped[int] = mapped_column(ForeignKey('characters.id'))
    planet_id : Mapped[int] = mapped_column(ForeignKey('planets.id'))

    users = relationship("User" , back_populates="favorites")
    characters = relationship("Character" , back_populates="favorites")
    planets = relationship("Planet" , back_populates="favorites")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
