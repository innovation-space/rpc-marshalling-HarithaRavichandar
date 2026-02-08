from rpc import RPCServer
from marshalling import unmarshal_student


def calculate_grade_average(profile_data: dict) -> float:
    """
    Remote procedure:
    float calculate_grade_average(StudentProfile profile)
    """
    profile = unmarshal_student(profile_data)
    return sum(profile.grades) / len(profile.grades)


# Create RPC server and register method
rpc_server = RPCServer()
rpc_server.register_method("calculate_grade_average", calculate_grade_average)
