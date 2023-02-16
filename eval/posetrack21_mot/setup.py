from setuptools import setup,  find_packages 

setup(
    name='posetrack21_mot',
    version='0.1',
    packages=find_packages(include=['evaluation_kit',  'evaluation_kit.*']),
    install_requires=[
            'shapely',
            'numpy',
            'pandas',
            'scipy',
            'xmltodict',
            'tqdm',
            'lap',
    ],
)
