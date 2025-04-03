from collections import Counter


def count_operations_by_category(transactions):
    categories = [transaction.get("description", "Unknown") for transaction in transactions]
    return dict(Counter(categories))
