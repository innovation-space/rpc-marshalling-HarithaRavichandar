# Lab DA-1: RPC Framework with Object Marshalling

## Overview
This project implements a Python-based Remote Procedure Call (RPC) framework that supports object marshalling and server-side type validation. It demonstrates safe and reliable client–server communication in a distributed systems environment.

---

## Implemented Remote Procedure

The `StudentProfile` object contains:
- name (string)
- id (integer)
- grades (list of integers)

---

## Key Concepts Demonstrated
- Remote Procedure Call (RPC)
- Client–Server Architecture
- Object Marshalling and Unmarshalling
- Server-Side Type Validation
- Error Handling

---

## Folder Structure

```text
rpc-marshalling-HarithaRavichandar/
├── client.py        # RPC client
├── server.py        # Remote procedure implementation
├── rpc.py           # Core RPC framework
├── marshalling.py   # Object marshalling and validation
├── models.py        # StudentProfile definition
├── results.md       # Experiment results
├── Video.md         # Screen-recorded walkthrough link
├── README.md        # Project documentation
└── .gitignore       # Ignored files configuration

'''
How to Run

Ensure Python 3 is installed.

Navigate to the project directory.

Run the following command:
python client.py
Output Behavior

Valid input returns the calculated grade average.

Invalid input is rejected by the server with an appropriate error message.

Conclusion

The project successfully demonstrates an RPC-based client–server model with object marshalling and server-side validation, ensuring type safety and reliable communication.

---

### ✅ After Pasting (Final Step)
```bash
git add README.md
git commit -m "Add README with folder structure and usage instructions"
git push origin rpc-marshalling-objects
