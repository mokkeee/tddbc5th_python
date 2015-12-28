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

    def is_traversal(self):
        # if not self.is_connected_grids():
        #     return False
        start_grid = self._traverse_start_grid()
        traversed_grids = [start_grid]
        current_grid = start_grid
        while len(traversed_grids) < len(self):
            next_grid = self._next_grid(current_grid, traversed_grids)
            if next_grid is None:
                return False
            current_grid = next_grid
            traversed_grids.insert(-1, current_grid)
        else:
            return True

    def neighbors(self, grid):
        return [x for x in self._grids if x.is_neighbor(grid)]

    def _traverse_start_grid(self):
        sorted_grids = sorted(self._grids, key=lambda x: len(self.neighbors(x)))
        return sorted_grids[0]

    def _next_grid(self, current_grid, traversed_grids):
        neighbors = [x for x in self.neighbors(current_grid) if x not in traversed_grids]
        if len(neighbors) == 0:
            return None
        return neighbors[0]

    def _has_neighbor(self, grid):
        neighbors = self.neighbors(grid)
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
        if points_count not in [2, 3, 4]:
            return False
        return True
