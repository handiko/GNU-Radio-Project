#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx Wav
# Generated: Thu Oct 18 08:08:52 2018
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys


class tx_wav(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tx Wav")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tx Wav")
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

        self.settings = Qt.QSettings("GNU Radio", "tx_wav")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48e3
        self.freq = freq = samp_rate/4
        self.amp = amp = 3

        ##################################################
        # Blocks
        ##################################################
        self._freq_range = Range(1e2, samp_rate/2, 1, samp_rate/4, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, "freq", "counter_slider", float)
        self.top_layout.addWidget(self._freq_win)
        self._amp_range = Range(-40, 20, 1, 3, 200)
        self._amp_win = RangeWidget(self._amp_range, self.set_amp, "amp", "counter_slider", float)
        self.top_layout.addWidget(self._amp_win)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.complex_band_pass(pow(10.0,amp/10.0),samp_rate,-3000,-300,100,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((0, ))
        self.audio_sink_0 = audio.sink(int(samp_rate), '', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 0.1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, pow(10.0,amp/10.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.audio_sink_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_add_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tx_wav")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_freq(self.samp_rate/4)
        self.fft_filter_xxx_0.set_taps((firdes.complex_band_pass(pow(10.0,self.amp/10.0),self.samp_rate,-3000,-300,100,firdes.WIN_BLACKMAN)))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq)

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp
        self.fft_filter_xxx_0.set_taps((firdes.complex_band_pass(pow(10.0,self.amp/10.0),self.samp_rate,-3000,-300,100,firdes.WIN_BLACKMAN)))
        self.analog_noise_source_x_0.set_amplitude(pow(10.0,self.amp/10.0))


def main(top_block_cls=tx_wav, options=None):

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
