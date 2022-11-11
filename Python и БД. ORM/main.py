import datetime
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f"Publisher {self.id}: {self.name}"

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="books")

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="stocks")

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sales")

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


DSN = "postgresql://postgres:123123@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name="Publisher")
publisher2 = Publisher(name="Publisher2")
book = Book(title="Book", publisher=publisher1)
shop = Shop(name="Shop")
stock = Stock(count=5, book=book, shop=shop)
sale = Sale(price=5000, date_sale=datetime.date.today(), count=10, stock=stock)

session.add_all([publisher1, publisher2, book, shop, stock, sale])
session.commit()

publisher_info = input()
pub_filter = Publisher.id == int(publisher_info) if publisher_info.isdigit() else Publisher.name == publisher_info

q = session.query(Publisher, Book, Stock, Shop, Sale).select_from(Publisher).join(Book).join(Stock).join(Shop, Stock.id_shop == Shop.id).join(Sale).filter(pub_filter)
for s in q:
    publisher, book, stock, shop, sale = s
    print(f"{book.title} | {shop.name} | {sale.price} | {sale.date_sale}")

session.close()