#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ws
# Generated: Sat Sep 15 17:49:03 2018
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class ws(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ws")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ws")
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

        self.settings = Qt.QSettings("GNU Radio", "ws")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.length = length = 32
        self.freq = freq = 1000

        ##################################################
        # Blocks
        ##################################################
        self._freq_range = Range(100, 2000, 10, 1000, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, "freq", "counter_slider", float)
        self.top_layout.addWidget(self._freq_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	4096, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, length)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, length)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1.0/16, ))
        self.blocks_delay_0_3 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_2_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_2 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_1_1 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_1_0_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0_2 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0_1_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0_1 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0_0_1 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*length, 1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(length)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_delay_0_1, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_delay_0_2, 0))    
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.blocks_add_xx_0, 8))    
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.blocks_delay_0_3, 0))    
        self.connect((self.blocks_delay_0_0_0_1, 0), (self.blocks_add_xx_0, 12))    
        self.connect((self.blocks_delay_0_0_0_1, 0), (self.blocks_delay_0_2_0, 0))    
        self.connect((self.blocks_delay_0_0_1, 0), (self.blocks_add_xx_0, 6))    
        self.connect((self.blocks_delay_0_0_1, 0), (self.blocks_delay_0_1_0, 0))    
        self.connect((self.blocks_delay_0_0_1_0, 0), (self.blocks_add_xx_0, 14))    
        self.connect((self.blocks_delay_0_0_1_0, 0), (self.blocks_delay_0_1_0_0, 0))    
        self.connect((self.blocks_delay_0_0_2, 0), (self.blocks_add_xx_0, 10))    
        self.connect((self.blocks_delay_0_0_2, 0), (self.blocks_delay_0_1_1, 0))    
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_delay_0_0_0, 0))    
        self.connect((self.blocks_delay_0_1_0, 0), (self.blocks_add_xx_0, 7))    
        self.connect((self.blocks_delay_0_1_0, 0), (self.blocks_delay_0_0_0_0, 0))    
        self.connect((self.blocks_delay_0_1_0_0, 0), (self.blocks_add_xx_0, 15))    
        self.connect((self.blocks_delay_0_1_1, 0), (self.blocks_add_xx_0, 11))    
        self.connect((self.blocks_delay_0_1_1, 0), (self.blocks_delay_0_0_0_1, 0))    
        self.connect((self.blocks_delay_0_2, 0), (self.blocks_add_xx_0, 5))    
        self.connect((self.blocks_delay_0_2, 0), (self.blocks_delay_0_0_1, 0))    
        self.connect((self.blocks_delay_0_2_0, 0), (self.blocks_add_xx_0, 13))    
        self.connect((self.blocks_delay_0_2_0, 0), (self.blocks_delay_0_0_1_0, 0))    
        self.connect((self.blocks_delay_0_3, 0), (self.blocks_add_xx_0, 9))    
        self.connect((self.blocks_delay_0_3, 0), (self.blocks_delay_0_0_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ws")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq)


def main(top_block_cls=ws, options=None):

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
