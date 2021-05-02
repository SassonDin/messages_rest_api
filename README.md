# messages_rest_api

id     method       name                    description
1)      POST      create_user             only users in the database can send and receive messages, to create and add a user to the database, send a user name in json format with POST method MUST be UNIQUE

example:  {'name': 'din}

2)      POST      write_message           send a message with POST method as specified in the example (name of sender and receiver must exist in the database beforehand!)

example: {'sender': 'din',
           'receiver': 'katya',
           'subject': 'herolo',
           'content': 'interview pending'
           }
3)      POST      delete_message          delets a message with POST method as specified in the example

example: {'sender: 'din',
          'receiver': 'katya',
          'content': 'interesting message content'
          }
          
4)      GET     get_messages_by_user      returns all messages (as a dictionary) owned by the user, send a user name as specified in the example with GET method

example: {'name': 'din}

5)      GET     get_unread_messages       returns all unread messages of a user (as a dictionary) and updates status to read, send a user name as specified in the example with GET method

example:  {'name': 'din}

6)      GET   get_unread_message          returns ONE unread message of a user (as a dictionary) and updates status to read, send a user name as specified in the example with GET method

example:  {'name': 'din}

