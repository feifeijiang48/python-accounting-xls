data_models
"""
Data Models for Consolidation

Extended models to support consolidation-specific operations.
"""

from dataclasses import dataclass
from typing import Optional, List
from decimal import Decimal
from enum import Enum


class RuleType(Enum):
    """Types of consolidation rules."""
    ELIMINATION = "elimination"
    ADJUSTMENT = "adjustment"
    TRANSLATION = "translation"
    NCI_CALCULATION = "nci_calculation"


class EliminationType(Enum):
    """Types of inter-company eliminations."""
    SALES = "sales"
    RECEIVABLES_PAYABLES = "receivables_payables"
    DIVIDENDS = "dividends"
    PROFITS = "profits"


@dataclass
class ConsolidationEntity:
    """Represents an entity in the consolidation group."""
    id: str
    name: str
    parent_id: Optional[str] = None
    ownership_percentage: Decimal = Decimal("100.00")
    functional_currency: str = "USD"
    reporting_currency: str = "USD"
    is_subsidiary: bool = True
    equity_method: bool = False
    
    def is_fully_owned(self) -> bool:
        """Check if entity is fully owned."""
        return self.ownership_percentage == Decimal("100.00")
    
    def get_nci_percentage(self) -> Decimal:
        """Get non-controlling interest percentage."""
        return 100 - self.ownership_percentage


@dataclass
class ConsolidationAccount:
    """Represents an account in consolidation."""
    code: str
    name: str
    account_type: str  # Asset, Liability, Capital, Income, Expense
    sub_type: Optional[str] = None
    consolidation_group: Optional[str] = None
    is_inter_company: bool = False


@dataclass
class EliminationRule:
    """Represents an inter-company elimination rule."""
    id: str
    rule_type: RuleType
    elimination_type: Optional[EliminationType] = None
    entity_a: Optional[str] = None
    entity_b: Optional[str] = None
    account: Optional[str] = None
    description: str = ""
    is_active: bool = True


@dataclass
class ConsolidationAdjustment:
    """Represents a consolidation adjustment."""
    id: str
    description: str
    entity: str
    account: str
    amount: Decimal
    debit_credit: str  # "Debit" or "Credit"
    reason: str = ""
    is_reversing: bool = False


@dataclass
class ExchangeRate:
    """Represents an exchange rate."""
    from_currency: str
    to_currency: str
    rate: Decimal
    date: str
    source: str = "manual"