# PasswordStrengthChecker-1-OmarBaydoun

A Python command-line tool that evaluates password strength by checking length and character variety, classifying passwords as **Weak**, **Medium**, or **Strong**.

Built as **Project 1** of the [DecodeLabs](https://www.decodelabs.tech) Cybersecurity Internship — Industrial Training Kit. This project focuses on the fundamentals of input validation and security logic that underpin more advanced authentication systems: string handling, conditional checks, and basic entropy reasoning.

## Overview

Weak or reused passwords remain one of the leading causes of account compromise. This tool implements a simple, transparent policy check that can be used as a building block in signup flows, internal tooling, or as a learning reference for password validation logic.

## How It Works

The script evaluates a password against two criteria:

1. **Length** — must be at least 8 characters. Passwords shorter than this are rejected and the user is re-prompted.
2. **Character variety** — the password is scored on whether it contains:
   - a digit (`0-9`)
   - an uppercase letter (`A-Z`)
   - a symbol (any non-alphanumeric character)

The number of variety criteria met determines the final classification:

| Variety criteria met | Strength |
|---|---|
| 0–1 | Weak |
| 2 | Medium |
| 3 | Strong |

## Requirements

- Python 3.x
- No external dependencies — uses only the Python standard library.

## Usage

```bash
python3 Password_Checker.py
```

You'll be prompted to enter a password, and the script will print its strength classification.

### Example Runs

```
Enter a password to check: abcdefgh
Password strength: Weak
```

```
Enter a password to check: Abcdefg1
Password strength: Medium
```

```
Enter a password to check: Abcdefg1!
Password strength: Strong
```

```
Enter a password to check: abc
Password too short! Must be at least 8 characters.
Enter a password to check: Abcdefg1!
Password strength: Strong
```

## Future Improvements

This project intentionally scopes to validation logic only. Natural next steps, in line with the broader Industrial Training Kit track, include:

- **Common/leaked password check** — reject passwords found in known breach datasets (e.g., `Have I Been Pwned` corpus).
- **Secure hashing** — once a password passes validation, hash it with a memory-hard algorithm such as **Argon2id** before storage (covered in Project 2: Hashing & Encryption).
- **Constant-time comparison** — use `hmac.compare_digest()` for any secret comparisons to mitigate timing attacks.
- **Expanded entropy scoring** — move beyond a simple variety count toward a proper entropy calculation (e.g., based on character set size and length).
- **In-memory hygiene** — for production use, consider how sensitive password data is handled and cleared in memory, since Python strings are immutable and persist until garbage collected.

## Author

Omar Baydoun
DecodeLabs Cybersecurity Internship — Batch 2026
LinkedIn: [linkedin.com/in/omar-baydoun-750738356](https://www.linkedin.com/in/omar-baydoun-750738356)
