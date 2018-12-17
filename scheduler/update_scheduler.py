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

from PyQt5 import QtCore
from enum import Enum


class UpdateScheduler(object):
    tasks = []

    class TaskStatus(Enum):
        Started = 1
        Stopped = 2

    @staticmethod
    def register(identifier, update_func, interval=30000, start=True, immediate=False):

        # check if the identifier is unique
        for t in UpdateScheduler.tasks:
            if t['identifier'] == identifier:
                raise ValueError('identifier already exists')

        timer = QtCore.QTimer()
        timer.setSingleShot(False)
        timer.timeout.connect(update_func)

        if immediate:
            update_func()

        if start:
            timer.start(interval)
            status = UpdateScheduler.TaskStatus.Started
        else:
            status = UpdateScheduler.TaskStatus.Stopped

        UpdateScheduler.tasks.append(
            {'identifier': identifier,
             'function': update_func,
             'interval': interval,
             'timer': timer,
             'status': status})

    @staticmethod
    def deregister(identifier):
        to_remove = None
        for t in UpdateScheduler.tasks:
            if t['identifier'] == identifier:
                t['timer'].stop()
                to_remove = t
                break
        if to_remove is not None:
            UpdateScheduler.tasks.remove(to_remove)

    @staticmethod
    def start(identifier):
        for t in UpdateScheduler.tasks:
            if t['identifier'] == identifier:
                t['timer'].start(t['interval'])
                t['status'] = UpdateScheduler.TaskStatus.Started

    @staticmethod
    def stop(identifier):
        for t in UpdateScheduler.tasks:
            if t['identifier'] == identifier:
                t['timer'].stop()
                t['status'] = UpdateScheduler.TaskStatus.Stopped

    @staticmethod
    def trigger(identifier, parameter=None):
        for t in UpdateScheduler.tasks:
            if t['identifier'] == identifier:
                if t['status'] == UpdateScheduler.TaskStatus.Started:
                    t['timer'].stop()
                if parameter is None:
                    t['function']()
                else:
                    t['function'](parameter)
                    if t['status'] == UpdateScheduler.TaskStatus.Started:
                        t['timer'].start(t['interval'])
