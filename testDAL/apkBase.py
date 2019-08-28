__author__ = 'shikun'
import math
from math import  floor
import subprocess
import os
import platform

class ApkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath
        self.aaptPath = self.get_aapt_path()
        if (platform.system() == 'Windows'):
            self.cmd = " | findstr"
        else:
            self.cmd = " | grep"

    @staticmethod
    def get_aapt_path():
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt.exe" in files:
                    return os.path.join(path, "aapt.exe")
        else:
            return "ANDROID_HOME not exist"

    # 得到app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkpath)/(1024*1000))
        return str(size) + "M"
    # 得到版本
    def get_apk_version(self):
        cmd = self.aaptPath+" dump badging " + self.apkpath + self.cmd + " versionName"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[3].decode()[12:]
        return result

    #得到应用名字
    def get_apk_name(self):
        cmd = self.aaptPath+" dump badging " + self.apkpath + self.cmd + " application-label: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[0].decode()[18:]
        return result

    #得到包名
    def get_apk_pkg(self):
        cmd = self.aaptPath + " dump badging " + self.apkpath + self.cmd + " package: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result

    #得到启动类
    def get_apk_activity(self):
        cmd = self.aaptPath + " dump badging " + self.apkpath + self.cmd + "  launchable-activity: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result
if __name__ == '__main__':
    ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_pkg()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_version()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_name()
    ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()


