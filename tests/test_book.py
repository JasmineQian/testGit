from pytest_bdd import scenarios
from steps.book_steps import *
# from testGit.tests.book_steps import *

# scenarios("test_book.feature")

scenarios("test_seq.feature", "test_seq02.feature")
