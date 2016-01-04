#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from grid_point import GridPoint

__author__ = 'mokkeee'


class Test1_1:
    grid_point_4_7 = GridPoint(4, 7)

    def test_4_7のｘ座標は４である(self):
        assert self.grid_point_4_7.x == 4

    def test_4_7のy座標は7である(self):
        assert self.grid_point_4_7.y == 7

    def test_4_7の文字列表現が合っている(self):
        assert str(self.grid_point_4_7) == '(4, 7)'


@pytest.mark.parametrize(('x', 'y', 'str_value'), [
    (1, 0, '(1, 0)'),
    (0, 1, '(0, 1)'),
    (1, -1, '(1, -1)'),
    (-1, 1, '(-1, 1)'),
    (-10000, 100000, '(-10000, 100000)'),
])
def test_指定値に応じた格子点が作成できること(x, y, str_value):
    grid_point = GridPoint(x, y)
    assert str(grid_point) == str_value


@pytest.mark.parametrize('value', [
    "1",
    0.1,
    (1, 2),
])
def test_格子点ｘ_yに整数以外を指定するとエラーになる(value):
    with pytest.raises(TypeError):
        GridPoint(value, 1)
    with pytest.raises(TypeError):
        GridPoint(1, value)


class Test_Error:
    def test_格子点x_yの値は更新不可である(self):
        grid_point = GridPoint(0, 0)
        with pytest.raises(AttributeError):
            grid_point.x = 1
        with pytest.raises(AttributeError):
            grid_point.y = 1


class Test1_2:
    def test_格子点4_7と格子点4_7は等しい(self):
        assert GridPoint(4, 7) == GridPoint(4, 7)

    def test_格子点4_7と格子点4_8は等しくない(self):
        assert GridPoint(4, 7) != GridPoint(4, 8)

    def test_格子点4_7と格子点3_7は等しくない(self):
        assert GridPoint(4, 7) != GridPoint(3, 7)

    def test_格子点とNoneは等しくない(self):
        assert not GridPoint(4, 7).__eq__(None)
        assert GridPoint(4, 7).__ne__(None)

    def test_格子点と格子点でないクラスは等しくない(self):
        assert GridPoint(4, 7) != int(4)


@pytest.mark.parametrize(('this', 'other', 'result'), [
    ((1, 2), (1, 1), True),
    ((1, 2), (1, 3), True),
    ((1, 2), (1, 2), False),
    ((1, 2), (2, 3), False),
    ((0, 2), (1, 2), True),
    ((0, 2), (-1, 2), True),
])
def test_隣り合っている格子点の判定ができること(this, other, result):
    this_grid = GridPoint(this[0], this[1])
    other_grid = GridPoint(other[0], other[1])
    assert this_grid.is_neighbor(other_grid) == result
