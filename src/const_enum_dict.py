from enum import IntEnum


# 响应类型枚举
class ResponseTypeEnum(IntEnum):
    LOW_PASS = 0
    HIGH_PASS = 1
    BAND_PASS = 2
    BAND_STOP = 3


# 响应类形列表
response_type_map = ['lowpass', 'highpass', 'bandpass', 'bandstop']


# 设计方法枚举
class DesignMethodEnum(IntEnum):
    BUTTER_WORTH = 0
    CHEBYSHEV_1 = 1
    CHEBYSHEV_2 = 2
    ELLIPTIC = 3
    WINDOW = 4


# 设计方法名称
design_method_name_map = ['巴特沃斯过滤器','切比雪夫过滤器',"反切比雪夫过滤器","椭圆过滤器","窗口法"]

# iir设计方法列表
iir_design_method_map = ['butter', 'cheby1', 'cheby2', 'ellip'
                         ]


# 阶数类型枚举
class OrderTypeEnum(IntEnum):
    SPECIFY_ORDER = 0
    MINI_ORDER = 1


# window类型枚举
class WindowTypeEnum(IntEnum):
    KAISER = 0
    RECTANGULAR = 1
    HANN = 2
    HAMMMING = 3
    BLACKMAN = 4


window_type_name_map = ['kaiser', 'boxcar', 'hann', 'hamming', 'blackman']


class ExactMatchEnum(IntEnum):
    STOP_BAND = 1
    PASS_BAND = 2
    ALL = 3


class ImpulseResponseTypeEnum(IntEnum):
    IIR = 0
    FIR = 1


impulse_response_type_map = ['IIR', 'FIR']

# 各种滤波器设计方法的优点缺点
impulse_response_features_map = {
    ImpulseResponseTypeEnum.IIR: ("其设计可以直接利用模拟滤波器设计的成果，因为模拟滤波器本身就是无限长脉冲响应的",
                                  "由于存在反馈其稳定性不能得到保证。另外，反馈还使IIR滤波器的数字运算可能溢出，即Z转换后极点有可能超出单位圆之外"),
    ImpulseResponseTypeEnum.FIR: (
        "他们可以完全有 线性相位,他们总是稳定的。设计方法通常是线性的。它们可以通过硬件有效地实现。滤波器启动瞬变具有有限的持续时间。",
        "相较于可以直接采样模拟滤波器设计的IIR滤波器来说设计较为不易,性能不如同样阶数的IIR滤波器")
}

features_map = {
    DesignMethodEnum.BUTTER_WORTH: "巴特沃斯滤波器的衰减速度比其他类型滤波器缓慢，但十分平坦，没有幅度变化",
    DesignMethodEnum.ELLIPTIC: "椭圆滤波器能够以较低的阶数获得较窄的过渡带宽，但是它在通带和阻带上都有波动",
    DesignMethodEnum.CHEBYSHEV_1: "切比雪夫滤波器在过渡带比巴特沃斯滤波器的衰减快，但频率响应的幅频特性不如后者平坦。切比雪夫滤波器和理想滤波器的频率响应曲线之间的误差最小，但是在通频带内存在幅度波动",
    DesignMethodEnum.CHEBYSHEV_2: "II型切比雪夫滤波器频率截止速度不如I型快,在通频带内没有幅度波动，只在阻频带内有幅度波动",
    # DesignMethodEnum.BESSEL: "贝塞尔滤波器几乎整个通频带都具有恒定的群延迟，因而在通频带上保持了被过滤的信号波形",
    DesignMethodEnum.WINDOW: "设计原理简单，有闭合公式可循；（2）是从时域出发的一种设计方法，需要求hd(n)，不直接；（3）不能准确控制通带及阻带的截止频率；"
}
