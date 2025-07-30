# 🔐 MPIN Strength Validator

This project implements a secure MPIN (Mobile Personal Identification Number) strength validator in Python. It evaluates MPINs based on common security weaknesses like repetitive patterns and demographic data (e.g., birthdates, anniversaries).

---

## 📌 Features

- ✅ **Strength Classification** — Categorizes MPINs as `STRONG`, `WEAK`, or `INVALID`
- ✅ **Common Patterns Detection** — Detects easily guessable MPINs like `1234`, `0000`, `1111`, etc.
- ✅ **Demographic Relevance Checks** — Flags MPINs resembling:
  - User's Date of Birth
  - Spouse's Date of Birth
  - Wedding Anniversary
- ✅ **Invalid Format Handling** — Flags MPINs that are:
  - Too short or too long
  - Contain non-numeric characters
- ✅ **Clear Reasoning** — Returns structured feedback explaining why an MPIN is weak or invalid

---

## ⚙️ Requirements

- Python 3.7 or higher
- `pytest` for running test cases

Install `pytest`:

```bash
pip install pytest
