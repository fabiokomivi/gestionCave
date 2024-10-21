from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import MODEL


DATABASE_URL = "postgresql://fabio:fabio2002@localhost:5432/CaveDB1"
engine = create_engine(DATABASE_URL)


#creation des tables proproment dit
MODEL.metadata.create_all(engine)

#creer une session pour interagir avec la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


















