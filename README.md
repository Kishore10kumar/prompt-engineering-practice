# Customer Query Classification Using Prompt Engineering

## Problem Statement
An e-commerce company receives many customer queries about orders, deliveries,
payments, refunds, cancellations and product defects. This project designs a
prompt that classifies each query into exactly one predefined category.

- **Input:** a customer query in natural language
- **Output:** a single category word, with no explanation or punctuation
- **Categories:** Delivery, Shipping, Refund, Payment, Cancellation, Defect, Return, Account, Unknown

## Repository Structure
| File | Purpose |
|---|---|
| `prompt.txt` | The classification prompt |
| `test_cases.csv` | 40 test queries with expected labels |
| `classify.py` | Script that runs the prompt against the test cases |
| `requirements.txt` | Python dependencies |

## The Prompt
(Paste the full contents of prompt.txt here inside a code block.)

## Design Choices
- **Role and task:** defines the model's job clearly.
- **Category definitions:** removes ambiguity about what each label means.
- **Tie-break rules:** resolve confusing pairs such as Delivery vs Shipping, Refund vs Payment and Return vs Defect.
- **Few-shot examples:** anchor the expected output format.
- **Strict output rules:** force a single word with no extra text.
- **Injection guard:** the query is treated as data, so instructions inside it are ignored.

## How to Run
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
python classify.py
```

## Results
- Model: (fill in)
- Temperature: 0
- Accuracy: (fill in)/40
- Format-strict: (fill in)/40

## Limitations
- No prompt can guarantee 100% accuracy; genuinely ambiguous queries
  (e.g. "I returned it but didn't get my money") may be classified either way.
- Results depend on the model and settings used.
- Queries mixing several issues are classified by their primary intent only.
