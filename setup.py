import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="transformation_fn_template",
    version="0.1.0",
    description='Template for hsfs online transformation function(s) development',
    author="Hopsworks AB",
    author_email="davit@logicalclocks.com",
    license="Apache License 2.0",
    keywords="Hopsworks, Feature Store, Spark, Machine Learning, MLOps, DataOps",
    url="https://github.com/logicalclocks/custom_transformation_fn_template.git",
    download_url="https://github.com/logicalclocks/custom_transformation_fn_template/releases/tag/"
                 + "0.1.0",
    packages=find_packages(),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)