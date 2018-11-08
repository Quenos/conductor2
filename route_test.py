import unittest
import hop
import route


class RouteUnitTest(unittest.TestCase):

    def test_equal_same_order(self):
        print("equal routes and same order")

        r1 = route.Route()
        r2 = route.Route()
        h1 = hop.Hop(chan_id='1')
        h2 = hop.Hop(chan_id='1')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='2')
        h2 = hop.Hop(chan_id='2')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='3')
        h2 = hop.Hop(chan_id='3')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='4')
        h2 = hop.Hop(chan_id='4')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='5')
        h2 = hop.Hop(chan_id='5')
        r1.add_hop(h1)
        r2.add_hop(h2)
        self.assertEqual(r1, r2)

    def test_equal_diff_order(self):
        print("equal routes, but different order")

        r1 = route.Route()
        r2 = route.Route()
        h1 = hop.Hop(chan_id='1')
        h2 = hop.Hop(chan_id='2')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='2')
        h2 = hop.Hop(chan_id='3')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='3')
        h2 = hop.Hop(chan_id='4')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='4')
        h2 = hop.Hop(chan_id='5')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='5')
        h2 = hop.Hop(chan_id='1')
        r1.add_hop(h1)
        r2.add_hop(h2)
        self.assertEqual(r1, r2)

    def test_not_equal(self):
        print("equal routes, but one hop differs")

        r1 = route.Route()
        r2 = route.Route()
        h1 = hop.Hop(chan_id='1')
        h2 = hop.Hop(chan_id='1')
        r1.add_hop(h1)
        r2.add_hop(h2)
        h1 = hop.Hop(chan_id='2')
        h2 = hop.Hop(chan_id='2')
        r1.hops.append(h1)
        r2.hops.append(h2)
        h1 = hop.Hop(chan_id='3')
        h2 = hop.Hop(chan_id='103')
        r1.hops.append(h1)
        r2.hops.append(h2)
        h1 = hop.Hop(chan_id='4')
        h2 = hop.Hop(chan_id='4')
        r1.hops.append(h1)
        r2.hops.append(h2)
        h1 = hop.Hop(chan_id='5')
        h2 = hop.Hop(chan_id='5')
        r1.hops.append(h1)
        r2.hops.append(h2)
        self.assertNotEqual(r1, r2)

    def test_contains(self):
        r1 = route.Route()
        h1 = hop.Hop(chan_id='1')
        r1.add_hop(h1)
        h1 = hop.Hop(chan_id='2')
        r1.add_hop(h1)
        h1 = hop.Hop(chan_id='3')
        r1.add_hop(h1)
        h1 = hop.Hop(chan_id='4')
        r1.add_hop(h1)
        h1 = hop.Hop(chan_id='5')
        r1.add_hop(h1)
        self.assertTrue('3' in r1)

if __name__ == '__main__':
    unittest.main()
