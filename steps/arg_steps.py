



###############
# STEPS #
###############
from pytest_bdd import parsers, given


@given(parsers.re(r"There are {start:Number} cucumbers",extra_types =dict(Number=int)))
def start_cucumebrs(start):
    return dict(start=start,eat=0)

