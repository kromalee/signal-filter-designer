from PyQt5 \
    import QtWidgets, \
    QtCore
from PyQt5.QtWidgets \
    import QMessageBox

from src.main_window_ui_rc \
    import Ui_mainWindow
from src.const_enum_dict \
    import ResponseTypeEnum, \
    DesignMethodEnum, \
    OrderTypeEnum, \
    WindowTypeEnum, \
    window_type_name_map
from src.const_weight_list \
    import all_weight, \
    select_weight_list, \
    check_weight_list, \
    input_weight_list, \
    all_ways_valid_fields
from src.class_signal_filter \
    import SignalFilter
from src.class_form_state \
    import FormState
from src.test_dialog_controller \
    import TestDialog

import copy
import functools


def showErrorDialog(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setText("错误")
    msg.setInformativeText(message)
    msg.setWindowTitle("错误")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):  # 这俩是父类,一个Qt的控件, 还有一个是 我们设计的UI
    def __init__(self):  # self 自己,代指MainWindow
        # 视图View

        # 执行父类的构造函数,创建💐那些控件
        super(MainWindow, self).__init__()
        # qt的接口.启动ui
        self.setupUi(self)

        # 设置主窗口固定宽高
        MainWindow.setFixedSize(self, 1366, 768)

        # 表单状态 Model 实例化一个表单状态,用来记录表单状态
        self.form_state = FormState()

        # 创建一个信号过滤器,因为还没点  "设计" ,所以先用None占个位置
        self.signal_filter = None
        # doDesign是哪个"设计"按钮的名字,   self.doDesign.clicked 当这个按钮被点击的时候,执行 self.do_design
        # connect是qt的api, 把按钮的点击事件和他的处理方法连接出来
        self.doDesign.clicked.connect(self.do_design)
        # doTest类似
        self.doTest.clicked.connect(self.do_test)
        # 至此所有的功能都创建完成了

        # 表单初始化
        # 绑定控件变化回调
        self.bind_ui_to_state()
        # 读取表单的默认状态
        self.read_state_from_ui()
        # 默认状态并对UI产生影响
        self.state_effect_to_ui()

    def read_state_from_ui(self):
        # 从下拉列表读取每个下拉的状态
        for every_weight_state_name in select_weight_list:
            self.on_select_change(every_weight_state_name, None)
        # 从checkbox读取每个状态
        for every_weight_state_name in check_weight_list:
            self.on_checkbox_change(every_weight_state_name, None)
        # 从数字输入框读取每个状态
        for every_weight_state_name in input_weight_list:
            self.on_input_change(every_weight_state_name, None)

    def bind_ui_to_state(self):
        # 下拉变化时更新值到state
        # 循环控件名称列表
        """
        # 下拉选择控件
            select_weight_list = [
                "responseType",
                "designMethod",
                "orderType",
                "windowType",
            ]
        """

        for every_weight_state_name in select_weight_list:
            # 检查有没有对应的输入框控件
            if hasattr(self, every_weight_state_name + 'Input'):
                # 有则给这个输入框绑定一个 变化时的处理函数
                getattr(self, every_weight_state_name + 'Input').currentIndexChanged.connect(
                    functools.partial(self.on_select_change, every_weight_state_name, self.state_effect_to_ui))
        # checkbox变化时更新值到state
        for every_weight_state_name in check_weight_list:
            if hasattr(self, every_weight_state_name + 'Input'):
                getattr(self, every_weight_state_name + 'Input').toggled.connect(
                    functools.partial(self.on_checkbox_change, every_weight_state_name, self.state_effect_to_ui))
        # 输入框变化时更新值到state
        for every_weight_state_name in input_weight_list:
            if hasattr(self, every_weight_state_name + 'Input'):
                getattr(self, every_weight_state_name + 'Input').valueChanged.connect(
                    functools.partial(self.on_input_change, every_weight_state_name, self.state_effect_to_ui))

    # 无effect时,仅执行更新状态操作
    # 有effect时,额外执行effect
    def on_select_change(self, every_weight_state_name, effect):
        # 检查有没有对应的输入框控件
        if hasattr(self, every_weight_state_name + 'Input'):
            #
            setattr(self.form_state, every_weight_state_name,
                    getattr(self, every_weight_state_name + "Input").currentIndex())
        if effect:
            effect()

    def on_checkbox_change(self, every_weight_state_name, effect):
        if hasattr(self, every_weight_state_name + 'Input'):
            setattr(self.form_state, every_weight_state_name,
                    getattr(self, every_weight_state_name + "Input").isChecked())
        if effect:
            effect()

    def on_input_change(self, every_weight_state_name, effect):
        if hasattr(self, every_weight_state_name + 'Input'):
            setattr(self.form_state, every_weight_state_name, getattr(self, every_weight_state_name + "Input").value())
        if effect:
            effect()

    # 当前状态对ui产生影响
    def state_effect_to_ui(self):
        valid, invalid = self.gen_field_with_effectiveness()

        # 批量显示/隐藏字段
        self.batch_hide_weight(invalid)
        self.batch_show_weight(valid)
        # 其他联动效果
        # designMethod 修改时修改响应类型
        if self.form_state.designMethod in [DesignMethodEnum.WINDOW]:
            self.impulseResponseTypeLabel.setText('FIR')

            # 限制窗类型的选择
            if self.form_state.orderType in [OrderTypeEnum.MINI_ORDER]:
                self.disable_item_comboBox(self.windowTypeInput,
                                           [WindowTypeEnum.HANN, WindowTypeEnum.RECTANGULAR, WindowTypeEnum.HAMMMING,
                                            WindowTypeEnum.BLACKMAN])
                # self.windowTypeInput.showPopup()
            else:
                self.disable_item_comboBox(self.windowTypeInput,
                                           [WindowTypeEnum.HANN, WindowTypeEnum.RECTANGULAR, WindowTypeEnum.HAMMMING,
                                            WindowTypeEnum.BLACKMAN], 1 | 32)
        else:
            self.impulseResponseTypeLabel.setText('IIR')

    @staticmethod
    def disable_item_comboBox(combo_box, target_list, v=0):
        """
        将下拉按钮中的某些项目批量禁用
        :param cBox: comboBox对象
        :param List: 需要禁用的项目,列表数据,如[1,2,5,6]
        :param v: 0为禁用,1|32为解除
        """
        for i in range(len(target_list)):
            index = combo_box.model().index(target_list[i], 0)  # 选择需要设定的项目
            combo_box.model().setData(index, v, QtCore.Qt.UserRole - 1)  # 禁用comboBox的指定项目

    # 批量隐藏控件
    def batch_hide_weight(self, target_list):
        for item in target_list:
            if hasattr(self, item + 'Input'):
                getattr(self, item + "Input").hide()
            if hasattr(self, item + 'Label'):
                getattr(self, item + "Label").hide()

    # 批量显示控件
    def batch_show_weight(self, target_list):
        for item in target_list:
            if hasattr(self, item + 'Input'):
                getattr(self, item + "Input").show()
            if hasattr(self, item + 'Label'):
                getattr(self, item + "Label").show()

    # 生成有效字段和无效字段
    def gen_field_with_effectiveness(self):
        # 条件合并

        # 是否单边的响应类型
        is_single_band = self.form_state.responseType in [ResponseTypeEnum.LOW_PASS, ResponseTypeEnum.HIGH_PASS]
        # 是否最小阶数
        is_mini_order = self.form_state.orderType in [OrderTypeEnum.MINI_ORDER]

        # 有效字段初始化:一直有效的字段
        valid_fields = copy.deepcopy(all_ways_valid_fields)

        # 分支判断添加所需字段
        if is_single_band and (not is_mini_order):
            valid_fields += ["fc1", "order"]
        elif is_single_band and is_mini_order:
            valid_fields += ["fe1", "fe2", "rp", "rs", 'fe']
        elif (not is_single_band) and (not is_mini_order):
            valid_fields += ["fc1", "fc2", "order"]
        else:
            valid_fields += ["fe1", "fe2", "fe3", "fe4", "rp", "rs", 'fe']

        # 当CHEBYSHEV_1,CHEBYSHEV_2,ELLIPTIC 增加 通带波纹和阻带衰减
        if self.form_state.designMethod in [DesignMethodEnum.CHEBYSHEV_1, DesignMethodEnum.CHEBYSHEV_2,
                                            DesignMethodEnum.ELLIPTIC]:
            valid_fields += ['rs', 'rp']

        # 设计类型是window时,显示window类型 和缩放
        if self.form_state.designMethod in [DesignMethodEnum.WINDOW]:
            valid_fields += ['windowType', 'scale']

        # 设计类型是window时, window类型是 KAISER,并且是最小阶数,增加通带波纹和阻带衰减
        if (self.form_state.designMethod in [DesignMethodEnum.WINDOW]) and (
                self.form_state.windowType in [WindowTypeEnum.KAISER]) and is_mini_order:
            valid_fields += ['rs', 'rp']

        # 设计类型是window时, window类型是 KAISER,并且不是最小阶数,增加 beta
        if (self.form_state.designMethod in [DesignMethodEnum.WINDOW]) and (
                self.form_state.windowType in [WindowTypeEnum.KAISER]) and (not is_mini_order):
            valid_fields += ['beta']

        # 根据有效字段和所有字段,算出无效字段
        return valid_fields, [x for x in all_weight if x not in valid_fields]

    # 获取参数
    def get_value_from_state(self):
        return copy.deepcopy(self.form_state)

    # 生成滤波器,画特性图
    def do_design(self):
        # try:
        #     self.signal_filter = SignalFilter(self.get_value_from_state())
        try:
            self.signal_filter = SignalFilter(self.get_value_from_state())
        #   收集所有异常,弹窗
        except Exception as err:
            print(err)
            showErrorDialog(str(err))
            return
        else:
            pass

        # 修改滤波器信息部分内容
        self.nameLabel.setText(
            str(self.signal_filter.get_design_method_name())
            + "-"
            + str(
                self.signal_filter.get_impulse_response_type())
        )
        self.orderResultLabel.setText(str(self.signal_filter.get_order_num()))
        self.goodLabel.setText(str(self.signal_filter.get_advantage_text()))
        self.badLabel.setText(str(self.signal_filter.get_disadvantage_text()))
        self.featureLabel.setText(str(self.signal_filter.get_feature_text()))
        # 向对应画布上绘制 相位响应
        self.signal_filter.show_phase_response(self.phaseResponse)
        # 向对应画布上绘制 幅值响应
        self.signal_filter.show_amplitude_response(self.amplitudeResponse)

    # 打开测试窗口
    def do_test(self):
        test_dialog = TestDialog(self.signal_filter)

        test_dialog.show()
        test_dialog.exec_()  # Dialog 的运行
