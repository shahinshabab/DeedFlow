from .schema import EMPTY_REGISTRATION_DATA


def normalize_registration_data(data):
    normalized = EMPTY_REGISTRATION_DATA.copy()
    normalized.update(data or {})
    normalized['executants'] = normalized.get('executants') or []
    normalized['claimants'] = normalized.get('claimants') or []
    normalized['property_details'] = normalized.get('property_details') or EMPTY_REGISTRATION_DATA['property_details']
    return normalized
