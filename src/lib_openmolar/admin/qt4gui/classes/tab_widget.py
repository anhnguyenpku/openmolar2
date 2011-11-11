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


from PyQt4 import QtCore, QtGui, QtWebKit

from lib_openmolar.common.widgets.closeable_tab_widget import ClosableTabWidget

class AdminTabWidget(ClosableTabWidget):
    '''
    a minor re-implementation of the closeabletabwidget from openmolar common
    uses a toolbutton as the right widget, and has some custom signals
    '''
    def __init__(self, parent=None):
        super(AdminTabWidget, self).__init__(parent)

        action_close = QtGui.QAction(_("Close Tabs"), self)
        action_close.triggered.connect(self.closeAll)

        action_new_table = QtGui.QAction(_("New Table Viewer"), self)
        action_new_table.triggered.connect(self.new_table)

        action_new_query = QtGui.QAction(_("New Query Tool"), self)
        action_new_query.triggered.connect(self.new_query)

        menu = QtGui.QMenu(self)
        menu.addAction(action_close)
        menu.addSeparator()
        menu.addAction(action_new_table)
        menu.addAction(action_new_query)

        icon = QtGui.QIcon.fromTheme("preferences-desktop")
        menu_button = QtGui.QToolButton(self)
        menu_button.setIcon(icon)
        menu_button.setText(_("Options"))
        menu_button.setPopupMode(menu_button.InstantPopup)
        menu_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        menu_button.setMenu(menu)

        self.setCornerWidget(menu_button)

        self.currentChanged.connect(self._tab_changed)

        self.browser = QtWebKit.QWebView()
        self.addTab(self.browser, _("Messages"))

    def closeAll(self):
        if self.count() > 1:
            ClosableTabWidget.closeAll(self, _("Disconnect and"))
            self.addTab(self.browser, _("Messages"))

    def _tab_changed(self, i):
        try:
            ## if the current widget is a query tool, the query history
            ## may have been updated by another instance
            self.widget(i).get_history()
        except AttributeError:
            ## fail quietly!
            pass

    def new_query(self):
        self.emit(QtCore.SIGNAL("new query tab"))

    def new_table(self):
        self.emit(QtCore.SIGNAL("new table tab"))

if __name__ == "__main__":
    import gettext
    gettext.install("")

    app = QtGui.QApplication([])
    dl = QtGui.QDialog()
    dl.setMinimumSize(400,200)
    stw = AdminTabWidget(dl)

    label1 = QtGui.QLabel("Placeholder1")
    label2 = QtGui.QLabel("Placeholder2")
    stw.addTab(label1, "one")
    stw.addTab(label2, "two")

    layout = QtGui.QVBoxLayout(dl)
    layout.addWidget(stw)

    dl.exec_()