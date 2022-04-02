# simplebch

A python wrapper around Robert Morelos-Zaragoza's BCH implementation in C.

## Installation instructions

```shell
$ gcc -fPIC -shared -o simplebch.so -I/usr/include/python3 simplebch.c
$ python setup.py build_ext --inplace
$ pip install dist/simplebch-0.1.0-cp*
```
