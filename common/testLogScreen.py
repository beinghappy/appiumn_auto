import os
import time
def screenshotNG(caseName, driver, resultPath):
    # resultPath = "d:\\appium"
    logPath = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # screenshotPath = os.path.join(logPath, caseName)
    if not os.path.exists(resultPath):
        os.makedirs(resultPath)
    screenshotName = "CheckPoint_NG.png"
    screen_img = resultPath + caseName + "_" + logPath + "_" + screenshotName
    # screen_img = os.path.join(screenshotPath, screenshotName)
    isOk = driver.get_screenshot_as_file(screen_img)
    print(u"Í¼Æ¬½ØÍ¼ÊÇ·ñ³É¹¦ ")
    print(isOk)
    return screen_img
