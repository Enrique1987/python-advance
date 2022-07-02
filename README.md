## Python

![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)

===========

This repository includes all my personal notes taken during the different courses and books.

## Python Interview Questions

#### 1 Wha is the result of this ?
          x = 0.1 + 0.1 + 0.1
          y = 0.3
          x == y
		  
The result is `False` as the float numbers does not have exactly representation.

    0.1 --> 0.1000000000000000055511151
    x --> 0.3000000000000000444089210
    y --> 0.2999999999999999888977698

One simple way to compare floats could be :
    x = 0.1 + 0.1 + 0.1
    y = 0.3
    round(x, 5) == round(y, 5)

   True.
