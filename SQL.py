from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_


db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name=None):
        self.name = name

    def save(self):
        try:
            # inject self into db session
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as Err:
            db.session.rollback()
            return Err

    @staticmethod
    def get_user_by_name(name):
        return db.session.query(Users).filter_by(name=name).first()


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(50))
    receiver = db.Column(db.String(50))
    content = db.Column(db.String(500))
    subject = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime)
    is_read = db.Column(db.Boolean)

    def __init__(self, content=None, subject=None, is_read=False, sender=None, receiver=None):
        self.content = content
        self.subject = subject
        self.creation_date = datetime.now()
        self.is_read = is_read
        self.sender = sender
        self.receiver = receiver

    def save(self):
        try:
            # inject self into db session
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as Err:
            db.session.rollback()
            print(Err)

    def as_dict(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'receiver': self.receiver,
            'subject': self.subject,
            'content': self.content,
            'creation_date': self.creation_date
        }

    @staticmethod
    def get_messages_by_user(name):
        return db.session.query(Messages).filter_by(sender=name).all()

    @staticmethod
    def get_unread_message_by_user(name):
        message = db.session.query(Messages).filter_by(receiver=name).first()
        try:
            db.session.query(Messages).filter_by(id=message.id).update({'is_read': True})
            db.session.commit()
            return message
        except Exception as Err:
            print(Err)
            db.session.rollback()
            return False

    @staticmethod
    def get_unread_messages_by_user(name):
        messages = db.session.query(Messages).filter(and_(Messages.receiver == name, ~Messages.is_read)).all()
        try:
            for message in messages:
                db.session.query(Messages).filter_by(id=message.id).update({'is_read': True})
            db.session.commit()
            return messages
        except Exception as Err:
            print(Err)
            db.session.rollback()
            return False

    @staticmethod
    def delete_message_by_sender_receiver_content(data):
        try:
            message = db.session.query(Messages).filter(and_(
                Messages.sender == data['sender'], Messages.receiver == data['receiver'], Messages.content == data['content']))
            message.delete()
            db.session.commit()
        except Exception as Err:
            print(Err)
            db.session.rollback()
            return False








