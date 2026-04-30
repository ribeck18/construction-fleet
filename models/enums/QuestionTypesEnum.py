from enum import Enum


class QuestionTypesEnum(Enum):
    CRITICAL = "critical"
    MECHANICAL = "mechanical"
    DAMAGE_WEAR = "damage_wear"
    SAFETY_EQUIPMENT = "safety_equipment"
    DOCUMENTS = "documents"
    OPERATION_CHECK = "operation_check"
