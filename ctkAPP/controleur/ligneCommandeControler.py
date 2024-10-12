from models.database import SessionLocal
from models.ligneCommande import LigneCommande
from sqlalchemy.exc import SQLAlchemyError

def AjouterLigneCommande(commandeId, boissonId, quantite, prix, prixTotal):
    session = SessionLocal()
    nouvelleLigneCommande = LigneCommande(commandeId=commandeId, boissonId=boissonId, quantite=quantite, prix=prix, prixTotal=prixTotal)
    session.add(nouvelleLigneCommande)
    session.commit()



def RecupererLigneCommandeParId(ligneCommandeId):
    session = SessionLocal()
    ligneCommande = session.query(LigneCommande).filter_by(Id=ligneCommandeId).first()
    return ligneCommande


def ModifierLigneCommande(ligneCommandeId, nouvelleQuantite=None, nouveauPrixUnitaire=None):
    session = SessionLocal()
    ligneCommande = session.query(LigneCommande).filter_by(Id=ligneCommandeId).first()
    if ligneCommande:
        if nouvelleQuantite is not None:
            ligneCommande.Quantite = nouvelleQuantite
        if nouveauPrixUnitaire is not None:
            ligneCommande.PrixUnitaire = nouveauPrixUnitaire
        session.commit()



def SupprimerLigneCommande(ligneCommandeId):
    session = SessionLocal()
    ligneCommande = session.query(LigneCommande).filter_by(Id=ligneCommandeId).first()
    if ligneCommande:
        session.delete(ligneCommande)
        session.commit()


def obtenirLigneDeCommandes(commandeId):
    session = SessionLocal()
    lignesCommande = session.query(LigneCommande).filter_by(commandeId=commandeId).all()
    return lignesCommande

