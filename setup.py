from setuptools import setup, find_packages

setup(
    name="srvtest_udp",
    version="0.1.0",
    packages=find_packages(),
    description="Servidor UDP assincrono simples usando asyncio",
    author="Thiago Faioli",
    author_email="thiago.faioli@gmail.com",
    url="https://github.com/0xttfx/srvtest-udp-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
