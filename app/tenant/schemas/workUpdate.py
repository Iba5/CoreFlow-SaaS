from pydantic import BaseModel
from typing import Optional


class AddWorker(BaseModel):
    id:         str
    leader:     Optional[str]
    IsActive:   bool
    