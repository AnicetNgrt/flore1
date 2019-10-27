import setuptools

setuptools.setup(
    name="flore1",
    version="1.0.4",
    author="Anicet Nougaret",
    author_email="anicet.nougaret@zohomail.eu",
    description="The first 2D python game engine rendering in the terminal.",
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
