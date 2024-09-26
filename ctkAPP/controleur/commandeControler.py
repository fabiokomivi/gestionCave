from models.database import SessionLocal
from models.commande import Commande
from sqlalchemy.exc import SQLAlchemyError

# Créer une nouvelle commande
def creer_commande(client_id, employe_id):
    session = SessionLocal()  # Créer une session pour interagir avec la base de données
    nouvelle_commande = Commande(clientId=client_id, employeId=employe_id)
    
    try:
        session.add(nouvelle_commande)
        session.commit()
        session.refresh(nouvelle_commande)
        return nouvelle_commande
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erreur lors de la création de la commande: {str(e)}")
        return None
    finally:
        session.close()

# Obtenir toutes les commandes
def obtenir_commandes():
    session = SessionLocal()
    
    try:
        commandes = session.query(Commande).all()
        return commandes
    except SQLAlchemyError as e:
        print(f"Erreur lors de la récupération des commandes: {str(e)}")
        return []
    finally:
        session.close()

# Obtenir une commande par ID
def obtenir_commande_par_id(commande_id):
    session = SessionLocal()
    
    try:
        commande = session.query(Commande).filter_by(id=commande_id).first()
        return commande
    except SQLAlchemyError as e:
        print(f"Erreur lors de la récupération de la commande: {str(e)}")
        return None
    finally:
        session.close()

# Mettre à jour une commande
def mettre_a_jour_commande(commande_id, client_id=None, employe_id=None):
    session = SessionLocal()
    
    try:
        commande = session.query(Commande).filter_by(id=commande_id).first()
        if commande:
            if client_id:
                commande.clientId = client_id
            if employe_id:
                commande.employeId = employe_id
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
def supprimer_commande(commande_id):
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
