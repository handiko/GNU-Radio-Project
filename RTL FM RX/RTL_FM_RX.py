#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: RTL SDR FM RX
# Generated: Wed Sep 19 13:12:33 2018
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import osmosdr
import sip
import sys
import time


class RTL_FM_RX(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RTL SDR FM RX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RTL SDR FM RX")
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

        self.settings = Qt.QSettings("GNU Radio", "RTL_FM_RX")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.88e6
        self.rfgain = rfgain = 10
        self.freq = freq = 103.8
        self.ch_rate = ch_rate = 240e3
        self.audio_mute = audio_mute = False
        self.audio_cut = audio_cut = 12e3
        self.afgain = afgain = -10

        ##################################################
        # Blocks
        ##################################################
        self._rfgain_range = Range(0, 49, 0.1, 10, 200)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'RF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rfgain_win, 2,0,1,1)
        self._freq_range = Range(88.0, 108.0, 0.1, 103.8, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Freq (MHz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 1,0,1,3)
        _audio_mute_check_box = Qt.QCheckBox('Audio Mute')
        self._audio_mute_choices = {True: True, False: False}
        self._audio_mute_choices_inv = dict((v,k) for k,v in self._audio_mute_choices.iteritems())
        self._audio_mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_audio_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._audio_mute_choices_inv[i]))
        self._audio_mute_callback(self.audio_mute)
        _audio_mute_check_box.stateChanged.connect(lambda i: self.set_audio_mute(self._audio_mute_choices[bool(i)]))
        self.top_layout.addWidget(_audio_mute_check_box)
        self._afgain_range = Range(-20, 3, 0.1, -10, 200)
        self._afgain_win = RangeWidget(self._afgain_range, self.set_afgain, 'AF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._afgain_win, 2,1,1,1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(ch_rate),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq*1e6, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [0.75, 1.0, 1.0, 1.0, 1.0,
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq*1e6, 0)
        self.osmosdr_source_0.set_freq_corr(55, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rfgain, 0)
        self.osmosdr_source_0.set_if_gain(0, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_1 = filter.fir_filter_fff(10, firdes.low_pass(
        	pow(10,afgain/10), 240e3, audio_cut, audio_cut/2, firdes.WIN_HAMMING, 6.76))
        self.blks2_valve_0 = grc_blks2.valve(item_size=gr.sizeof_float*1, open=bool(audio_mute))
        self.audio_sink_0 = audio.sink(int(ch_rate/10), '', True)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(ch_rate/(2*math.pi*250e3/8.0))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_1, 0))    
        self.connect((self.blks2_valve_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.blks2_valve_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "RTL_FM_RX")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq*1e6, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.osmosdr_source_0.set_gain(self.rfgain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq*1e6, self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.freq*1e6, 0)

    def get_ch_rate(self):
        return self.ch_rate

    def set_ch_rate(self, ch_rate):
        self.ch_rate = ch_rate
        self.analog_quadrature_demod_cf_0.set_gain(self.ch_rate/(2*math.pi*250e3/8.0))

    def get_audio_mute(self):
        return self.audio_mute

    def set_audio_mute(self, audio_mute):
        self.audio_mute = audio_mute
        self._audio_mute_callback(self.audio_mute)
        self.blks2_valve_0.set_open(bool(self.audio_mute))

    def get_audio_cut(self):
        return self.audio_cut

    def set_audio_cut(self, audio_cut):
        self.audio_cut = audio_cut
        self.low_pass_filter_1.set_taps(firdes.low_pass(pow(10,self.afgain/10), 240e3, self.audio_cut, self.audio_cut/2, firdes.WIN_HAMMING, 6.76))

    def get_afgain(self):
        return self.afgain

    def set_afgain(self, afgain):
        self.afgain = afgain
        self.low_pass_filter_1.set_taps(firdes.low_pass(pow(10,self.afgain/10), 240e3, self.audio_cut, self.audio_cut/2, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=RTL_FM_RX, options=None):

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
