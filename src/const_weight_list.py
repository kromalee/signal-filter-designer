# 下拉选择控件
select_weight_list = [
    "responseType",
    "designMethod",
    "orderType",
    "windowType",
]
# 复选框控件
check_weight_list = ["scale"]

# 输入框控件
input_weight_list = [
    "order",
    "beta",
    "fs",  # 取样频率
    "fc1",  # 截至频率
    "fc2",
    "fe",  # 提示边缘频率输入的label
    "fe1",  # 边缘频率
    "fe2",
    "fe3",
    "fe4",
    "rp",  # 通带波纹
    "rs",  # 阻带衰减
]

# 所有的控件
all_weight = select_weight_list + check_weight_list + input_weight_list

# 总是有效的控件
all_ways_valid_fields = ["responseType", "designMethod", "orderType", "fs", ]
