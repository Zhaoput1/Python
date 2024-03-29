# -*- coding: utf-8 -*-
"""
# @Time    : 5/14/21 

# @Author  : Zhaopu Teng
"""
import re


def myAtoi(s: str) -> int:
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())),2**31-1),-2**31)

    # re.findall('^[\+\-]?\d+', s.lstrip()) ^表示在行的开头匹配，保证以+-0-9开头；后续只能是连续数字。
    # re.findall() 没有匹配时返回[],否则返回全部符合该正则的子字符串；在这里因为输入只有一行，所以结果只能是空列表或者长度为1的列表
    # * 用来解包，也就是把列表展开。
    # int() 在输入为空的情况下，会返回0。（也就是说能够处理空列表展开的情况）
    # 唯一美中不足的，虽然Python int 没有范围限制，但还是要遵守题意的吧。比较最后结果是否越界可以通过将INT_MAX、INT_MIN转成字符串
    # 和匹配结果进行对比即可（先比长度，不能得出结果的话再按位比较）。