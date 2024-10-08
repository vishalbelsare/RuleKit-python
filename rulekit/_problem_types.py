from enum import Enum


class ProblemType(Enum):
    CLASSIFICATION = 1
    REGRESSION = 2
    SURVIVAL = 3
    CONTRAST_CLASSIFICATION = 4
    CONTRAST_REGRESSION = 5
    CONTRAST_SURVIVAL = 6
