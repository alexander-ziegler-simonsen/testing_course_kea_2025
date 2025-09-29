import pytest
from conversions.weight import Weight, weightType

@pytest.mark.parametrize("value, w_type, expected", [
    (1.0, weightType.METRIC, 2.2046244202),     # kg to lbs
    (0.0, weightType.METRIC, 0.0),
    (2.5, weightType.METRIC, 5.5115610505),
    (1.0, weightType.IMPERIAL, 0.453592),       # lbs to kg
    (5.5, weightType.IMPERIAL, 2.494756),
])
def test_weight_conversion(value, w_type, expected):
    w = Weight(value, w_type)
    result = round(w.convert(), 6)
    assert result == round(expected, 6)

@pytest.mark.parametrize("invalid_value", ["abc", None, [], {}, object()])
def test_invalid_value_type(invalid_value):
    with pytest.raises(TypeError):
        Weight(invalid_value, weightType.METRIC)

@pytest.mark.parametrize("bad_type", ["Metric", None, 123, True, object()])
def test_invalid_weight_type_enum(bad_type):
    with pytest.raises(ValueError):
        Weight(70.0, bad_type)