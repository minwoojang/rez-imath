# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "imath"

version = "3.0.1"

description = \
    """
    Imath
    """

build_requires = [
    # 'cmake-3',
#    "ilmbase"
]

requires = [
    # 'boost-1.61',
    #'numpy'
]

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.openexr"


def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PKG_CONFIG_PATH.prepend("{root}/lib64/pkgconfig")
    env.INCLUDE_PATH.prepend("{root}/include")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.openexr"
