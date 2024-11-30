from setuptools import setup, find_packages

setup(
    name='ecommerce-etl',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'pandas',
        'sqlalchemy',
        'psycopg2-binary',
        'python-dotenv',
    ],
    author='Seu Nome',
    author_email='seu.email@exemplo.com',
    description='Pipeline ETL para dados de E-commerce',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)