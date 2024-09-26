from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import MODEL

class Commande(MODEL):
    __tablename__ = "Commandes"
    id = Column(Integer, primary_key=True, nullable=False)

    clientId = Column(Integer, ForeignKey("Clients.id"))
    client = relationship("Client", back_populates="commandes")

    employeId = Column(Integer, ForeignKey("Employes.id"))
    employe = relationship("Employe", back_populates="commandes")