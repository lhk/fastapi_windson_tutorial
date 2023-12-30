from configs.production import DATABASE_URI
from typing import Optional
from sqlmodel import Field, SQLModel, Session, select, create_engine



class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str

hero_1 = Hero(name="Deadpond")
hero_2 = Hero(name="Spider-Boy")
engine = create_engine(DATABASE_URI)


with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(statement).first()
    print(hero)