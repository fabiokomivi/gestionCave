from models.database import SessionLocal
from models.chef import Chef


def creerChef(nom, prenom, motDePasse , telephone):
    session = SessionLocal()
    session.add(Chef(nom=nom, prenom=prenom, motDePasse=motDePasse, telephone=telephone))
    session.commit()
    session.close()

def obtenirChefPar(nom, motDePasse):
    session = SessionLocal()
    chefs = session.query(Chef).filter(Chef.nom == nom, Chef.motDePasse==motDePasse).first()
    session.close()
    return chefs


def obtenirChefs():
    session = SessionLocal()
    chefs = session.query(Chef).all()
    session.close()
    return chefs


