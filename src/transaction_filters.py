import re


def filter_by_description(transactions, search_string):
    pattern = re.compile(re.escape(search_string.lower()))

    filtered_transactions = [
        transaction for transaction in transactions
        if "description" in transaction and pattern.search(transaction["description"].lower())
    ]

    return filtered_transactions
