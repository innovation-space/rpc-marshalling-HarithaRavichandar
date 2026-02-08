# Lab DA-1: RPC Framework with Object Marshalling

## Overview
This project implements a Python-based Remote Procedure Call (RPC) framework that supports object marshalling and server-side type validation. It demonstrates safe client–server communication in a distributed systems context.

---

## Implemented Remote Procedure

The `StudentProfile` object contains:
- `name` – string
- `id` – integer
- `grades` – list of integers

---

## Key Concepts Demonstrated
- Remote Procedure Call (RPC)
- Client–Server Architecture
- Object Marshalling and Unmarshalling
- Server-Side Type Validation
- Error Handling

---

## Folder Structure
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

---

## How to Run
1. Ensure Python 3 is installed.
2. Navigate to the project directory.
3. Execute:
   ```bash
   python client.py

---

## Next Step 

After adding or updating `README.md`:

```bash
git add README.md
git commit -m "Add README with folder structure and project overview."
git push origin rpc-marshalling-objects
