from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Float, DateTime
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
       

class Metal(Base):
    __tablename__ = 'metal'
    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    prices = relationship("Price", backref="metal")


class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True)

    price = Column(Float(asdecimal=True))
    created_at = Column(DateTime())
    metal_id = Column(Integer, ForeignKey("metal.id"))


class Database:

    def __init__(self, db_name):
        engine = create_engine(
            f'sqlite:///{db_name}',
            echo=False,
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def create_metal(self, metal):
        """Create the metal. If the metal exists, return False, otherwise return True.
        """
        obj = self.session.query(
            Metal
        ).filter(
            Metal.name==metal
        ).first()
        
        if obj:
            return obj
        
        obj = Metal(name=metal)
        self.session.add(obj)
        self.session.commit()
        
        return obj
    
    def create_price(self, price, created_at, metal):
        obj = self.session.query(
            Price
        ).filter(
            Price.price==price
        ).filter(
            Price.created_at==created_at
        ).filter(
            metal==metal
        ).first()
        
        if obj:
            return False
            
        metal_obj = self.create_metal(metal)
        
        obj = Price(
            price=price,
            created_at=created_at,
            metal=metal_obj,
        )
        self.session.add(obj)
        self.session.commit()
        
        return obj
    
    def get_metals(self):
        return self.session.query(Metal).all()
    
    def get_prices(self):
        return self.session.query(Price).all()
