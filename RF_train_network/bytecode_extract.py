# -*- coding: utf-8 -*-
from infrastructure.ware import Ware
from infrastructure.fileutils import DataFile
import os

def collect(rootdir, isMalware):
    wares = os.listdir(rootdir)
    total = len(wares)
    for i, ware in enumerate(wares):
        warePath = os.path.join(rootdir, ware)
        ware = Ware(warePath, isMalware)
        print("文件名", ware.name)
        ware.extractFeature(f)
        print("已提取", i + 1, "个文件的特征")
        print("百分比为：",(i + 1) * 100 / total, "%")
        
# 1代表良性软件　　0代表恶意软件   2代表测试软件

kindroot = "./smalis/kind"
virusroot = "./smalis/malware"
testwroot = "./smalis/test/white"
testbroot = "./smalis/test/black"

f = DataFile("./data.csv")


collect(kindroot, 1)
collect(virusroot, 0)
collect(testwroot, 2)
collect(testbroot, 2)

f.close()
        




