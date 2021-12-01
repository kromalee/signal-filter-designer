from src.const_enum_dict import ResponseTypeEnum, DesignMethodEnum, OrderTypeEnum, iir_design_method_map, \
    response_type_map, window_type_name_map, ImpulseResponseTypeEnum, impulse_response_type_map, WindowTypeEnum, \
    impulse_response_features_map, features_map, design_method_name_map
from scipy import signal
from logging import getLogger
import numpy as np

log = getLogger(__name__)


class SignalFilter:

    def __init__(self, state):
        self.state = state
        is_iir = DesignMethodEnum.BUTTER_WORTH <= state.designMethod <= DesignMethodEnum.ELLIPTIC
        self.is_iir = is_iir
        is_mini_order = state.orderType == OrderTypeEnum.MINI_ORDER
        is_single_band = state.responseType in [ResponseTypeEnum.LOW_PASS, ResponseTypeEnum.HIGH_PASS]
        if is_iir:
            self.state.impulseResponseType = ImpulseResponseTypeEnum.IIR
        else:
            self.state.impulseResponseType = ImpulseResponseTypeEnum.FIR
        if is_iir and (not is_mini_order):
            is_with_rp_rs = DesignMethodEnum.CHEBYSHEV_1 <= state.designMethod <= DesignMethodEnum.ELLIPTIC

            if is_single_band and (not is_with_rp_rs):
                self.b, self.a = self.iir_filter_helper(state.order,
                                                        state.fc1,
                                                        None,
                                                        None,
                                                        iir_design_method_map[state.designMethod],
                                                        response_type_map[state.responseType],
                                                        state.fs
                                                        )
            elif is_single_band and is_with_rp_rs:
                self.b, self.a = self.iir_filter_helper(state.order,
                                                        state.fc1,
                                                        state.rp,
                                                        state.rs,
                                                        iir_design_method_map[state.designMethod],
                                                        response_type_map[state.responseType],
                                                        state.fs
                                                        )
            elif (not is_single_band) and is_with_rp_rs:
                self.b, self.a = self.iir_filter_helper(state.order,
                                                        [state.fc1, state.fc2],
                                                        state.rp,
                                                        state.rs,
                                                        iir_design_method_map[state.designMethod],
                                                        response_type_map[state.responseType],
                                                        state.fs
                                                        )
            elif (not is_single_band) and (not is_with_rp_rs):
                self.b, self.a = self.iir_filter_helper(state.order,
                                                        [state.fc1, state.fc2],
                                                        None, None,
                                                        iir_design_method_map[state.designMethod],
                                                        response_type_map[state.responseType],
                                                        state.fs
                                                        )

        elif is_iir and is_mini_order:
            # IIR 最小阶📔
            if state.responseType in [ResponseTypeEnum.LOW_PASS]:
                wp = state.fe1
                ws = state.fe2
                fs = state.fs
            elif state.responseType in [ResponseTypeEnum.HIGH_PASS]:
                ws = state.fe1
                wp = state.fe2
                fs = state.fs
            elif state.responseType in [ResponseTypeEnum.BAND_PASS]:
                wp = [state.fe2 * 2 / state.fs, state.fe3 * 2 / state.fs]
                ws = [state.fe1 * 2 / state.fs, state.fe4 * 2 / state.fs]
                fs = 2.0
            elif state.responseType in [ResponseTypeEnum.BAND_STOP]:
                ws = [state.fe2 * 2 / state.fs, state.fe3 * 2 / state.fs]
                wp = [state.fe1 * 2 / state.fs, state.fe4 * 2 / state.fs]
                fs = 2.0
            if state.designMethod in [DesignMethodEnum.BUTTER_WORTH]:
                self.state.order = signal.buttord(wp, ws, state.rp, state.rs, analog=False, fs=state.fs)[0]
            elif state.designMethod in [DesignMethodEnum.CHEBYSHEV_1]:
                self.state.order = signal.cheb1ord(wp, ws, state.rp, state.rs, analog=False, fs=state.fs)[0]
            elif state.designMethod in [DesignMethodEnum.CHEBYSHEV_2]:
                self.state.order = signal.cheb2ord(wp, ws, state.rp, state.rs, analog=False, fs=state.fs)[0]
            elif state.designMethod in [DesignMethodEnum.ELLIPTIC]:
                self.state.order = signal.ellipord(wp, ws, state.rp, state.rs, analog=False, fs=state.fs)[0]
            else:
                pass
            self.b, self.a = signal.iirdesign(wp, ws,
                                              state.rp, state.rs,
                                              analog=False,
                                              ftype=iir_design_method_map[state.designMethod],
                                              fs=state.fs)

            #     计算order

        elif (not is_iir) and (not is_mini_order):
            if is_single_band:
                self.taps = self.fir_filter_window_helper(state.order,
                                                          state.fc1,
                                                          window_type_name_map[state.windowType],
                                                          response_type_map[state.responseType],
                                                          state.scale,
                                                          state.fs
                                                          )
            else:
                self.taps = self.fir_filter_window_helper_band(state.order,
                                                               state.fc1,
                                                               state.fc2,
                                                               window_type_name_map[state.windowType],
                                                               response_type_map[state.responseType],
                                                               state.scale,
                                                               state.fs)
        elif (not is_iir) and is_mini_order:
            if state.windowType in [WindowTypeEnum.KAISER]:
                if is_single_band:
                    self.taps = self.fir_filter_kaiser_window_mini_order_helper(state.fe1, state.fe2,
                                                                                state.rs,
                                                                                response_type_map[state.responseType],
                                                                                state.scale,
                                                                                state.fs
                                                                                )
                else:
                    self.taps = self.fir_filter_kaiser_window_mini_order_band_helper(state.fe1, state.fe2, state.fe3,
                                                                                     state.fe4,
                                                                                     state.rs,
                                                                                     response_type_map[
                                                                                         state.responseType],
                                                                                     state.scale,
                                                                                     state.fs
                                                                                     )
            else:
                raise Exception("无效的窗类型,请重新选择!")

    # 带有通带波纹和阻带衰减的iir_filter
    @staticmethod
    def iir_filter_helper(order_n,
                          fc_hz,
                          rp_db, rs_db,
                          design_method,
                          response_type,
                          fs_hz):
        if type(fc_hz) == list:
            wn = [fc_hz[0], fc_hz[1]]
        else:
            wn = fc_hz

        if rp_db is not None or rs_db is not None:
            b, a = signal.iirfilter(order_n, wn, rp=rp_db, rs=rs_db,
                                    btype=response_type, analog=False,
                                    ftype=design_method, fs=fs_hz)
        else:
            b, a = signal.iirfilter(order_n, wn,
                                    btype=response_type, analog=False,
                                    ftype=design_method, fs=fs_hz)
        return b, a

    # 高通/低通 FIR 指定阶数 Window
    @staticmethod
    def fir_filter_window_helper(order,
                                 fc_hz,
                                 window_type,
                                 res_type,
                                 scale,
                                 fs_hz):
        try:
            h = signal.firwin(order + 1,
                              width=None,
                              cutoff=fc_hz * 2 / fs_hz,
                              window=window_type,
                              pass_zero=res_type,
                              scale=scale,
                              fs=2.0)
        except ValueError:
            pass
        else:
            pass
        return h

    # 带通/带阻 FIR 指定阶数 Window
    @staticmethod
    def fir_filter_window_helper_band(order,
                                      fc1_hz, fc2_hz,
                                      window_type,
                                      res_type,
                                      scale,
                                      fs_hz):
        try:
            h = signal.firwin(order + 1,
                              width=None,
                              cutoff=[fc1_hz * 2 / fs_hz, fc2_hz * 2 / fs_hz],
                              window=window_type,
                              pass_zero=res_type,
                              scale=scale,
                              fs=2.0)
        except ValueError:
            pass
        else:
            pass
        return h

    # 高通/低通 最小阶数 FIR kaiser window
    # @staticmethod
    def fir_filter_kaiser_window_mini_order_helper(self, fe1_hz, fe2_hz,
                                                   ripple_db,
                                                   res_type,
                                                   scale,
                                                   fs_hz):
        nyq_rate = fs_hz / 2.0
        dealt_w = fe2_hz - fe1_hz
        width = dealt_w / nyq_rate
        N, beta = signal.kaiserord(ripple_db, width)
        self.state.order = N - 1
        cutoff_hz = (fe1_hz + fe2_hz) / 2
        taps = signal.firwin(N,
                             cutoff_hz / nyq_rate,
                             window=('kaiser', beta),
                             pass_zero=res_type,
                             scale=scale)
        return taps

    #  带通/带阻 最小阶数 FIR kaiser window
    # @staticmethod
    def fir_filter_kaiser_window_mini_order_band_helper(self, fe1_hz, fe2_hz,
                                                        fe3_hz, fe4_hz,
                                                        ripple_db, res_type,
                                                        scale, fs_hz):
        # deltaw=min((wp1-ws1),(ws2-wp2)); %计算通带滤波器过渡带w
        nyq_rate = fs_hz / 2.0
        dealt_w = min((fe2_hz - fe1_hz), (fe4_hz - fe3_hz))
        width = dealt_w / nyq_rate
        N, beta = signal.kaiserord(ripple_db, width)
        self.state.order = N - 1
        cutoff1_hz = (fe1_hz + fe2_hz) / 2
        cutoff2_hz = (fe3_hz + fe4_hz) / 2

        taps = signal.firwin(N,
                             [cutoff1_hz / nyq_rate, cutoff2_hz / nyq_rate],
                             window=('kaiser', beta),
                             pass_zero=res_type,
                             scale=scale)
        return taps

    # 相位响应
    def show_phase_response(self, weight):
        weight.clear()
        if self.state.impulseResponseType == ImpulseResponseTypeEnum.IIR:
            w, h = signal.freqz(self.b, self.a)

        else:
            w, h = signal.freqz(self.taps)
        w = np.unwrap(w / np.pi)
        angles = np.unwrap(np.angle(h, True))
        weight.plot(w, angles, pen='r')
        weight.setLabel(axis="left", text="相位 / rad")
        weight.setLabel(axis="bottom", text="归一化频率 (pi*rad/sample)")

    # 幅值响应
    def show_amplitude_response(self, weight):
        weight.clear()
        if self.state.impulseResponseType == ImpulseResponseTypeEnum.IIR:
            w, h = signal.freqz(self.b, self.a)
        else:
            w, h = signal.freqz(self.taps)
        w = np.unwrap(w / np.pi)
        weight.plot(w, 20 * np.log10(abs(h)), pen='r')
        weight.setLabel(axis="left", text="幅值 / dB")
        weight.setLabel(axis="bottom", text="归一化频率 (pi*rad/sample)")

    # 获取当前滤波器 阶数
    def get_order_num(self):
        return self.state.order

    # 获取当前滤波器 类型
    def get_type_text(self):
        pass

    # 获取当前滤波器 稳定性
    def get_stability_text(self):
        return "是"
        pass

    # 获取是FIR 还是IIR
    def get_impulse_response_type(self):
        return impulse_response_type_map[self.state.impulseResponseType]

    # 获取当前滤波器设计方法
    def get_design_method_name(self):
        return design_method_name_map[self.state.designMethod]

    # 获取当前滤波器 优点
    def get_advantage_text(self):
        return impulse_response_features_map[
            ImpulseResponseTypeEnum.IIR if self.is_iir else ImpulseResponseTypeEnum.FIR][0]

    # 获取当前滤波器 缺点
    def get_disadvantage_text(self):
        return impulse_response_features_map[
            ImpulseResponseTypeEnum.IIR if self.is_iir else ImpulseResponseTypeEnum.FIR][1]

    def get_feature_text(self):
        return features_map[self.state.designMethod]
