from models.database import SessionLocal
from models.commande import Commande
from models.ligneCommande import LigneCommande
from models.boisson import Boisson
from models.categorie import Categorie
from models.employe import Employe
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from sqlalchemy import func

# Créer une nouvelle commande
def creerCommande(clientId, employeId):
    session = SessionLocal()  # Créer une session pour interagir avec la base de données
    nouvelleCommande = Commande(clientId=clientId, employeId=employeId)

    session.add(nouvelleCommande)
    session.commit()
    session.refresh(nouvelleCommande)

    commande = session.query(Commande).options(joinedload(Commande.client)).get(nouvelleCommande.id)
    session.close()
    return commande

# Obtenir toutes les commandes
def obtenirCommandePar(commandeId=None, date=None, clientId=None,tous=False):
    session = SessionLocal()

    commandes = session.query(Commande).options(joinedload(Commande.client),
                                                joinedload(Commande.lignesCommande).joinedload(LigneCommande.boisson)
                                                )
    if tous:
        commandes = commandes.all()
    if commandeId:
        commandes = commandes.filter(Commande.id==commandeId).first()
    if date:
        commandes = commandes.filter(func.date_trunc('second', Commande.dateCommande) == date).all()
    if clientId:
        commandes = commandes.filter(Commande.clientId==clientId).all()
    session.close()
    return commandes


# Mettre à jour une commande
def mettre_a_jour_commande(commande_id, clientId=None, employeId=None):
    session = SessionLocal()
    
    try:
        commande = session.query(Commande).filter_by(id=commande_id).first()
        if commande:
            if clientId:
                commande.clientId = clientId
            if employeId:
                commande.employeId = employeId
            session.commit()
            return commande
        else:
            print(f"Commande avec ID {commande_id} introuvable.")
            return None
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erreur lors de la mise à jour de la commande: {str(e)}")
        return None
    finally:
        session.close()

# Supprimer une commande
def supprimerCommande(commande_id):
    session = SessionLocal()
    
    try:
        commande = session.query(Commande).filter_by(id=commande_id).first()
        if commande:
            session.delete(commande)
            session.commit()
            return True
        else:
            print(f"Commande avec ID {commande_id} introuvable.")
            return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erreur lors de la suppression de la commande: {str(e)}")
        return False
    finally:
        session.close()


def obtenirVentesParCategorie():
    session = SessionLocal()
    resultats = session.query(Categorie.nom, func.sum(LigneCommande.prixTotal)).\
                join(Boisson, Boisson.categorieId == Categorie.id).\
                join(LigneCommande, LigneCommande.boissonId == Boisson.id).\
                group_by(Categorie.nom).all()
    session.close()
    
    categories = [resultat[0] for resultat in resultats]
    ventes = [resultat[1] for resultat in resultats]
    
    return categories, ventes


def obtenirVentesParBoisson():
    # Connexion à la base de données et récupération des données
    session = SessionLocal()
    resultats = session.query(Boisson.nom, func.sum(LigneCommande.prixTotal)).\
                join(LigneCommande, LigneCommande.boissonId == Boisson.id).\
                group_by(Boisson.nom).all()
    session.close()
    
    boissons = [resultat[0] for resultat in resultats]
    ventes = [resultat[1] for resultat in resultats]
    
    return boissons, ventes

def obtenirVenteParEmployes():
    session = SessionLocal()
    resultats = session.query(
        Employe.nom,
        Employe.prenom,
        func.sum(LigneCommande.prixTotal)
    ).join(Commande, Commande.employeId == Employe.id) \
        .join(LigneCommande, LigneCommande.commandeId == Commande.id) \
        .group_by(Employe.nom, Employe.prenom) \
        .all()

    session.close()

    employes = [f"{resultat[0]} {resultat[1]}" for resultat in resultats]
    ventes = [resultat[2] for resultat in resultats]

    return employes, ventes

