from setuptools import setup

setup(
    name='lanchonetedarua',
    version='0.0.0',
    packages=['lanchonetedarua'],
    url='https://github.com/tbrito/lanchonete-da-rua',
    license='gpl-3.0',
    author='Alex Grover',
    author_email='graduacao-fiapi-grupo-23@gmail.com',
    description='Lanchonete da rua',
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        lanchonetedarua=lanchonetedarua.cli:cli
    ''',
)