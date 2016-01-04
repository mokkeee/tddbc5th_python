#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grid_point import GridPoint

__author__ = 'mokkeee'


class GridPoints(object):
    def __init__(self, *args):
        if not self.__is_valid_grids(args):
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
            if not self.__has_neighbor(grid):
                return False
        else:
            return True

    def is_traversal(self):
        # if not self.is_connected_grids():
        #     return False
        start_grid = self.__traverse_start_grid()
        traversed_grids = [start_grid]
        current_grid = start_grid
        while not self.__is_traverse_complete(traversed_grids):
            next_grid = self.__next_grid(current_grid, traversed_grids)
            if next_grid is None:
                return False
            current_grid = next_grid
            traversed_grids.insert(-1, current_grid)
        else:
            return True

    def neighbors(self, grid):
        return [x for x in self._grids if x.is_neighbor(grid)]

    def __traverse_start_grid(self):
        sorted_grids = sorted(self._grids, key=lambda x: len(self.neighbors(x)))
        return sorted_grids[0]

    def __next_grid(self, current_grid, traversed_grids):
        neighbors = [x for x in self.neighbors(current_grid) if x not in traversed_grids]
        if len(neighbors) == 0:
            return None
        return neighbors[0]

    def __is_traverse_complete(self, traversed_grids):
        return len(traversed_grids) == len(self)

    def __has_neighbor(self, grid):
        neighbors = self.neighbors(grid)
        if len(neighbors) == 0:
            return False
        return True

    @staticmethod
    def __is_valid_grids(args):
        for point in args:
            if not isinstance(point, GridPoint):
                return False
        points_count = len(args)
        if len(set(args)) != points_count:
            return False
        if points_count < 2:
            return False
        return True
