# Copyright 2018 <Quenos Blockchain R&D KFT>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import unittest
from lightning import hop, route


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
