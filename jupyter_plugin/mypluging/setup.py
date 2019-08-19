import setuptools

setuptools.setup(
    name="mypluging",
    version='0.0.35',
    url="",
    author="Red",
    author_email="",
    license="BSD 3-Clause",
    description="Jupyter server extension",
    packages=setuptools.find_packages(),
    # package_dir={'mypluging':'mypluging'},
    include_package_data=True,
    package_data={'mypluging': ['static/*.js']},
    install_requires=['tornado', 'notebook'],
    classifiers=[
        'Framework :: Jupyter',
    ]
)
