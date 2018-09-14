#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Basic Stream
# Generated: Fri Sep 14 10:37:21 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sip
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
        self.noise = noise = -3.0
        self.hdr_format = hdr_format = digital.header_format_default(digital.packet_utils.default_access_code, 0)
        
        
        self.enc = enc = fec.cc_encoder_make(8192, 7, 2, ([109,79]), 0, fec.CC_TERMINATED, False)
            
        
        
        self.dec = dec = fec.cc_decoder.make(8192, 7, 2, ([109,79]), 0, -1, fec.CC_TERMINATED, False)
            
        
        self.const = const = digital.constellation_bpsk().base()
        

        ##################################################
        # Blocks
        ##################################################
        self._noise_range = Range(-30.0, 3.0, 1.0, -3.0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "noise", "counter_slider", float)
        self.top_layout.addWidget(self._noise_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.fec_async_encoder_0 = fec.async_encoder(enc, True, False, False, 1500)
        self.fec_async_decoder_0 = fec.async_decoder(dec, True, False, 1500)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(True)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(False)
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(const)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([-1,1]), 1)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'packet_len')
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_random_pdu_0 = blocks.random_pdu(10, 400, chr(0xFF), 2)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 500)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, pow(10.0,noise/10.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))    
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.fec_async_decoder_0, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.fec_async_encoder_0, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))    
        self.msg_connect((self.fec_async_decoder_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))    
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "basic_stream")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(pow(10.0,self.noise/10.0))

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

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const


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
