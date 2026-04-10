from typing import Generic, Optional, TypeVar
from django.db import models

from apps.accounts.domain.enums.risk_level import RiskLevel
from apps.accounts.domain.types.service import ServiceResultType

T = TypeVar("T", bound=models.Model)
        

class ServiceBase(Generic[T]):
    
    def __init__(self):
        # Altered obj itself
        self.obj: Optional[T] = None
        self.service_result: ServiceResultType | None = None
        
    @property
    def pk(self):
        """
        Primary key of the object
        """
        if self.obj is None:
            return None
        
        return self.obj.pk