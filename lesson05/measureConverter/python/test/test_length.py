import pytest
from conversions.length import lengthClass, measureType  # adjust filename if needed

@pytest.mark.parametrize("value, m_type, expected", [
    (1.0, measureType.METRIC, 0.39),     # cm → inch
    (0.0, measureType.METRIC, 0.0),
    (2.54, measureType.METRIC, 1.0),
    (1.0, measureType.IMPERIAL, 2.54),           # inch → cm
    (10.0, measureType.IMPERIAL, 25.4),
])
def test_length_conversion(value, m_type, expected):
    l = lengthClass(value, m_type)
    result = l.convert()
    assert result == expected

@pytest.mark.parametrize("invalid_value", ["abc", None, [], {}, object()])
def test_invalid_value_type(invalid_value):
    with pytest.raises(TypeError):
        lengthClass(invalid_value, measureType.METRIC)

@pytest.mark.parametrize("bad_type", ["Metric", None, 123, True, object()])
def test_invalid_measure_type_enum(bad_type):
    with pytest.raises(ValueError):
        lengthClass(100.0, bad_type)
