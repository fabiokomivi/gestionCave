from models.database import SessionLocal
from models.chef import Chef
import hashlib


def hasher(password):
    passwordBytes = password.encode('utf-8')
    passwordHash = hashlib.sha256(passwordBytes)
    return passwordHash.hexdigest()


def creerChef(nom, prenom, motDePasse , telephone, email):
    session = SessionLocal()
    session.add(Chef(nom=nom, prenom=prenom, motDePasse=motDePasse, telephone=telephone, email=email))
    session.commit()
    session.close()

def obtenirChefPar(nom=None, motDePasse=None, addresse=None):
    session = SessionLocal()
    chefs = session.query(Chef)
    if nom:
        chefs = session.query(Chef).filter(Chef.nom.ilike(f"%{nom}%"))
    if motDePasse:
        chefs = session.query(Chef).filter(Chef.motDePasse==hasher(motDePasse))
    if addresse:
        chefs = session.query(Chef).filter(Chef.email==addresse)

    session.close()
    return chefs.first()


def obtenirChefs():
    session = SessionLocal()
    chefs = session.query(Chef).all()
    session.close()
    return chefs

def modifierChef(email, password):
    session = SessionLocal()
    if email:
        chef = session.query(Chef).filter(Chef.email==email).first()
        if chef:
            chef.email=email
            chef.motDePasse=password
            session.commit()
    session.close()
        



