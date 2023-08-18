"""Setup file."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()

setuptools.setup(
    name="quantum_glasses",
    description="Quantum Glasses",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires='>=3.9'
)
