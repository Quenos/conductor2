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

from abc import ABC, abstractmethod


class _HTLC(ABC):
    def __init__(self, htlc=None):
        if htlc:
            self.update(htlc)
        else:
            self.incoming = None
            self.amount = 0

    @abstractmethod
    def update(self, htlc):
        self.incoming = htlc.incoming
        self.amount = htlc.amount


class HTLC(_HTLC):
    def __init__(self, htlc=None):
        super().__init__(htlc)
        if htlc:
            self.update(htlc)
        else:
            self.hashlock = None
            self.expiration_height = None

    def update(self, htlc):
        super().update(htlc)
        self.hashlock = htlc.hashlock
        self.expiration_height = htlc.expiration_height


class PendingHTLC(_HTLC):
    def __init__(self, htlc=None):
        super().__init__(htlc)
        if htlc:
            self.update(htlc)
        else:
            self.outpoint = None
            self.maturity_height = None
            self.blocks_til_maturity = None
            self.stage = None

    def update(self, htlc):
        self.outpoint = htlc.outpoint
        self.maturity_height = htlc.maturity_height
        self.blocks_til_maturity = htlc.blocks_til_maturity
        self.stage = htlc.stage
