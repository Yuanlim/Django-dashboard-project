from typing import Generic, Optional, Type, TypeVar

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import force_str
from rest_framework import status

from apps.accounts.domain.enums.risk_level import RiskLevel
from apps.accounts.domain.types.service import ServiceResultType

T = TypeVar("T", bound=models.Model)
        

class ServiceBase(Generic[T]):
    
    def __init__(self, model_type: Type[T], service_name: str):
        # For service result report
        self.model_type = model_type
        self.service_name = service_name
        
        # Altered obj itself
        self.obj: Optional[T] = None
        self.service_result: ServiceResultType[T] = {
            "error": True,
            "to_logger": [],
            "risk_level": RiskLevel.NONE,
            "client_response": [],
            "from_service": self.service_name,
            "response_status": status.HTTP_200_OK,
            "obj": None 
        }
        
        
    def error_to_result(
        self, error: ValidationError, 
        risk_level: RiskLevel,
        response_status: int,
        ):
        
        self.service_result = {
            "error": True,
            "to_logger": [],
            "risk_level": risk_level,
            "client_response": [],
            "from_service": self.service_name,
            "response_status": response_status,
            "obj": None
        }
        
        if hasattr(error, "message_dict"):
            for field, messages in error.message_dict.items():
                first_msg = messages[0]
                self.service_result["client_response"].append(first_msg)
                self.service_result["to_logger"].append(f"{field}: {first_msg}")
        else:
            for msg in error.messages:
                self.service_result["client_response"].append(msg)
                self.service_result["to_logger"].append(msg)
            
            
    def success_result(self):
        self.service_result = {
            "error": False,
            "to_logger": [],
            "risk_level": RiskLevel.NONE,
            "client_response": [],
            "from_service": self.service_name,
            "response_status": status.HTTP_200_OK,
            "obj": self.obj
        }
        
        
    def search_name_404_result(self, search_keyword: str, additional_msg: Optional[str]):
        self.service_result = {
            "error": True,
            "to_logger": [],
            "risk_level": RiskLevel.NONE,
            "client_response": [f"{self.model_name} named {search_keyword} does not exist.{additional_msg}"],
            "from_service": self.service_name,
            "response_status": status.HTTP_404_NOT_FOUND,
            "obj": None
        }
        
        
    def search_pk_404_result(self, pk: int):
        self.service_result = {
            "error": True,
            "to_logger": [
                f"Client has no direct access to pk search, but failed highly due to a bug. '{self.model_name} with id {pk}'"
            ],
            "risk_level": RiskLevel.WARN,
            "client_response": ["Something when wrong..."],
            "from_service": self.service_name,
            "response_status": status.HTTP_404_NOT_FOUND,
            "obj": None
        }
        
        
    @property
    def pk(self):
        """
        Primary key of the object
        """
        if self.obj is None:
            return None
        
        return self.obj.pk
    
    
    @property
    def model_name(self):
        """
        The model name that this base assign to.
        """
        return self.model_type.__name__
        