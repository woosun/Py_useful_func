# 스크린샷
def screenshot():
    import pyautogui
    filenames =os.path.basename(__file__)
    filenames =filenames.split('.')
    scr_dir = './screenshots'
    if not os.path.exists(scr_dir):
        os.mkdir(scr_dir)
    nows = datetime.datetime.now()
    filenames1= nows.strftime("%Y.%m.%d_%H_%M_%S")
    pyautogui.screenshot(scr_dir+'/scr_'+filenames[0]+filenames1+".png")
