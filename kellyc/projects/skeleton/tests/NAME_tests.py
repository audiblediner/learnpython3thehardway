from nose.tools import *
# import name

def setup():
	print("SETUP!")

def tear_down():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN!") # removed end='' parameter
