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
        instance = PlayerInOutSchema(**invalid_basemodel_data)
        

@pytest.fixture
def basemodel_data_list(basemodel_data) -> list[PlayerInOutSchema]:
    instance = PlayerInOutSchema(**basemodel_data)
    lista = [instance]
    return lista

def test_convert_data_into_basemodel_data_list(basemodel_data_list):
    instance = PlayersOutSchema(**{'players': basemodel_data_list})
    assert isinstance(instance, PlayersOutSchema)


def test_invalid_list_players():
    with pytest.raises(pydantic.ValidationError):
       instance = PlayersOutSchema(**{'pĺayers_com_acento': list()}) 


@pytest.fixture
def basemodel_data_modify():
    return {'nickname': 'JubileuJoestar'}

def test_convert_data_into_basemodel_modify(basemodel_data_modify):
    instance = PlayerModifySchema(**basemodel_data_modify)

    assert isinstance(instance, PlayerModifySchema) 

@pytest.fixture
def invalid_basemodel_data_modify() -> dict:
    return {'abluble': 'VASH O ESTOURO DA BOIADA'}

def test_convert_invalid_data_into_basemodel_modify(invalid_basemodel_data_modify):
    instance = PlayerModifySchema(**invalid_basemodel_data_modify)
    playermodify_dict = instance.dict()
    assert 'abluble' not in playermodify_dict