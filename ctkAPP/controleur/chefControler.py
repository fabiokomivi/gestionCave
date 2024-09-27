from models.database import SessionLocal
from models.chef import Chef


def creerChef(nom, prenom, telephone):
    session = SessionLocal()
    session.add(Chef(nom=nom, prenom=prenom, telephone=telephone))
    session.commit()
    session.close()

def obtenirChefPar(nom, motDePasse):
    session = SessionLocal()
    session.query(Chef).filter()


def obtenirChefs():
    session = SessionLocal()
    chefs = session.query(Chef).all()
    session.close
    return chefs