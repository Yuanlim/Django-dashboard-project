from enum import Enum


class RiskLevel(str, Enum):
    RISKY = "risky"
    WARN = "warn"
    NONE = "none"