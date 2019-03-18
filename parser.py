from datetime import datetime

records = [{
    'author': 'Ilia',
    'date_created': datetime.now(),
    'title': 'Magnum opus',
    'description': 'bla bla',
    'pages': [
        'Lorem ipsum',
        'asdfasdf asdf asdf asfd',
        'asdf asdfa sdfa sdf',
    ],
}, {
    'author': 'Boyan',
    'date_created': datetime.now(),
    'title': 'Diplomna rabota',
    'description': 'bla bla',
    'pages': [
        'Shellcode',
        'bla bla shellcode bla bla',
        'asdf asdfa sdfa sdf',
    ],
}]

for record in records:
    print(record['title'])
