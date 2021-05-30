from pytest_bdd import scenarios
from .steps import *

# run all tests
scenarios('features')
