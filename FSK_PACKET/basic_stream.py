#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Basic Stream
# Generated: Tue Sep 11 17:18:17 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sys


class basic_stream(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Basic Stream")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Basic Stream")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "basic_stream")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        
        
        self.enc = enc = fec.cc_encoder_make(8000, 7, 2, ([79,109]), 0, fec.CC_TERMINATED, False)
            
        
        
        self.dec = dec = fec.cc_decoder.make(2048, 7, 2, ([79,109]), 0, -1, fec.CC_TERMINATED, False)
            

        ##################################################
        # Blocks
        ##################################################
        self.fec_async_encoder_0 = fec.async_encoder(enc, False, True, True, 1500)
        self.fec_async_decoder_0 = fec.async_decoder(dec, False, True, 1500)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(True)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(False)
        self.blocks_random_pdu_0_0_0 = blocks.random_pdu(10, 10, chr(0xFF), 1)
        self.blocks_random_pdu_0_0 = blocks.random_pdu(10, 10, chr(0xFF), 1)
        self.blocks_random_pdu_0 = blocks.random_pdu(10, 10, chr(0xFF), 1)
        self.blocks_message_strobe_0_0_0 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_debug_5 = blocks.message_debug()
        self.blocks_message_debug_4 = blocks.message_debug()
        self.blocks_message_debug_3 = blocks.message_debug()
        self.blocks_message_debug_2 = blocks.message_debug()
        self.blocks_message_debug_1 = blocks.message_debug()
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.blocks_random_pdu_0_0, 'generate'))    
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.blocks_random_pdu_0_0_0, 'generate'))    
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.blocks_message_debug_0, 'print_pdu'))    
        self.msg_connect((self.blocks_random_pdu_0_0, 'pdus'), (self.blocks_message_debug_0_0, 'print_pdu'))    
        self.msg_connect((self.blocks_random_pdu_0_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))    
        self.msg_connect((self.blocks_random_pdu_0_0_0, 'pdus'), (self.blocks_message_debug_3, 'print_pdu'))    
        self.msg_connect((self.blocks_random_pdu_0_0_0, 'pdus'), (self.fec_async_encoder_0, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.blocks_message_debug_1, 'print_pdu'))    
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_message_debug_2, 'print_pdu'))    
        self.msg_connect((self.fec_async_decoder_0, 'out'), (self.blocks_message_debug_5, 'print_pdu'))    
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.blocks_message_debug_4, 'print_pdu'))    
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.fec_async_decoder_0, 'in'))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "basic_stream")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_enc(self):
        return self.enc

    def set_enc(self, enc):
        self.enc = enc

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec


def main(top_block_cls=basic_stream, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
