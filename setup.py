import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pfs2yaml",
    version="0.0.1",
    install_requires=['pyyaml'],
    author="Henrik Andersson",
    author_email="jan@dhigroup.com",
    description="A package that can convert DHI pfs files to yaml",
    platform="windows_x64",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/DHI/py-dhi-dfs.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows 10",
    ],
)
