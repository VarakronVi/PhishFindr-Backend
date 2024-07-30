from typing import Union, Any
from database import models

def individual_data(link: Union[Any, None]) -> Union[models.DangerousLink, None]: 
    if not link:
        return None
    return {
        "id": str(link['_id']),
        "full_url": link['full_url'],
        "domain_name": link['domain_name'],
        "is_deprecated": link['is_deprecated'],
        "created_at": link['created_at'],
        "updated_at": link['updated_at'],
    }