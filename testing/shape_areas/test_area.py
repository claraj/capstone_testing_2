from unittest import TestCase
import area


class TestShapeAreasTriangles(TestCase):

    def test_triangle_area(self):
        # A triangle with height 4 and base 5 should have area 10
        self.assertEqual(10, area.triangle_area(4, 5))


    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))


    def test_triangle_negative_height_base_raises_value_exception(self):

        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)


    def test_triangle_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 1))
        self.assertEqual(0, area.triangle_area(1, 0))
        self.assertEqual(0, area.triangle_area(0, 0))



class TestShapeAreaCircles(TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(314.1592653589, area.circle_area(10))


    def test_circle_area_zero_radius(self):
        self.assertEqual(0, area.circle_area(0))


    def test_circle_area_value_error_negative_radius(self):
        with self.assertRaises(ValueError):
            area.circle_area(-10)
