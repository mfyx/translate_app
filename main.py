import sys
from interface import *
from gpt import *


def translate():
    source_text = ui.textEdit.toPlainText()
    source_lang = ui.comboBox.currentText()
    target_text = ""
    target_lang = ui.comboBox_2.currentText()

    """
    Translate the {source_lang} text
    that is delimited by triple backticks 
    into a language that is {target_lang}.
    text: ```{source_text}```
    """
    prompt = f"""
    请将“{source_lang}”语言的文本翻译成“{target_lang}”语言的文本，
    该文本被三个`符号分隔，
    除了翻译完成的文本外不要额外回复任何内容，包括`符号。
    源文本：```{source_text}```
    """
    print(prompt)

    target_text = get_completion(prompt)
    print(target_text)
    target_text = target_text.strip('`')
    ui.textEdit_2.setText(target_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(translate)

    sys.exit(app.exec_())