import csv
import os
import sys

import anthropic

MODEL = "claude-sonnet-5-5"
CATEGORIES = {
    "Delivery", "Shipping", "Refund", "Payment", "Cancellation",
    "Defect", "Return", "Account", "Unknown",
}

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

with open("prompt.txt", encoding="utf-8") as f:
    PROMPT_TEMPLATE = f.read()


def classify(query: str) -> str:
    prompt = PROMPT_TEMPLATE.replace("{{customer_query}}", query)
    response = client.messages.create(
        model=MODEL,
        max_tokens=10,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def run_tests(path: str = "test_cases.csv") -> None:
    correct = 0
    format_ok = 0
    total = 0
    failures = []

    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total += 1
            raw = classify(row["query"])
            # Strict format check: output must be exactly one category word
            if raw in CATEGORIES:
                format_ok += 1
            prediction = raw.strip()
            if prediction == row["expected"]:
                correct += 1
            else:
                failures.append((row["query"], row["expected"], raw))

    print(f"Accuracy:      {correct}/{total} = {correct / total:.1%}")
    print(f"Format-strict: {format_ok}/{total} = {format_ok / total:.1%}")
    if failures:
        print("\nFailures:")
        for query, expected, got in failures:
            print(f"- {query!r}: expected {expected}, got {got!r}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(classify(" ".join(sys.argv[1:])))
    else:
        run_tests()
