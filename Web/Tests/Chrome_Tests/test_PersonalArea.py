import pytest
from Web.Utils.PreConditions.pre_condition import Precondition_Chrome


@pytest.mark.usefixtures('login_correctly')
class Test1(Precondition_Chrome):
    def test_1(self, login_correctly):
        pass

    def test2(self, login_correctly):
        pass