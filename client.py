from rpc import RPCClient
from server import rpc_server
from models import StudentProfile
from marshalling import marshal_student

# Create RPC client
client = RPCClient(rpc_server)

# Valid student profile
student = StudentProfile(
    name="Haritha",
    id=101,
    grades=[85, 90, 88]
)

response = client.call(
    "calculate_grade_average",
    marshal_student(student)
)

print("Response:", response)


# Invalid data test (string instead of int)
invalid_student_data = {
    "name": "Haritha",
    "id": "101",          # WRONG TYPE
    "grades": [90, 80]
}

error_response = client.call(
    "calculate_grade_average",
    invalid_student_data
)

print("Error Response:", error_response)
