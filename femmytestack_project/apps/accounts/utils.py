from uuid import uuid4


def generate_random_id(length=5):
    random_id = str(uuid4())
    # this will return a unique identifier
    return random_id[:length]
