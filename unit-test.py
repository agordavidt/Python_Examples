import unittest

class UnitTests02(unittest.TestCase):

def testFoo(self):
	self.failUnless(False)

class UnitTests01(unittest.TestCase):

	def testBar01(self):
		self.failUnless(False)

	def testBar02(self):
		self.failUnless(False)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
