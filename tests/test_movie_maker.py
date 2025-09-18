import os

from mock import MagicMock, patch

import nglview
from nglview.utils.test_utils import get_mocked_traj
from make_dummy_comm import *
import PIL.Image


def test_movie_maker():
    from nglview.contrib.movie import MovieMaker
    traj = get_mocked_traj()
    view = nglview.show_simpletraj(traj)

    movie = MovieMaker(view,
                       in_memory=True,
                       download_folder='here',
                       render_params={'factor': 4},
                       moviepy_params={},
                       stop=2)
    movie.make()
