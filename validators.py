validators
"""
Data Validators for Consolidation

Validates data integrity and completeness.
"""

import pandas as pd
from typing import Tuple, List
import logging

logger = logging.getLogger(__name__)


class ConsolidationValidator:
    """Validates consolidation data."""
    
    @staticmethod
    def validate_chart_of_accounts(df: pd.DataFrame) -> Tuple[bool, List[str]]:
        """
        Validate Chart of Accounts structure.
        
        Args:
            df: DataFrame with chart data
            
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        
        # Check required columns
        required_cols = ['Account Code', 'Account Name', 'Account Type']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            errors.append(f"Missing columns in Chart of Accounts: {missing_cols}")
        
        # Check for duplicates
        if 'Account Code' in df.columns:
            duplicates = df[df['Account Code'].duplicated()]['Account Code'].unique()
            if len(duplicates) > 0:
                errors.append(f"Duplicate account codes: {duplicates.tolist()}")
        
        # Check for valid account types
        valid_types = ['Asset', 'Liability', 'Capital', 'Income', 'Expense']
        if 'Account Type' in df.columns:
            invalid_types = df[~df['Account Type'].isin(valid_types)]['Account Type'].unique()
            if len(invalid_types) > 0:
                errors.append(f"Invalid account types: {invalid_types.tolist()}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_trial_balance(df: pd.DataFrame) -> Tuple[bool, List[str]]:
        """
        Validate Trial Balance structure.
        
        Args:
            df: DataFrame with trial balance data
            
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        
        # Check required columns
        required_cols = ['Account Code', 'Debit', 'Credit']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            errors.append(f"Missing columns in Trial Balance: {missing_cols}")
        
        # Check debit-credit balance
        if 'Debit' in df.columns and 'Credit' in df.columns:
            total_debit = pd.to_numeric(df['Debit'], errors='coerce').sum()
            total_credit = pd.to_numeric(df['Credit'], errors='coerce').sum()
            
            if abs(total_debit - total_credit) > 0.01:
                errors.append(
                    f"Trial Balance not in balance: "
                    f"Debit={total_debit:.2f}, Credit={total_credit:.2f}"
                )
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_consolidation_rules(df: pd.DataFrame) -> Tuple[bool, List[str]]:
        """
        Validate Consolidation Rules structure.
        
        Args:
            df: DataFrame with consolidation rules
            
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        
        if df is None or df.empty:
            errors.append("Consolidation rules file is empty")
            return False, errors
        
        return True, errors