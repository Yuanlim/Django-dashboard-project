from typing import TypedDict

from apps.accounts.domain.enums.risk_level import RiskLevel


class ServiceResultType(TypedDict):
    # When service finishes check this to whether create reports and response immediately to client
    error: bool
    # To frontend response
    client_response: str
    # http 400, 404, 500... etc
    response_status: int
    # Documentation for monitoring
    to_logger: str
    # Which service reports it
    from_service: str
    # Based on how important the service is
    risk_level: RiskLevel