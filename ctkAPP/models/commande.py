from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import MODEL
from datetime import datetime, timezone

class Commande(MODEL):
    __tablename__ = "Commandes"
    id = Column(Integer, primary_key=True, nullable=False)

    clientId = Column(Integer, ForeignKey("Clients.id"))
    client = relationship("Client", back_populates="commandes")
    dateCommande = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    employeId = Column(Integer, ForeignKey("Employes.id"))
    employe = relationship("Employe", back_populates="commandes")

    lignesCommande = relationship("LigneCommande", back_populates="commande")