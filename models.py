from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey
from typing import List
from typing import Optional


class Base(DeclarativeBase):
    pass


# order product Many to Many
association_table = Table(
    "orders_product",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    
    #  One o One Relationship
    profile: Mapped["Profile"] = relationship(back_populates="user")
    
    # One-to-Many (1:N)
    orders: Mapped[List["Order"]] = relationship(back_populates="user")

    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Profile(Base):
    __tablename__ = "profiles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    #  One o One Relationship
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="profile")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    total: Mapped[float]
    
    # Many-to-One (N:1)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")
    
    products: Mapped[List["Product"]] = relationship(
        secondary=association_table, back_populates="orders"
    )
   
    
class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    # Many to Many
    orders: Mapped[List["Order"]] = relationship(
        secondary=association_table, back_populates="products"
    )
    
