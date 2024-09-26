from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .base import MODEL


class Boisson(MODEL):
    __tablename__= "Boissons"
    id = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String, nullable=False)
    prix = Column(Integer, nullable=False)
    image = Column(LargeBinary, nullable=True)
    description = Column(String)

    categorieId = Column(Integer, ForeignKey("Categories.id"))
    categorie = relationship("Categorie", back_populates="boissons")

    stock = relationship("Stock", uselist=False, back_populates="boisson")