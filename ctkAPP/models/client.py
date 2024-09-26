from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import MODEL

class Client(MODEL):
    __tablename__= "Clients"
    id = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    addresse = Column(String, nullable=False)

    commandes = relationship("Commande", back_populates="client")