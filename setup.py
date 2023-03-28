from setuptools import find_packages, setup


def load_requirements(f):
    retval = [str(k.strip()) for k in open(f, "rt")]
    return [k for k in retval if k and k[0] not in ("#", "-")]


setup(
    name="decm05",
    version="0.0.0",  # set version for local deployment
    description="Mini project for M05 module of UniDistance's Master in AI",
    url="https://github.com/master-ai-batch5/M05-mp-decaillet",
    authors="Décaillet Valentin, Décaillet Benjamin",
    author_email="decaillet.valentin@etu.unidistance.ch, decaillet.benjamin@etu.unidistance.ch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=('decm05', 'decm05.*')),
    package_data={"decm05": ["data/*", "../doc/*.md", "../doc/*.rst", "../doc/img/*", "../build-requirements.txt"]},
    include_package_data=True,
    install_requires=load_requirements("build-requirements.txt"),
    entry_points={"console_scripts": ["run_decm05 = decm05.service:run_service"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
