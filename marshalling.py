from models import StudentProfile


def marshal_student(profile: StudentProfile) -> dict:
    """
    Convert StudentProfile object into dictionary (client side).
    """
    return {
        "name": profile.name,
        "id": profile.id,
        "grades": profile.grades
    }


def validate_types(data: dict):
    """
    Server-side type validation.
    Raises TypeError if incorrect types are received.
    """
    if not isinstance(data, dict):
        raise TypeError("Expected data to be a dictionary")

    if "name" not in data or not isinstance(data["name"], str):
        raise TypeError("Expected 'name' to be a string")

    if "id" not in data or not isinstance(data["id"], int):
        raise TypeError("Expected 'id' to be an integer")

    if "grades" not in data or not isinstance(data["grades"], list):
        raise TypeError("Expected 'grades' to be a list")

    for grade in data["grades"]:
        if not isinstance(grade, int):
            raise TypeError("Each grade must be an integer")


def unmarshal_student(data: dict) -> StudentProfile:
    """
    Convert dictionary into StudentProfile object (server side).
    """
    validate_types(data)
    return StudentProfile(
        name=data["name"],
        id=data["id"],
        grades=data["grades"]
    )
