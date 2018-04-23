from setuptools import setup, find_packages

RUNTIME_PACKAGES = [
    "numpy==1.14.2",
    "opencv-python==3.4.0.12",
]

setup(
    name="dsample",
    version="1.0.0",
    description="downsample images",
    author="Melanie Berkley",
    license="MIT",
    packages=find_packages(),
    install_requires=RUNTIME_PACKAGES,
)
