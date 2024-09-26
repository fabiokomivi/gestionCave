from models.database import SessionLocal
from models.categorie import Categorie


def creerCategorie(nom, description):
    session = SessionLocal()
    session.add(Categorie(nom=nom, description=description))
    session.commit()
    session.close()


def obtenirCategorie():
    session = SessionLocal()
    categories = session.query(Categorie).all()
    session.close
    return categories