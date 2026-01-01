import csv

THRESHOLD = 0.01  # 1% tolerance for mismatch

def pct_diff(expected, received):
    if expected == 0:
        return 0.0 if received == 0 else 1.0
    return abs(expected - received) / expected

rows = []
with open("sample_transactions.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        expected = float(r["expected_amount"])
        received = float(r["received_amount"])
        fee = float(r["fee"])
        status = r["status"]

        mismatch = pct_diff(expected, received) > THRESHOLD
        fee_explains = abs((expected - received) - fee) < 1e-6

        rows.append({
            "tx_id": r["tx_id"],
            "asset": r["asset"],
            "expected": expected,
            "received": received,
            "fee": fee,
            "status": status,
            "mismatch_flag": mismatch,
            "fee_explains_diff": fee_explains,
        })

print("tx_id asset expected received fee status mismatch fee_explains")
for r in rows:
    print(
        f'{r["tx_id"]:>4} {r["asset"]:>5} {r["expected"]:>8.4f} {r["received"]:>8.4f} '
        f'{r["fee"]:>6.4f} {r["status"]:>7} {str(r["mismatch_flag"]):>8} {str(r["fee_explains_diff"]):>12}'
    )
