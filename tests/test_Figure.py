import math

import pytest

from src.Figure import Figure
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize('test_figure', [Circle, Square, Rectangle, Triangle])
def test_figure_1(figure_rnd, test_figure):
    assert isinstance(figure_rnd, Figure)


@pytest.mark.parametrize('test_figure', [Circle, Square, Rectangle, Triangle])
def test_figure_2(figure_rnd, test_figure):
    assert hasattr(figure_rnd, 'name')
    assert hasattr(figure_rnd, 'area')
    assert hasattr(figure_rnd, 'perimeter')
    assert hasattr(figure_rnd, 'add_area')


@pytest.mark.parametrize('test_figure', [Circle, Square, Rectangle])
@pytest.mark.parametrize('test_param1', [0.1, 1.111, 10])
@pytest.mark.parametrize('test_param2', [0.1, 1.111, 10])
@pytest.mark.parametrize('test_param3', [0.1, 1.111, 10])
def test_figure_3(figure_reg, test_figure, test_param1, test_param2, test_param3):
    if isinstance(figure_reg, Circle):
        assert 2 * math.pi * test_param1 == figure_reg.perimeter
        assert math.pi * (test_param1 ** 2) == figure_reg.area
    elif isinstance(figure_reg, Square):
        assert test_param1 * 4 == figure_reg.perimeter
        assert test_param1 ** 2 == figure_reg.area
    elif isinstance(figure_reg, Rectangle):
        assert (test_param1 + test_param2) * 2 == figure_reg.perimeter
        assert test_param1 * test_param2 == figure_reg.area


@pytest.mark.parametrize('test_figure', [Triangle])
@pytest.mark.parametrize('test_param1', [0.3, 3.3, 33.3])
@pytest.mark.parametrize('test_param2', [0.4, 4.4, 44.4])
@pytest.mark.parametrize('test_param3', [0.5, 5.5, 55.5])
def test_figure_4(figure_reg, test_figure, test_param1, test_param2, test_param3):
    if isinstance(figure_reg, Triangle):
        assert test_param1 + test_param2 + test_param3 == figure_reg.perimeter
        half_perimeter = (test_param1 + test_param2 + test_param3) / 2
        assert math.sqrt(
            half_perimeter * (half_perimeter - test_param1) * (half_perimeter - test_param2) * (
                    half_perimeter - test_param3)) == figure_reg.area


@pytest.mark.parametrize('test_figure, test_param1, test_param2, test_param3',
                         [[Circle, 0, None, None],
                          [Circle, -1, None, None],
                          [Square, 0, None, None],
                          [Square, -1, None, None],
                          [Rectangle, -1, 1, None],
                          [Rectangle, 1, -1, None],
                          [Rectangle, 0, 1, None],
                          [Rectangle, 1, 0, None],
                          [Rectangle, -1, 1, None],
                          [Triangle, 0, 4, 5],
                          [Triangle, 3, 0, 5],
                          [Triangle, 3, 4, 0],
                          [Triangle, -1, 4, 5],
                          [Triangle, 3, -1, 5],
                          [Triangle, 3, 4, -1],
                          [Triangle, 3, 4, 8]])
def test_figure_5(figure_reg, test_figure, test_param1, test_param2, test_param3):
    assert figure_reg is None


@pytest.mark.parametrize('test_figure', [Circle, Square, Rectangle, Triangle])
def test_figure_6(figure_rnd, test_figure):
    with pytest.raises(ValueError):
        figure_rnd.add_area('test_object')


@pytest.mark.parametrize('test_figure', [Circle, Square, Rectangle, Triangle])
def test_figure_7(figure_rnd, test_figure, circle_rnd, square_rnd, rectangle_rnd, triangle_rnd):
    assert figure_rnd.add_area(circle_rnd) == circle_rnd.add_area(figure_rnd)
    assert figure_rnd.add_area(circle_rnd) == figure_rnd.area + circle_rnd.area
    assert figure_rnd.add_area(square_rnd) == square_rnd.add_area(figure_rnd)
    assert figure_rnd.add_area(square_rnd) == figure_rnd.area + square_rnd.area
    assert figure_rnd.add_area(rectangle_rnd) == rectangle_rnd.add_area(figure_rnd)
    assert figure_rnd.add_area(rectangle_rnd) == figure_rnd.area + rectangle_rnd.area
    assert figure_rnd.add_area(triangle_rnd) == triangle_rnd.add_area(figure_rnd)
    assert figure_rnd.add_area(triangle_rnd) == figure_rnd.area + triangle_rnd.area
