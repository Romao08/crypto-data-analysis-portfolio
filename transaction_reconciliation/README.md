# Transaction Reconciliation (Example)

This project demonstrates how to reconcile transaction-level data in a crypto / fintech context, focusing on detecting mismatches between expected and received amounts, with special attention to fee impact.

The example mirrors common real-world scenarios such as:
- Users sending an amount without accounting for network fees
- Partial settlements
- Amount mismatches that require investigation

---

## Problem

Given a set of transactions with:
- an expected amount
- an actual received amount
- an associated transaction fee

we want to identify cases where the received amount does not match expectations and classify the root cause.

---

## What the script does

The `analysis.py` script:
- Loads transaction data from a CSV file
- Compares expected vs received amounts
- Accounts for transaction fees
- Flags discrepancies and categorizes them (e.g. fee-related mismatch)
- Produces a clear reconciliation output that can be used by operations or support teams

This logic is commonly used in payment operations, exchanges, wallets, and blockchain analytics.

---

## Dataset

- `sample_transactions.csv`
- Simplified and fully simulated data
- No real user or proprietary information

---

## How to run

```bash
pip install pandas
python analysis.py
