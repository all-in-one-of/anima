# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import logging
import unittest
import sys

from anima.pipeline.ui import IS_PYSIDE, IS_PYQT4

logger = logging.getLogger('anima.pipeline.ui.reference_editor')


if IS_PYSIDE():
    logger.debug('environment is set to pyside, importing pyside')
    from PySide import QtCore, QtGui
    from PySide.QtTest import QTest
    from PySide.QtCore import Qt
elif IS_PYQT4():
    logger.debug('environment is set to pyqt4, importing pyqt4')
    import sip
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtTest import QTest
    from PyQt4.QtCore import Qt


from anima.pipeline.ui import reference_editor



class ReferenceEditorTestCase(unittest.TestCase):

    def setUp(self):
        """set up the test environment
        """
        if not QtGui.QApplication.instance():
            logger.debug('creating a new QApplication')
            self.app = QtGui.QApplication(sys.argv)
        else:
            logger.debug('using the present QApplication: %s' % QtGui.qApp)
            # self.app = QtGui.qApp
            self.app = QtGui.QApplication.instance()

    def tearDown(self):
        """clean up the test environment
        """
        pass

    def show_dialog(self, dialog):
        """show the given dialog
        """
        dialog.show()
        self.app.exec_()
        self.app.connect(
            self.app,
            QtCore.SIGNAL("lastWindowClosed()"),
            self.app,
            QtCore.SLOT("quit()")
        )

    def test_close_button_closes_the_UI(self):
        """testing if the close button is closing the UI when clicked
        """
        dialog = reference_editor.MainDialog()
        #self.show_dialog(dialog)
        QTest.mouseClick(dialog.buttonBox.buttons()[0], Qt.LeftButton)
        self.assertFalse(dialog.isVisible())

    
