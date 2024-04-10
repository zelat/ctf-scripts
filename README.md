# ctf-scripts

这是一个CTF常用脚本的集合

| Category        | Language | Scripts / Programs                                   | Purpose                                                                                                                                                             |
|-----------------|----------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TrafficAnalysis | Python   | [decode_modbus.py](TrafficAnalysis/decode_modbus.py) | 用于解析PCAP文件中MODBUS协议的数据包，来寻找特定标志（flag）的工具。                                                                                                                           |
| TrafficAnalysis | Python   | [len2hex.py](TrafficAnalysis/len2hex.py)             | 将数据包长度转为hex                                                                                                                                                         |
| TrafficAnalysis | Python   | [generate.py](TrafficAnalysis/generate.py)           | 从指定目录中读取所有文件，然后在这些文件的内容中寻找所有匹配方括号（[]）内部内容的正则表达式模式。找到的匹配项被合并成一个字符串（通过空格分隔每个匹配项），然后这个字符串会被添加到一个列表中。最后，这个列表中的每个元素（每个元素代表一个文件中所有匹配的内容）都会被写入到一个名为passwd.txt的文件中，每个元素占一行。 |
| Steganography   | Python   | [decode_image.py](LogAnalysis/decode_image.py)       | 将一个Base64编码的字符串，其中包含了一个PNG图片的编码信息，转换回原始的二进制图片数据并保存到一个文件中                                                                                                            |