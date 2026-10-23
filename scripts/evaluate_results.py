
"""Calculate classification metrics from a manually reviewed results CSV.

Expected columns:
    ground_truth: positive or negative
    prediction: positive or negative

Only reviewed, complete rows are evaluated. This script does not run
static analyzers or establish ground truth by itself.
"""

import csv
import sys
from pathlib import Path


def calculate_metrics(rows):
    tp = fp = tn = fn = 0

    for row in rows:
        actual = row["ground_truth"].strip().lower()
        predicted = row["prediction"].strip().lower()

        if actual not in {"positive", "negative"}:
            raise ValueError(f"Invalid ground_truth: {actual!r}")
        if predicted not in {"positive", "negative"}:
            raise ValueError(f"Invalid prediction: {predicted!r}")

        if actual == "positive" and predicted == "positive":
            tp += 1
        elif actual == "negative" and predicted == "positive":
            fp += 1
        elif actual == "negative" and predicted == "negative":
            tn += 1
        else:
            fn += 1

    precision = tp / (tp + fp) if tp + fp else None
    recall = tp / (tp + fn) if tp + fn else None

    if precision is not None and recall is not None:
        f1 = (
            2 * precision * recall / (precision + recall)
            if precision + recall
            else 0.0
        )
    else:
        f1 = None

    return {
        "TP": tp,
        "FP": fp,
        "TN": tn,
        "FN": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python evaluate_results.py reviewed_results.csv")
        raise SystemExit(2)

    path = Path(sys.argv[1])

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required = {"ground_truth", "prediction"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain ground_truth and prediction columns."
            )

        rows = list(reader)

    if not rows:
        raise ValueError("No data rows found; no metrics calculated.")

    if any(not row["ground_truth"].strip()
           or not row["prediction"].strip() for row in rows):
        raise ValueError(
            "Some rows are incomplete. Review them before evaluation."
        )

    metrics = calculate_metrics(rows)

    print("Metrics from supplied reviewed rows:")
    for name, value in metrics.items():
        if isinstance(value, float):
            display = "undefined" if value is None else f"{value:.4f}"
        else:
            display = value
        print(f"{name}: {display}")


if __name__ == "__main__":
    main()
