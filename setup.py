import setuptools

setuptools.setup(
    include_package_data=True,
    name="flore1",
    version="1.5.3",
    author="Anicet Nougaret",
    author_email="anicet.nougaret@zohomail.eu",
    description="The first 2D python game engine rendering in the terminal.",
    url="https://github.com/AnicetNgrt/flore1",
    packages=setuptools.find_packages(),
    install_requires=[
        'pillow',
        'keyboard',
        'clipboard'
      ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers"
    ],
    python_requires=' >= 3.7',
)
