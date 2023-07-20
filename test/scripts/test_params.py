#! /usr/bin/env python3
import unittest
import rostest
import rospy

class ParamsTestCase(unittest.TestCase):
	def test_param(self):
		self.assertEqual(rospy.get_param('/value'), 10)

		# value = rospy.get_param('/value', None)
		# self.assertIsNotNone(value)


if __name__ == '__main__':
	rostest.rosrun('test_packages_tutorial', 'test_params', ParamsTestCase)