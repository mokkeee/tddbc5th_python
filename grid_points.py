#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'


class GridPoints(object):
    def __init__(self, *args):
        if self._contains_same_grid(args):
            raise ValueError
        self._grids = args

    def __contains__(self, item):
        return item in self._grids

    def is_connected_points(self):
        return self._grids[0].is_neighbor(self._grids[1])

    @staticmethod
    def _contains_same_grid(args):
        if len(set(args)) != len(args):
            return True
        return False
