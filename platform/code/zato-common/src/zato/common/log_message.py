# -*- coding: utf-8 -*-

"""
Copyright (C) 2011 Dariusz Suchojad <dsuch at gefira.pl>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# The constants below don't use the Bunch class because we don't need to iterate
# over them at all.

# LMC stands for the 'log message code'
# RID stands for the 'request ID'

# Needs to be kept in sync with zato.common.util.new_req_id
RID_LENGTH = 24

NULL_LMC = '0000.0000'
NULL_RID = '0' * RID_LENGTH