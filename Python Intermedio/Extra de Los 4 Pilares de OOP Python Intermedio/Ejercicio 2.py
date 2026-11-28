from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True

class RegularUser(User):
    allowed_permissions = {"read"}

    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        return permission in self.allowed_permissions

def main():
    user1 = AdminUser("Diana")
    user2 = RegularUser("Paúl")

    print(f"User 1 role: {user1.get_role()}")
    print(f"User 2 role: {user2.get_role()}")
    print(f"User 1 has permission to delete: {user1.has_permission('delete')}")
    print(f"User 2 has permission to delete: {user2.has_permission('delete')}")
    print(f"User 2 has permission to read: {user2.has_permission('read')}")

if __name__ == "__main__":
    main()
