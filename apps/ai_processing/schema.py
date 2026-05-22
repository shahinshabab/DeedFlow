REGISTRATION_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'document_type': {'type': 'string'},
        'document_number': {'type': 'string'},
        'document_date': {'type': 'string'},
        'district': {'type': 'string'},
        'sro': {'type': 'string'},
        'consideration_amount': {'type': 'string'},
        'executants': {
            'type': 'array',
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'name': {'type': 'string'},
                    'address': {'type': 'string'},
                    'id_number': {'type': 'string'},
                },
                'required': ['name', 'address', 'id_number'],
            },
        },
        'claimants': {
            'type': 'array',
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'name': {'type': 'string'},
                    'address': {'type': 'string'},
                    'id_number': {'type': 'string'},
                },
                'required': ['name', 'address', 'id_number'],
            },
        },
        'property_details': {
            'type': 'object',
            'additionalProperties': False,
            'properties': {
                'taluk': {'type': 'string'},
                'village': {'type': 'string'},
                'desam': {'type': 'string'},
                'survey_number': {'type': 'string'},
                'extent': {'type': 'string'},
                'boundaries': {'type': 'string'},
            },
            'required': ['taluk', 'village', 'desam', 'survey_number', 'extent', 'boundaries'],
        },
        'notes': {'type': 'string'},
    },
    'required': [
        'document_type', 'document_number', 'document_date', 'district', 'sro',
        'consideration_amount', 'executants', 'claimants', 'property_details', 'notes'
    ],
}

EMPTY_REGISTRATION_DATA = {
    'document_type': '',
    'document_number': '',
    'document_date': '',
    'district': '',
    'sro': '',
    'consideration_amount': '',
    'executants': [],
    'claimants': [],
    'property_details': {
        'taluk': '',
        'village': '',
        'desam': '',
        'survey_number': '',
        'extent': '',
        'boundaries': '',
    },
    'notes': '',
}
