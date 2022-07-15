## Python

![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)

===========

This repository includes all my personal notes taken during the different courses and books.

## Python Interview Questions

### Data Type questions

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

#### How would you round a variable that represent the Age of somebody.

    With `floor` , the reason is that someone who have 23 years and 11 months is said to have 23 years, rounding is always downwards.
	
#### What is the result of:

    floor(-10.4) result: -11
    floor(11.4) result: 11
	
#### what is the different of decimal and float in python ?

	One of the differences they have is the way they store the data, float is represented as a fraction while decimal is stored as a string. 
    Because of this some floats do not have exact representation such as 0.1.
	
#### floats vs decimals, what are the advantages of each one ?	

    floats: faster.
	decimals: more precise.
