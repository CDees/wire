from PyQt4 import QtGui
import os, sys

import lib.slay_display_gui

import lib.wire_setup_gui
import lib.wire_connect_gui
import lib.wire_home_gui

import slay


class slay_display(QtGui.QWidget, lib.slay_display_gui.Ui_slay_display):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


class wire_setup(QtGui.QWidget, lib.wire_setup_gui.Ui_wire_setup_display):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.wire_setup_hostname.returnPressed.connect(self.info)
        self.wire_setup_port.returnPressed.connect(self.info)

    def info(self):
        self.hostname = self.wire_setup_hostname.text()
        self.port = self.wire_setup_port.text()
        if len(self.hostname) and len(self.port) > 0:
            self.connection_info_validated = True

            self.slay_recv = slay.recv(self.hostname, self.port, slay_rsa, wire_home, slay_display)
            self.slay_recv.start()

            self.close()
            wire_connect.show()


class wire_connect(QtGui.QWidget, lib.wire_connect_gui.Ui_wire_connect_display):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.wire_connect_hostname.returnPressed.connect(self.info)
        self.wire_connect_port.returnPressed.connect(self.info)

    def info(self):
        self.hostname = self.wire_connect_hostname.text()
        self.port = self.wire_connect_port.text()
        if len(self.hostname) and len(self.port) > 0:
            self.connection_info_validated = True

            self.slay_send = slay.send(self.hostname, self.port, slay_rsa,
                                  wire_setup.slay_recv, wire_home, slay_display)
            self.slay_send.start()

            self.close()
            slay_display.show()
            wire_home.show()


class wire_home(QtGui.QWidget, lib.wire_home_gui.Ui_wire_home_display):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.wire_home_message.returnPressed.connect(self.send)
        self.capture_public_key_validated = False

    def send(self):
        if self.capture_public_key_validated == False:
            session_key = wire_setup.slay_recv.capture_public_key
            wire_connect.slay_send.session_key(session_key)
            self.capture_public_key_validated = True
            self.send()

        if self.capture_public_key_validated == True:
            wire_connect.slay_send.send_message()


# ws.hostname    //    self-hostname
# ws.port        //    self-port
# wc.hostname    //    self-hostname
# wc.port        //    self-port


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    ###-------------###
    slay_display = slay_display()
    wire_setup = wire_setup()
    wire_connect = wire_connect()
    wire_home = wire_home()
    ###-------------###

    ###-------------###
    slay_rsa = slay.rsa_layer()
    ###-------------###

    wire_setup.show()


###-------------------------------------------------------------------------###
    sys.exit(app.exec_())
