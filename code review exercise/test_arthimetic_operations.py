import pytest
from arthimetic_operations import ArthimeticClass

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, "2"
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
    def test_subtract(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.subtract(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.subract("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.subtract(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.subtract("1", "2")
        
        assert expected_output == actual_output
    
    def test_multiply(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.multiply(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("1", "2")
        
        assert expected_output == actual_output
        
    def test_division(self ):
        # arrange
        x, y = 1, "2"
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.divide(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.divide("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.divide(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.divide("1", "2")
        with pytest.raises(ZeroDivisionError):
            ArthimeticClass.divide(1, 0)
        
        
        assert expected_output == actual_output
        