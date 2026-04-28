from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    DOWN = "down"
    IN_SHOP = "in_shop"
    NEEDS_ATTENTION = "needs_attention"
