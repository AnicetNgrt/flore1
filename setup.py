from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flore1",
    version="1.0.0",
    author="Anicet Nougaret",
    author_email="anicet.nougaret@zohomail.eu",
    description="The first 2D python game engine rendering in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnicetNgrt/flore1",
    packages=setuptools.find_packages(),
    install_requires=[            
          'pillow'
      ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers"
    ],
    python_requires=' >= 3.6',
)
