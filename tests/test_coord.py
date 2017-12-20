import unittest
from coord import Coord3d

class TestCoord3d(unittest.TestCase):

    def test_create(self):
        c = Coord3d(5, 6, 7)
        self.assertEqual((c.x, c.y, c.z), (5, 6, 7))

    def test_create_empty(self):
        c = Coord3d()
        self.assertEqual((c.x, c.y, c.z), (0, 0, 0))

    def test_clone(self):
        c = Coord3d(5, 6, 7)
        c2 = Coord3d(c)

    def test_tuple(self):
        c = Coord3d(8, 9, 10)
        self.assertEqual(c.tuple(), (8, 9, 10))
        self.assertEqual(c.tuple(3), (8, 9 ,10))
        self.assertEqual(c.tuple(2), (8, 9))
        self.assertRaises(lambda: c.tuple(1))
        self.assertRaises(lambda: c.tuple(4))

    def test_scaled(self):
        c = Coord3d(2, 3, 4)
        c2 = c.scaled(2)
        self.assertEqual(c.tuple(), (2, 3, 4))
        self.assertEqual(c2.tuple(), (4, 6, 8))

    def test_crossed(self):
        c = Coord3d(3, 2, 1).crossed(Coord3d(-4, 7, 1))
        self.assertEqual(c.tuple(), (-5, -7, 29))

    def test_plus(self):
        c = Coord3d(1, 2, 3).plus(Coord3d(4, 5, 6))
        self.assertEqual(c.tuple(), (5, 7, 9))

    def test_minus(self):
        c = Coord3d(5, 6, 7).minus(Coord3d(3, 2, 1))
        self.assertEqual(c.tuple(), (2, 4, 6))

    def test_grow(self):
        c = Coord3d(-1, 1, 3).grow(10)
        self.assertEqual(c.tuple(), (-11, 11, 13))

    def test_times(self):
        c = Coord3d(1, 2, 3).times(Coord3d(2, 3, 4))
        self.assertEqual(c.tuple(), (2, 6, 12))

    def test_over(self):
        c = Coord3d(2, 6, 12).over(Coord3d(2, 3, 4))
        self.assertEqual(c.tuple(), (1, 2, 3))

    def test_equals(self):
        not_equal = Coord3d(1, 2, 3).equals(Coord3d(2, 2, 3))
        self.assertFalse(not_equal)
        not_equal = Coord3d(1, 2, 3).equals(Coord3d(1, 3, 3))
        self.assertFalse(not_equal)
        not_equal = Coord3d(1, 2, 3).equals(Coord3d(1, 2, 4))
        self.assertFalse(not_equal)
        equal = Coord3d(1, 2, 3).equals(Coord3d(1, 2, 3))
        self.assertTrue(equal)

    def test_compliment(self):
        c = Coord3d(10, -10, 20).compliment()
        self.assertEqual(c.tuple(), (-10, 10, -20))

    def test_dotted(self):
        dp = Coord3d(1, 2, 3).dotted(Coord3d(4, -5, 6))
        self.assertEqual(dp, 12)

    def test_normalized(self):
        n = Coord3d(10, 10, 10).normalized()
        strvals = (str(n.x)[:5], str(n.y)[:5], str(n.z)[:5])
        self.assertEqual(strvals, ('0.577', '0.577', '0.577'))

    def test_length_sqr(self):
        l2 = Coord3d(10, 10, 10).length_sqr()
        self.assertEqual(l2, 300)

    def test_length(self):
        l = Coord3d(10, 10, 20).length()
        self.assertEqual(str(l)[:5], '24.49')

    def  test_clamped(self):
        c = Coord3d(10, 10, 10)
        self.assertEqual(c.clamped(20).tuple(), (10, 10, 10))
        strs = [str(axis)[:3] for axis in c.clamped(17).tuple()]
        self.assertEqual(strs, ['9.8', '9.8' ,'9.8'])
