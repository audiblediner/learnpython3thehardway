from nose.tools import *

def setup():
	print("SETUP!")

def tear_down():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN!") # removed end='' parameter


class TestUM:

    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")
