import statistics

transactions = [
    {"user": "alice", "amount": 42.50, "location": "NYC"},
    {"user": "alice", "amount": 38.10, "location": "NYC"},
    {"user": "alice", "amount": 5200.00, "location": "Lagos"},
    {"user": "bob", "amount": 15.00, "location": "LA"},
]
def flag_transaction(tx, user_history_amounts):
    if not user_history_amounts:
        return False
    avg = statistics.mean(user_history_amounts)
    stdev = statistics.pstdev(user_history_amounts) or 1
    z_score = (tx["amount"] - avg) / stdev
    return z_score > 2

history = {"alice": [42.50, 38.10],"bob": []}
# Check every transaction
for tx in transactions:
    result = flag_transaction(
        tx,
        history.get(tx["user"], [])
    )
    print(
        f"User: {tx['user']} | "
        f"Amount: ${tx['amount']} | "
        f"Location: {tx['location']} | "
        f"Fraud: {result}"
    )