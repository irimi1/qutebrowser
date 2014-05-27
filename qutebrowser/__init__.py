# Copyright 2014 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""A vim like browser based on Qt."""

import os.path

__author__ = "Florian Bruhin"
__copyright__ = "Copyright 2014 Florian Bruhin (The Compiler)"
__license__ = "GPL"
__maintainer__ = __author__
__email__ = "mail@qutebrowser.org"
__version_info__ = (0, 0, 0)
__version__ = '.'.join(map(str, __version_info__))

basedir = os.path.dirname(os.path.realpath(__file__))
