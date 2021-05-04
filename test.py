import requests

BASE = 'http://127.0.0.1:8081/'
message = {'content': 'sdfsdfsdfdsf',
           'subject': 'coro',
           'sender': 'din',
           'receiver': 'katya'
           }
username = {'name': 'din'}
# response = requests.post(BASE + 'create_user', data=myobj)
# print(response.text)
code = '200'
while code != '500':
    username['name'] = input()
    code = requests.post(url=BASE + 'create_user', data=username).text

    # message['sender'] = input('sender: ')
    # message['receiver'] = input('receiver: ')
    # message['subject'] = input('subject: ')
    # message['content'] = input('content: ')
    # code = requests.post(url=BASE + 'write_message', data=message).text[:3]

    # username['name'] = input('username: ')
    # code = requests.get(url=BASE + 'get_unread_messages', params=username)

    # message['sender'] = input('sender: ')
    # message['receiver'] = input('receiver: ')
    # message['content'] = input('content: ')
    # code = requests.post(url=BASE + 'delete_message', data=message).text[:3]

