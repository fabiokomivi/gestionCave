from models.database import SessionLocal
from models.boisson import Boisson


def creerBoisson(nom, prix, image, description):
    session = SessionLocal()
    session.add(Boisson(nom=nom, prix=prix, image=image, description=description))
    session.commit()
    session.close()


def obtenirBoisson():
    session = SessionLocal()
    boissons = session.query(Boisson).all()
    session.close
    return boissons