#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grid_point import GridPoint
from grid_points import GridPoints

__author__ = 'mokkeee'

import pytest


class Test_GridPoints1:
    grid_points = GridPoints(GridPoint(0, 1), GridPoint(2, 3))

    def test_格子点集合ー0_1ー2_3は格子点0_1を含むこと(self):
        assert GridPoint(0, 1) in self.grid_points

    def test_格子点集合ー0_1ー2_3は格子点2_3を含むこと(self):
        assert GridPoint(2, 3) in self.grid_points

    def test_格子点集合ー0_1ー2_3は格子点1_3を含まないこと(self):
        assert not GridPoint(1, 3) in self.grid_points


class Test_GridPoints_Error:
    def test_同一格子点を持つ格子点集合は生成できないこと(self):
        with pytest.raises(ValueError):
            GridPoints(GridPoint(0, 1), GridPoint(0, 1))

@pytest.mark.parametrize(('grid1', 'grid2', 'result'), [
    ([1, 2], [1, 1], True),
    ([1, 2], [1, 3], True),
    ([1, 2], [2, 3], False),
    ([1, 2], [1, 4], False),
    ([0, 3], [2, 3], False),
    ([0, 2], [1, 2], True),
    ([0, 2], [-1, 2], True),
])
def test_格子点集合の判定ができること(grid1, grid2, result):
    grid_points = GridPoints(GridPoint(grid1[0], grid1[1]), GridPoint(grid2[0], grid2[1]))
    assert grid_points.is_connected_points() == result