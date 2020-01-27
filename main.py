import sys
from Window_login import *

# 主函数
def main():
    app = QApplication(sys.argv)
    l = Window_login()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()