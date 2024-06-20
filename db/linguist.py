from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
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
        is_user_exist = True if user is not None else False
        session.delete(user) if is_user_exist else None
        return is_user_exist


class Deck(Base):
    __tablename__ = 'deck'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    @staticmethod
    def deck_create(name, user_id):
        new_deck = Deck(name=name, user_id=user_id)
        session.add(new_deck)
        return new_deck

    @staticmethod
    def deck_get_by_id(deck_id):
        query = session.query(Deck)
        return query.select_from(Deck).filter_by(id=deck_id).first()

    @staticmethod
    def deck_update(deck_id, name):
        update_deck = Deck.deck_get_by_id(deck_id)
        update_deck.name = name
        return update_deck

    @staticmethod
    def deck_delete_by_id(deck_id):
        deck = Deck.deck_get_by_id(deck_id)
        is_deck_exist = True if deck is not None else False
        session.delete(deck) if is_deck_exist else None
        return is_deck_exist


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

    @staticmethod
    def card_create(user_id, word, translation, tip):
        new_card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
        session.add(new_card)
        return new_card

    @staticmethod
    def card_get_by_id(card_id):
        query = session.query(Card)
        return query.select_from(Card).filter_by(id=card_id).first()

    @staticmethod
    def card_filter(sub_word):
        query = session.query(Card)
        return tuple(query.filter(
            (Card.word.ilike(sub_word)) | (Card.translation.ilike(sub_word)) | (Card.tip.ilike(sub_word))).all())

    @staticmethod
    def card_update(card_id, word=None, translation=None, tip=None):
        update_card = Card.card_get_by_id(card_id)
        update_card.word = word
        update_card.translation = translation
        update_card.tip = tip
        return update_card

    @staticmethod
    def card_delete_by_id(card_id):
        card = Card.card_get_by_id(card_id)
        is_card_exist = True if card is not None else False
        session.delete(card) if is_card_exist else None
        return is_card_exist


Base.metadata.create_all(engine)

# User.user_create('test', 'email', 'pass')

# User.user_get_by_id(1)
# print(User.user_update_name(1, "main").name)
# print(User.user_change_password(1, 'pass', 'new_pass'))
# print(User.user_delete_by_id(1))

# Card.card_create('2', 'word1', 'translation1', 'tip1')
# result = Card.card_filter('tip')
# print(result)
# Card.card_update(1, 'word', 'test', 'test')
# Card.card_delete_by_id(1)
# session.commit()
