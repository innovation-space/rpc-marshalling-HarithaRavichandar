# Lab DA-1: RPC Marshalling with Objects

## Objective
To implement a Python-based RPC framework that supports remote invocation
of a method using a custom object (StudentProfile) with server-side type validation.

## Implemented Features
- StudentProfile object with name, id, and grades
- RPC framework with client-server interaction
- Marshalling and unmarshalling of objects
- Server-side validate_types() function
- Type safety enforcement using TypeError

## Validation Testing
- Correct input successfully returns grade average
- Sending a string instead of an integer for student ID raises TypeError
- Sending non-integer grades raises TypeError

## Result
The RPC framework correctly validates incoming data and prevents invalid
client requests from being processed on the server side.
