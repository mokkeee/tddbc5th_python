#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grid_point import GridPoint

__author__ = 'mokkeee'


class GridPoints(object):
    def __init__(self, *args):
        if not self._is_valid_grids(args):
            raise ValueError
        self._grids = args

    def __contains__(self, item):
        if not isinstance(item, GridPoint):
            return False
        return item in self._grids

    def __len__(self):
        return len(self._grids)

    def is_connected_grids(self):
        for grid in self._grids:
            if not self._has_neighbor(grid):
                return False
        return True
        # return self._grids[0].is_neighbor(self._grids[1])

    def _has_neighbor(self, grid):
        neighbors = [x for x in self._grids if x.is_neighbor(grid)]
        if len(neighbors) == 0:
            return False
        return True

    @staticmethod
    def _is_valid_grids(args):
        for point in args:
            if not isinstance(point, GridPoint):
                return False
        points_count = len(args)
        if len(set(args)) != points_count:
            return False
        if points_count not in [2, 3]:
            return False
        return True
