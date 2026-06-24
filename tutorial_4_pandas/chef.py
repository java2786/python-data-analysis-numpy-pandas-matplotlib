class Chef:
    # properties
    name = None
    age = None

    # cook
    def cook(self, food="Tea"):
        print(f"{self.name} is making {food}")


chef = Chef()

chef.name = "Ranveer Brar"
chef.age = 46

chef.cook("Biryani")