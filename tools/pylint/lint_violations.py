"""pylint fixture with intentional violations."""


CONFIG_A = 'a'
CONFIG_B = "b"


def getUserName(userId):
    temp = "throwaway"
    return "user_" + str(userId)


def get_user_age(user_id):
    return 42
