

ADVERTISEMENT_CREATE = {
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'date_of_creation': {
            'type': 'datetime',
            'pattern': 'dd/MMM/yyyy'
        },
        'owner': {
            'type': 'string'
        }
    },
    'required': ['title', 'description', 'date_of_creation', 'owner']
}