from pydantic import BaseModel
from datetime import datetime

class DangerousLink(BaseModel):
    full_url: str 
    domain_name: str 
    is_deprecated: bool 
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))