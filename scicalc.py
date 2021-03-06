#!/usr/bin/env python
#
# A simple command-line scientific calculator.
#

import sys, math
import numpy as np

def die_with_usage(message):
	print("\n****\n**** error: {}\n****\n".format(message), file=sys.stderr)
	print("usage:\n\n    {} <operator> [arg1 [arg2 [...]]]\n".format(sys.argv[0]), file=sys.stderr)
	print(", where <operator> can be one of:\n", file=sys.stderr)
	for (op, func) in operators.items():
		print("    {}: {}".format(op, func.__doc__), file=sys.stderr)
	print("", file=sys.stderr)
	print("note: you can also use 'pi' and 'e' as arguments, for example:\n")
	print("    {} sin pi".format(sys.argv[0]))
	print("", file=sys.stderr)
	exit(-1)

#
# The operators.
#
# These functions must take the necessary number of arguments, and return
# the result of the operation. They must have a short docstring explaining
# what they do (it will be printed by the die_with_usage() function).
#
# Exceptions:
#   - If an incorrect number of arguments is passed, the function must raise a TypeError.
#   - If there's a problem with argument values (e.g., a negative number passed to log),
#     the function must raise a ValueError.
#

def add(*args):
	"""Add a list of numbers"""

	sum = 0.0
	for arg in args:
		sum += arg
	return sum

def multiply(*args):
	"""Multiplies list of inputed sys arguments"""

	mul = 1.0
	for arg in args:
		mul *= arg
	return mul

def log10(x):
	"""Return a base-10 logarithm of x"""

	return math.log10(x)

def abs(x):
	"""Return absolute value of the input."""
	return np.abs(x)

def divide(x, y):
	"""Divides argument x by argument y"""
	return x/y

def factorial(x):
	"""Returns the factorial of x"""

	return math.factorial(x)

def exp(x):
	"""Return the constant "e" raised to the input value"""
	return math.e**x

def sub(x, y):
	"""subtracts y from x"""
	return x - y

def sin(x):
	"""Return sin of x (x is in radians)"""
	return math.sin(x)

def cos(x):
	"""Return cos of x (x is in radians)"""
	return math.cos(x)

def tan(x):
	"""Return tan of x (x is in radians)"""
	return math.tan(x)

def natural_log(x):
    """Finds the natural log of some number"""
    return math.log(x)

def inverse(x):
	"""Returns whatever input as one over the input"""
	return 1/x

def niner(x):
	"Adds 9 to an argument"
	return x + 9

def sciNot(x):
	"""Returns scientific notation of x value"""

	return '%.2E' % x

def sqrt(x):
	"""Returns square root of x value"""
	return math.sqrt(x)




#
# The dictionary that maps the command-line name of the operation,
# to the function that performs it. There can be multiple names
# for the same operator (e.g., 'add' and 'sum').
#
operators = {
	'add': add,
	'sum': add,
	'log10': log10,
	'divide': divide,
	'factorial': factorial,
	'exp': exp,
	'mul': multiply,
	'sub': sub,
	'subtract': sub,
	'sin': sin,
	'cos': cos,
	'tan': tan,
        'naturallog': natural_log,
	'absolute_value': abs,
	'inverse': inverse,
	'niner': niner,
	'sciNot': sciNot,
	'sqrt': sqrt
}

if __name__ == "__main__":
	#
	# Collect and parse arguments
	#
	try:
		op = sys.argv[1]
		my_args = []
		#allowing for e an pi as inputs
		for arg in sys.argv[2:]:
			if arg == 'e':
				my_args.append(2.718281828459)
			elif arg == 'pi':
				my_args.append(3.14159265)
			else:
				my_args.append(arg)

		args = [ float(arg) for arg in my_args ]
	except IndexError:
		die_with_usage("Insufficient number of arguments.")
	except ValueError as e:
		die_with_usage(e)

	#
	# Run the requested operation, and print the result
	#
	try:
		print(operators[op](*args))
	except KeyError:
		die_with_usage("Unknown operator '{}'.".format(op))
	except TypeError as e:
		die_with_usage(e)
	except ValueError as e:
		die_with_usage(e)
