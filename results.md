# RPC Marshalling with Objects – Results

## Objective
To implement a Python-based Remote Procedure Call (RPC) framework that supports object marshalling and server-side type validation for safe client–server communication.

---

## Function Implemented

The `StudentProfile` object includes:
- name (string)
- id (integer)
- grades (list of integers)

---

## Key Features
- Object marshalling and unmarshalling of `StudentProfile`
- Server-side type validation using `validate_types()`
- TypeError raised for invalid client input
- RPC-based client–server interaction

---

## Validation Testing
1. Valid student data returns the correct grade average.
2. Sending a string instead of an integer for student ID raises `TypeError`.
3. Sending non-integer values in grades list raises `TypeError`.

---

## Sample Output

---

## Conclusion
The RPC framework correctly handles object marshalling, enforces server-side validation, and ensures reliable remote procedure execution in a distributed environment.
