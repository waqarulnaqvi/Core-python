class Parent_class:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def parent_method(self):
        print("This is the parent method")

    def dispaly(self):
        print(self.name)
        print(self.id)


class Child_class(Parent_class):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def parent_method(self):
        print("Harry")
        super().parent_method()
        print()

    def dispaly(self):
        print(self.name)
        print(self.id)
        print(self.lang)
        super().dispaly()

    def child_method(self):
        print("This is the child method")
        super().parent_method()
        print()


child_object = Child_class("ali", 12, "eng")
child_object.child_method()
child_object.parent_method()
child_object.dispaly()
