# 用于解析PCAP文件（Packet Capture Data File，一种网络数据包捕获文件）来寻找特定标志（flag）的工具。它特别关注Modbus协议的数据包，这是一个在工业环境中常用的应用层协议
import pyshark

def find_flag():
    cap = pyshark.FileCapture("./files/Modbus.pcap")  # 使用pyshark打开位于相对路径的Modbus.pcap文件进行分析。
    idx = 1  # 初始化一个计数器，用于追踪当前处理的数据包序号。
    for c in cap:  # 遍历PCAP文件中的所有捕获到的数据包。
        for pkt in c:  # 遍历单个数据包中的所有层。
            if pkt.layer_name == "modbus":  # 检查当前层是否为Modbus协议层。
                func_code = int(pkt.func_code)  # 获取Modbus功能码。
                if func_code == 16:  # 判断功能码是否为16，16通常代表写多个寄存器的功能。
                    payload = str(c["TCP"].payload).replace(":", "")  # 提取TCP层的负载数据，并移除所有冒号。
                    print(hex_to_ascii(payload))  # 将负载中的十六进制数据转换为ASCII字符串，并打印出来。
                    print("{0} *".format(idx))  # 打印当前数据包的序号，后面跟一个星号标记。
        idx += 1  # 数据包序号自增。

def hex_to_ascii(payload):
    data = payload  # 将输入的负载赋值给data变量。
    flags = []  # 初始化一个空列表，用于存储转换后的ASCII字符。
    for d in data:  # 遍历负载中的每个字符。
        _ord = ord(d)  # 获取字符的ASCII数值。
        if (_ord > 0) and (_ord < 128):  # 如果ASCII数值在有效范围内（可打印字符）。
            flags.append(chr(_ord))  # 将数值转换为对应的ASCII字符，并添加到列表中。
    return ''.join(flags)  # 将列表中的所有ASCII字符连接成字符串并返回。

if __name__ == '__main__':
    find_flag()
