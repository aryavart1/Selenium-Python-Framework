import pytest

class BaseClass:

    @pytest.mark.usefixtures("setup")
    pass