from pytest_bdd import scenario, given, when, then


@scenario("../features/Tree.feature", "Add properties to tree")
def test_tree():
    pass


class Tree:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("my kdhjhs")
        return self.name
        print(Tree)


@given("a new tree is created with name default", target_fixture="tree")
def tree():
    print("a new tree is created with name default")
    return Tree(name="default")


@when("the name of the tree is asked for")
def get_name(tree):
    return tree.get_name()
    print("the name of the tree is asked for")


@then("default is returned")
def is_default(get_name):
    assert get_name == 'default'
