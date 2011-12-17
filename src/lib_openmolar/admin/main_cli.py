#! /usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
##                                                                           ##
##  Copyright 2010, Neil Wallace <rowinggolfer@googlemail.com>               ##
##                                                                           ##
##  This program is free software: you can redistribute it and/or modify     ##
##  it under the terms of the GNU General Public License as published by     ##
##  the Free Software Foundation, either version 3 of the License, or        ##
##  (at your option) any later version.                                      ##
##                                                                           ##
##  This program is distributed in the hope that it will be useful,          ##
##  but WITHOUT ANY WARRANTY; without even the implied warranty of           ##
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            ##
##  GNU General Public License for more details.                             ##
##                                                                           ##
##  You should have received a copy of the GNU General Public License        ##
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.    ##
##                                                                           ##
###############################################################################

from lib_openmolar.admin.db_tools.proxy_manager import ProxyManager

class AdminMain(ProxyManager):
    '''
    This class is the core commandline application.
    '''

    def __init__(self):
        self.log("cli is up and running!")

    def log(self, message=""):
        '''
        pass a message onto the logger
        '''
        LOGGER.info(message)

def main():
    admin = AdminMain()
    admin.init_proxy()

if __name__ == "__main__":
    import gettext
    gettext.install("openmolar")
    sys.exit(main())