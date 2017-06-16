"""
Copyright (c) 2012-2015 RockStor, Inc. <http://rockstor.com>
This file is part of RockStor.

RockStor is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

RockStor is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import json
import sys
from storageadmin.views.rockon_json import rockons


def main():
    out_file = sys.argv[1]
    with open(out_file, 'w') as ofo:
        json.dump(rockons, ofo, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()