#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime


class Date(object):
    def __init__(self, date_string=''):
        if not date_string:
            self.date = datetime.date.today()
        else:
            self.date = datetime.datetime.strptime(date_string, '%Y%m%d')

    @property
    def today(self):
        """
        String format for today. It's a convenient way to get string
        format for today even if the given_date is not today.
        """
        return datetime.date.today().strftime('%Y%m%d')

    @property
    def now(self):
        """Datetime object for now."""
        return datetime.datetime.now()

    @property
    def day_before(self):
        """String format for the day before given_date."""
        return (self.date - datetime.timedelta(1)).strftime('%Y%m%d')

    @property
    def day_after(self):
        """String format for the day after given_date."""
        return (self.date + datetime.timedelta(1)).strftime('%Y%m%d')

    # It's for three-columns ui, in the future we may implementation
    # it with javascript.
    def date_range(self, num):
        """Return a string format date list according to the range num."""
        date_range = [
            (self.date - datetime.timedelta(i)).strftime('%Y%m%d')
            for i in range(num)
        ]
        return date_range
