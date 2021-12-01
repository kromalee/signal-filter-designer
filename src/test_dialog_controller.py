import os
import wave
from PyQt5.QtWidgets import QDialog, QFileDialog
from src.test_dialog_ui_rc import Ui_Dialog
import numpy as np
from scipy import signal as sg


class TestDialog(QDialog, Ui_Dialog):
    def __init__(self, signal_filter=None):
        super(TestDialog, self).__init__()
        self.setupUi(self)
        self.signal_filter = signal_filter
        TestDialog.setFixedSize(self, 1366, 768)
        self.setWindowTitle('滤波器测试')
        sampling_rate = 8000
        t = np.arange(0, 1.0, 1.0 / sampling_rate)
        x = np.sin(2 * np.pi * 156.25 * t) + 2 * np.sin(2 * np.pi * 234.375 * t)
        # x = np.sin(2 * np.pi * 400 * t) + 2 * np.sin(2 * np.pi * 1000 * t)

        self.wavePlot.plot(t, x, pen='b', alpha=0.75)
        if hasattr(signal_filter, 'b') and hasattr(signal_filter, 'a'):
            self.wavePlot.plot(t, sg.lfilter(signal_filter.b, signal_filter.a, x), pen='r', alpha=0.75)
        else:
            self.wavePlot.plot(t, sg.lfilter(signal_filter.taps, 1.0, x), pen='r', alpha=0.75)
        self.wavePlot.setLabel(axis="left", text="幅值")
        self.wavePlot.setLabel(axis="bottom", text="归一化时间 (pi*rad/sample)")

        # 频域分析 - 原始信号
        fft_size = 512
        t = np.arange(0, 1.0, 1.0 / sampling_rate)
        xs = x[:fft_size]
        xf = np.fft.rfft(xs) / fft_size
        freqs = np.linspace(0, sampling_rate // 2, fft_size // 2 + 1)
        xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
        self.wavePlotFBefore.plot(freqs, xfp)
        self.wavePlotFBefore.setLabel(axis="left", text="幅值")
        self.wavePlotFBefore.setLabel(axis="bottom", text="频率 (Hz)")

        # 频域分析 -滤波后信号
        if hasattr(signal_filter, 'b') and hasattr(signal_filter, 'a'):
            x_after = sg.lfilter(signal_filter.b, signal_filter.a, x)
        else:
            x_after = sg.lfilter(signal_filter.taps, 1.0, x)
        x_after_s = x_after[:fft_size]
        x_after_f = np.fft.rfft(x_after_s) / fft_size
        x_after_fp = 20 * np.log10(np.clip(np.abs(x_after_f), 1e-20, 1e100))
        self.wavePlotFAfter.plot(freqs, x_after_fp)
        self.wavePlotFAfter.setLabel(axis="left", text="幅值")
        self.wavePlotFAfter.setLabel(axis="bottom", text="频率 (Hz)")

    # def draw_plot(self):
    #     pass

    # def open_file(self):
    #     path = QFileDialog.getOpenFileName(self, "Open File Dialog", ".",
    #                                        "波形文件(*.wav)")
    #     self.path.setText(str(path[0]))
    #     f = wave.open(path[0], "rb")
    #     # 读取格式信息
    #     # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    #     params = f.getparams()
    #     nchannels, sampwidth, framerate, nframes = params[:4]
    #     print(framerate)
    #     # print(len(nframes))
    #     # 读取波形数据
    #     str_data = f.readframes(nframes)
    #     f.close()
    #     # 将波形数据转换为数组
    #     wave_data = np.fromstring(str_data, dtype=np.short)
    #     wave_data.shape = -1, 2
    #     wave_t_data = wave_data.T
    #     time = np.arange(0, nframes) * (1.0 / framerate)
    #
    #     # 将过滤器应用于data。使用lfilter_zi选择过滤器的初始条件：
    #     b, a = self.signal_filter.b, self.signal_filter.a
    #
    #     self.wavePlot.plot(time, wave_t_data[0], pen='b', alpha=0.75)
    #     self.wavePlot.plot(time, sg.filtfilt(b, a, wave_t_data[0]), pen='r', alpha=0.75)
