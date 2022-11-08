## Python

![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)

===========

This repository includes all my personal notes taken during the different courses and books.

## Python Interview Questions


### In your experience as a python developer could you tell me about bad practices you have seen written. ?

- The most common is not writing according to pep8, in my company it was corrected by putting an autocheck when you wanted to make a Pull Request.
- Code repeated or no.
- variables and funktions with non-self-clearing names
- Magic numbers
- Death code
- prints as logs (interesting in the dev phase but not in prod if it doesnt bring any extra value)
- poorly organised code, should be: first imports, later funcions that you going to use and later the main.
- O() notation.
- Clases that should be a function.(I see that typical error from people that come from a OOP like Java)
- Empty Except Blocks and Poor Error messages.

### What about Python best practices ?

Well basically all in the Zen of Python.

- Simple is better than complex.
- Flat is better thatn ntested.
- Readability counts.
- If the implementation is hard to expain, its a bad idea.
- If the implementation is easy to explain, it ba be a good idea.

### can you tell me what is the output of that code ? 

```
def analyzeAge( age ):
   if age < 21:
       print "You are a child"
   if age >= 21: 
       print "You are an adult"
   else:   #Handle all cases where 'age' is negative 
       print "The age must be a positive integer!"

analyzeAge( 18 )  #Calling the function
```


**Solution**

>You are a child
>The age must be a positive integer!

### Could you explain why is failing and how would you fix it ? 

its failing caise the second if should be a elif.

### continue vs pass vs break:

```
a = [1, 2, 0, 3]
for element in a:
    if not element:
        pass
    print(element)
```

vs

```
a = [1, 2, 0, 3]
for element in a:
    if not element:
        continue
    print(element)
```
vs

```
a = [1, 2, 0, 3]
for element in a:
    if not element:
        break
    print(element)
```

**solution**
`pass` will do nothing(afther the pass will print) but `continue` will ignore the complete loop(not printing if enter in the continue) mean `break` will break the loop and finish

### without writing the code, how would you compare 2 dataframes to see if they are the same ?

to compare 2 dataframes and see if they are the same I would use pandas. 
If what we want to see is if our dataframe A and dataframe B are equal before we put to compare by means of programming the first thing that would do is some simple verifications to know if realment is worth comparing them (this is as if we are doctors and we want to save the life to a patient, the first thing that interests us is if esata alive, to know the pulse etc..) in our case what interests us first verifications would do it by means of dataframA.info() dataframeB.ingo(), if simply they have different dimension already we know that they cannot be equal.

Let's imagine they have the same dimension, the next thing we need to do is to set all the columns to the same name and the same data type, and then we are ready to write the code to compare them.


### Imagine your dataframe contains nan values, how would you compare the two dataframes ?

Using methods like dataframe1.compare(dataframe2) will not work if the dataframe had null values as the  the comparation nan == nan is false. ( we can not compare two unknow thins
because we dont know them,) so in this case it may be interesting to replace nan by some value you know such as "nan" or 999999 and then proceed to compare them again.

### Data Type questions(are not part of an interview as a python developer as they are very advanced)

#### 1 What is the result of this ?
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
