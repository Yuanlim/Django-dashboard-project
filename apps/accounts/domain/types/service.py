from typing import Generic, List, TypeVar, TypedDict

from django.db import models

from apps.accounts.domain.enums.risk_level import RiskLevel

T = TypeVar("T", bound=models.Model)

class ServiceResultType(TypedDict, Generic[T]):
    # When service finishes check this to whether create reports and response immediately to client
    error: bool
    # To frontend response
    client_response: List[str]
    # http 400, 404, 500... etc
    response_status: int
    # Documentation for monitoring
    to_logger: List[str]
    # Which service reports it
    from_service: str
    # Based on how important the service is
    risk_level: RiskLevel
    # Respond data
    obj : T | None