from sqlalchemy import create_engine, Column, Integer, Unicode, UnicodeText, ForeignKey, String, select
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/Test")
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    deck = relationship("Deck", back_populates="user")
    card = relationship("Card", back_populates="user")

    @staticmethod
    def user_create(name, email, password):
        new_user = User(name=name, email=email, password=password)
        session.add(new_user)
        return new_user

    @staticmethod
    def user_get_by_id(user_id):
        query = session.query(User)
        return query.select_from(User).filter_by(id=user_id).first()

    @staticmethod
    def user_update_name(user_id, name):
        update_user = User.user_get_by_id(user_id)
        update_user.name = name
        return update_user

    @staticmethod
    def user_change_password(user_id, old_password, new_password):
        user = User.user_get_by_id(user_id)
        is_same_password = user.password == old_password
        if is_same_password:
            user.password = new_password
        return is_same_password

    @staticmethod
    def user_delete_by_id(user_id):
        user = User.user_get_by_id(user_id)
        session.delete(user) if user is not None else print("User does not exist")
        return True if user is not None else False

class Deck(Base):
    __tablename__ = 'deck'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="deck")


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    word = Column(String)
    email = Column(String)
    translation = Column(String)
    tip = Column(String)
    user = relationship("User", back_populates="card")


# Base.metadata.create_all(engine)

User.user_create('test', 'email', 'pass')

# User.user_get_by_id(1)
# print(User.user_update_name(1, "main").name)
# print(User.user_change_password(1, 'pass', 'new_pass'))
print(User.user_delete_by_id(1))

session.commit()
