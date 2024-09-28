from models.database import SessionLocal
from models.employe import Employe


def creerEmploye(chefId, nom, prenom, motDePasse , telephone, addresse):
    session = SessionLocal()
    session.add(Employe(chefId = chefId, nom=nom, prenom=prenom, motDePasse=motDePasse, telephone=telephone, addresse=addresse))
    session.commit()
    session.close()

def obtenirEmployePar(nom, motDePasse):
    session = SessionLocal()
    employe = session.query(Employe).filter(Employe.nom == nom, Employe.motDePasse==motDePasse).first()
    session.close()
    return employe


def obtenirEmploye():
    session = SessionLocal()
    employes = session.query(Employe).all()
    session.close()
    return employes