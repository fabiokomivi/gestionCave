from models.database import SessionLocal
from models.client import Client


def creerClient(nom, prenom, telephone, addresse):
    session = SessionLocal()
    session.add(Client(nom=nom, prenom=prenom, telephone=telephone, addresse=addresse))
    session.commit()
    session.close()


def obtenirClients():
    session = SessionLocal()
    clients = session.query(Client).all()
    session.close
    return clients