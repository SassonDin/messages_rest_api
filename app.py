from flask import Flask, request, jsonify
# from flask_restful import Api, Resource
from SQL import db, Users, Messages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///APImessages.db"
db.init_app(app)


@app.before_first_request
def initialize_database():
    db.create_all()


@app.route('/', methods=['GET'])
def get():

    return "hgfhgcghghvhjvhjv"


@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.form.to_dict()
        Users(name=data['name']).save()
        return '200'
    except Exception as err:
        print(err)
        return '500'


@app.route('/write_message', methods=['POST'])
def write_message():
    try:
        data = request.form.to_dict()
        if Users.get_user_by_name(data['sender']) and Users.get_user_by_name(data['receiver']):
            Messages(content=data['content'], subject=data['subject'], is_read=False, sender=data['sender'], receiver=data['receiver']).save()
            return '200'
        else:
            return '500 either sender or receiver do not exist'
    except Exception as err:
        print(err)
        return '500'


@app.route('/get_user_messages/', methods=['GET'])
def get_user_messages():
    try:
        data = request.args.to_dict()
        if Users.get_user_by_name(data['name']):
            messages = Messages.get_messages_by_user(data['name'])
        return messages.jsonify()
    except Exception as err:
        print(err)
        return '500'


@app.route('/get_unread_messages', methods=['GET'])
def get_unread_messages():
    try:
        data = request.args.to_dict()
        if Users.get_user_by_name(data['name']):
            messages = Messages.get_unread_messages_by_user(data['name'])
        return_dic = dict()
        for message in messages:
            return_dic[message.id] = message.as_dict()
        return return_dic
    except Exception as err:
        print(err)
        return '500'


@app.route('/get_unread_message', methods=['GET'])
def get_unread_message():
    try:
        data = request.args.to_dict()
        if Users.get_user_by_name(data['name']):
            message = Messages.get_unread_message_by_user(data['name'])
        return message.as_dict()
    except Exception as err:
        print(err)
        return '500'


@app.route('/delete_message', methods=['POST'])
def delete_message():
    try:
        data = request.form.to_dict()
        if Users.get_user_by_name(data['sender']):
            Messages.delete_message_by_sender_receiver_content(data)
        return '200'
    except Exception as err:
        print(err)
        return '500'


if __name__ == '__main__':
    app.run(port="8081", debug=True)

