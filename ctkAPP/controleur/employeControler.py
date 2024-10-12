from models.database import SessionLocal
from models.employe import Employe


def creerEmploye(chefId, nom, prenom, telephone, addresse, motDePasse ):
    session = SessionLocal()
    session.add(Employe(chefId = chefId, nom=nom, prenom=prenom, motDePasse=motDePasse, telephone=telephone, addresse=addresse))
    session.commit()
    session.close()

def obtenirEmployePar(nom=None, prenom=None, telephone=None, addresse=None):
    session = SessionLocal()
    try:
        query = session.query(Employe)
        
        if telephone:
            query = query.filter(Employe.telephone.ilike(f"%{telephone}%"))
        
        if addresse:
            query = query.filter(Employe.addresse.ilike(f"%{addresse}%"))
        if nom:
            query = query.filter(Employe.nom.ilike(f"%{nom}%"))
        if prenom:
            query = query.filter(Employe.prenom.ilike(f"%{prenom}%"))
        
        employes = query.all()
        return employes

    finally:
        session.close()


def obtenirEmploye():
    session = SessionLocal()
    employes = session.query(Employe).all()
    session.close()
    return employes

def modifierEmploye(employeId, nom=None, prenom=None, telephone=None, addresse=None, mdp=None):
    # Ouvrir une session
    session = SessionLocal()
    employe = session.query(Employe).filter(Employe.id == employeId).first()
    if employe is None:
        session.close()
        return False
    if nom:
        employe.nom = nom
    if prenom:
        employe.prenom = prenom
    if telephone:
        employe.telephone = telephone
    if addresse:
        employe.addresse = addresse
    if mdp:
        employe.motDePasse = mdp
    session.commit()
    session.close()
    return True

def supprimerEmploye(employeId):
    session = SessionLocal()
    employe = session.query(Employe).filter(Employe.id==employeId).first()
    if employe:
        session.delete(employe)
        session.commit()
        session.close()
        return True
    else:
        session.close()
        return False
