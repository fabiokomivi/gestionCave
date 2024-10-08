from models.database import SessionLocal
from models.boisson import Boisson
from models.stock import Stock


def creerBoisson(nom, prix,  categorieId, image=""):
    session = SessionLocal()
    if image:
        boisson = Boisson(nom=nom, prix=prix, image=image, categorieId=categorieId)
        stock = Stock(quantite=0, boisson=boisson)
        session.add(boisson)
        session.add(stock)
    else:
        boisson = Boisson(nom=nom, prix=prix, categorieId=categorieId)
        stock = Stock(quantite=0, boisson=boisson)
        session.add(boisson)
        session.add(stock)
    session.commit()
    session.close()
    return True


def obtenirBoissonParAttribue(boissonId="", nom="", prix=0, tous=False):
    session = SessionLocal()
    boissons = session.query(Boisson)
    if tous:
        session.close()
        return boissons.all()
    if boissonId:
        boissons=boissons.filter(Boisson.id==boissonId)
    if prix:
        boissons=boissons.filter(Boisson.prix==prix)
    if nom:
        boissons = boissons.filter(Boisson.nom.ilike(f"%{nom}%"))
    session.close
    return boissons.all()

def modifierBoisson(boissonId, nom, prix, categorieId, image):
    session = SessionLocal()
    boisson = session.query(Boisson).filter(Boisson.id==boissonId).first()
    if nom:
        boisson.nom=nom
    if prix:
        boisson.prix = prix
    if image:
        boisson.image = image
    if categorieId:
        boisson.categorieId=categorieId
    session.commit()
    session.close()
    return True

def supprimerBoisson(boissonId):
    session = SessionLocal()
    boisson = session.query(Boisson).filter(Boisson.id==boissonId).first()
    if boisson:
        session.delete(boisson)
        session.commit()
    session.close()
    return True
