import pydantic
import pytest
from tibiacrud.models.models import *

@pytest.fixture
def basemodel_data() -> dict:
    return {'nickname': 'LordPaulistinha',
            'vocation': 'Royal Paladin',
            'level': 500}

def test_convert_data_into_basemodel(basemodel_data):
    instance = PlayerInOutSchema(**basemodel_data)

    assert isinstance(instance, PlayerInOutSchema)

@pytest.fixture
def invalid_basemodel_data() -> dict:
    return {'minhabolaesquerda': 'é azul'}

def test_convert_invalid_data_into_basemodel(invalid_basemodel_data):
    with pytest.raises(pydantic.ValidationError):
        isinstance = PlayerInOutSchema(**invalid_basemodel_data)