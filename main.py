import sys
from interface import *
from gpt import *
#from message_box import MessageBox


def translate():
    source_text = ui.textEdit.toPlainText()
    source_lang = ui.comboBox.currentText()
    target_text = ""
    target_lang = ui.comboBox_2.currentText()

    prompt = f"""Translate the {source_lang} text \
    that is delimited by triple backticks 
    into a language that is {target_lang}.
    text: ```{source_text}```
    """

    print(prompt)

    target_text = get_completion(prompt)
    print(target_text)

    ui.textEdit_2.setText(target_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(translate)

    sys.exit(app.exec_())