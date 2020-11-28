class Customer:
    autoincremented_id = 1
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.autoincremented_id
        Customer.autoincremented_id += 1

    @staticmethod
    def get_next_id():
        return Customer.autoincremented_id

    # def autoincrement(self):
    #     if hasattr(self, "num"):
    #         self.num += 1  # increment if not first call
    #     else:
    #         self.num = 1  # initialize on first call
    #     return self.num

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# c = Customer("Pesho", "Sofia","pp@abv.bg")
# print(c.get_next_id())
#
# c1 = Customer("Ivan", "Plovdiv","ii@abv.bg")
# print(c1.get_next_id())

