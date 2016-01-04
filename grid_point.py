#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'


class GridPoint(object):
    def __init__(self, x, y):
        """ ｘ座標、ｙ座標は共に整数を指定する """
        if not isinstance(x, int):
            raise TypeError("x is not int value.")
        if not isinstance(y, int):
            raise TypeError("y is not int value.")
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return '(%d, %d)' % (self.__x, self.__y)

    def __eq__(self, other):
        if not isinstance(other, GridPoint):
            return False
        return self.__x == other.__x and self.__y == other.__y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.__x << 11 + self.__y

    def is_neighbor(self, other):
        if self.x == other.x:
            if self.__is_neighbor_value(self.y, other.y):
                return True
        if self.y == other.y:
            if self.__is_neighbor_value(self.x, other.x):
                return True
        return False

    @staticmethod
    def __is_neighbor_value(self_value, other_value):
        if self_value == other_value - 1:
            return True
        if self_value == other_value + 1:
            return True
        return False

