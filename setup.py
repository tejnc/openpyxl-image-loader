import pathlib
from setuptools import setup

BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / 'README.md').read_text()

setup(
    name='openpyxl-image-loader',
    version='0.1.0',
    description='Openpyxl wrapper that gets images from cells',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/mauricio-chavez/openpyxl-image-loader',
    author='Tej Narayan Chaudhary',
    author_email='tejnarayan15.tnc@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['openpyxl_image_loader'],
    include_package_data=True,
    install_requires=['Pillow','openpyxl',],
)
