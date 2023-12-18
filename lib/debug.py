#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    Song.create_table()
    import ipdb; ipdb.set_trace()
