#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Audio modem FSK loop back test
# Author: Aaron Scher
# Description: Audio modem FSK loop back test
# Generated: Wed Sep 12 16:12:55 2018
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import epy_block_0
import math
import numpy
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0)):
        gr.top_block.__init__(self, "Audio modem FSK loop back test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Audio modem FSK loop back test")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.hdr_format = hdr_format

        ##################################################
        # Variables
        ##################################################
        self.nfilts = nfilts = 32
        self.SPS = SPS = 147
        self.RX_decimation = RX_decimation = 49
        self.EBW = EBW = .05
        self.samp_rate = samp_rate = 44.1E3
        self.fsk_deviation_hz = fsk_deviation_hz = 100
        self.carrier_freq = carrier_freq = 1.75E3
        
        self.RRC_filter_taps = RRC_filter_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, EBW, 5*SPS*nfilts/RX_decimation)
          

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=RX_decimation,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate/RX_decimation, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
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
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/RX_decimation, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_edit_box_msg_0 = qtgui.edit_box_msg(qtgui.STRING, '', '', False, False, '')
        self._qtgui_edit_box_msg_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_edit_box_msg_0_win)
        self.epy_block_0 = epy_block_0.msg_block()
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, 'len_key')
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_fff(SPS/RX_decimation, 6.28/400.0*2/70, (RRC_filter_taps), nfilts, nfilts/2, 2, 1)
        self.digital_correlate_access_code_xx_ts_1_0_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          2, 'len_key2')
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bf(((2*3.14*carrier_freq-2*3.14*fsk_deviation_hz,2*3.14*carrier_freq+2*3.14*fsk_deviation_hz)), 1)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.blocks_vector_source_x_0 = blocks.vector_source_b((1,0), True, 1, [])
        self.blocks_vco_f_0 = blocks.vco_f(samp_rate, 1, 1)
        self.blocks_tagged_stream_to_pdu_0_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'len_key2')
        self.blocks_tagged_stream_mux_1 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 200, 'len_key')
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, SPS-1)
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key2', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'len_key')
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.audio_source_0 = audio.source(44100, '', True)
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -carrier_freq, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz/8.0)/(RX_decimation))
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-60, .01, 0, True)
        self.analog_feedforward_agc_cc_0 = analog.feedforward_agc_cc(1024, 1.0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0_0, 'pdus'), (self.blocks_message_debug_0_0, 'print'))    
        self.msg_connect((self.epy_block_0, 'msg_out'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))    
        self.msg_connect((self.qtgui_edit_box_msg_0, 'msg'), (self.epy_block_0, 'msg_in'))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.analog_feedforward_agc_cc_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.analog_feedforward_agc_cc_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))    
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.digital_protocol_formatter_bb_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_tagged_stream_mux_1, 1))    
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.blocks_tagged_stream_to_pdu_0_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vco_f_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_1, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_1, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))    
        self.connect((self.blocks_vco_f_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_correlate_access_code_xx_ts_1_0_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.digital_correlate_access_code_xx_ts_1_0_0, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_binary_slicer_fb_0_0, 0))    
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_pwr_squelch_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_SPS(self):
        return self.SPS

    def set_SPS(self, SPS):
        self.SPS = SPS
        self.blocks_repeat_0.set_interpolation(self.SPS-1)

    def get_RX_decimation(self):
        return self.RX_decimation

    def set_RX_decimation(self, RX_decimation):
        self.RX_decimation = RX_decimation
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.RX_decimation)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.RX_decimation)
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0)/(self.RX_decimation))

    def get_EBW(self):
        return self.EBW

    def set_EBW(self, EBW):
        self.EBW = EBW

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.RX_decimation)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.RX_decimation)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0)/(self.RX_decimation))

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table(((2*3.14*self.carrier_freq-2*3.14*self.fsk_deviation_hz,2*3.14*self.carrier_freq+2*3.14*self.fsk_deviation_hz)))
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0)/(self.RX_decimation))

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table(((2*3.14*self.carrier_freq-2*3.14*self.fsk_deviation_hz,2*3.14*self.carrier_freq+2*3.14*self.fsk_deviation_hz)))
        self.analog_sig_source_x_1.set_frequency(-self.carrier_freq)

    def get_RRC_filter_taps(self):
        return self.RRC_filter_taps

    def set_RRC_filter_taps(self, RRC_filter_taps):
        self.RRC_filter_taps = RRC_filter_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.RRC_filter_taps))


def argument_parser():
    description = 'Audio modem FSK loop back test'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

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
