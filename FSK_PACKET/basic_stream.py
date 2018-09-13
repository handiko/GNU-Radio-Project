#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Basic Stream
# Generated: Thu Sep 13 19:14:49 2018
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
        self.hdr_format = hdr_format = digital.header_format_default(digital.packet_utils.default_access_code, 0)
        
        
        self.enc = enc = fec.cc_encoder_make(8000, 7, 2, ([109,79]), 0, fec.CC_TERMINATED, False)
            
        
        
        self.dec = dec = fec.cc_decoder.make(2048, 7, 2, ([109,79]), 0, -1, fec.CC_TERMINATED, False)
            

        ##################################################
        # Blocks
        ##################################################
        self.fec_async_encoder_0 = fec.async_encoder(enc, True, False, False, 1500)
        self.fec_async_decoder_0 = fec.async_decoder(dec, False, False, 1500)
        self.digital_protocol_formatter_async_0 = digital.protocol_formatter_async(hdr_format)
        self.digital_map_bb_0 = digital.map_bb(([-1,1]))
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(True)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          1, 'payload')
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_tagged_stream_to_pdu_2 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'payload')
        self.blocks_tagged_stream_to_pdu_1 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'packet_len')
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(1, 8, 'payload', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_random_pdu_0 = blocks.random_pdu(10, 10, chr(0xFF), 2)
        self.blocks_pdu_to_tagged_stream_3 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_2 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 500)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))    
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.fec_async_decoder_0, 'in'))    
        self.msg_connect((self.blocks_tagged_stream_to_pdu_1, 'pdus'), (self.fec_async_encoder_0, 'in'))    
        self.msg_connect((self.blocks_tagged_stream_to_pdu_2, 'pdus'), (self.digital_crc32_async_bb_1, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.digital_protocol_formatter_async_0, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))    
        self.msg_connect((self.digital_protocol_formatter_async_0, 'header'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.msg_connect((self.digital_protocol_formatter_async_0, 'payload'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))    
        self.msg_connect((self.fec_async_decoder_0, 'out'), (self.blocks_pdu_to_tagged_stream_3, 'pdus'))    
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.blocks_pdu_to_tagged_stream_2, 'pdus'))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))    
        self.connect((self.blocks_pdu_to_tagged_stream_2, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_3, 0), (self.digital_correlate_access_code_xx_ts_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_map_bb_0, 0))    
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_tagged_stream_to_pdu_2, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_tagged_stream_to_pdu_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))    
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_repack_bits_bb_1, 0))    
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "basic_stream")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

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
