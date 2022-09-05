"""
Author: tanishk sachdeva (tanishk.sachdeva@dubizzle.com)
setup.py (c) 2022
Desc: description
Created:  2022-07-22T12:12:44.160Z
Modified: 2022-07-27T12:05:51.803Z
"""
"""
Author: tanishk sachdeva (tanishk.sachdeva@dubizzle.com)
setup.py (c) 2022
Desc: description
Created:  2022-07-22T12:12:44.160Z
Modified: 2022-07-27T12:05:51.803Z
"""

from setuptools import find_packages, setup

setup(
    name="modnet_inference",
    packages=["modnet_inference"],
    version="0.1.0",
    description="Image + Text classifier used for moderation",
    author="fenix-ai",
    license="",
    python_requires="~=3.7",
)