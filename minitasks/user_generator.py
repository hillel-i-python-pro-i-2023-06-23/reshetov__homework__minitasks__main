from faker import Faker

fake = Faker()


def generator(number_of_users: int = 100) -> str:
    """
    :param: number of users(100 by default)
    :return: names and emails of random generated users
    """
    list_of_users = []
    for _ in range(number_of_users):
        name = fake.first_name()
        email = fake.ascii_email()
        list_of_users.append(f"{name} {email}")

    users_str = "\n".join(list_of_users)
    print(users_str)
    return users_str
