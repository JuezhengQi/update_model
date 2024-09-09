import os
import sys
import socket, getpass
import time
import paramiko
from PyQt5 import QtWidgets
from upload_platform_v1 import Ui_Form
import net_convert


class uploadPlatform(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(uploadPlatform, self).__init__()

        # 通过 QTDesigner 设计的界面
        self.setupUi(self)

        # 获取当前程序文件位置
        self.cwd = os.getcwd()

        # 设置 ssh 远程连接
        self.ssh_connect = paramiko.SSHClient()
        self.ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        # 判断 远程服务器 有无 update_description.txt
        # if exist: 将 update_description.txt 从远程服务器下载到本地指定文件夹
        # 尝试从 远程服务器 下载 update_description.txt
        # self.download_from_remote(self.target_folder.text(), self.cwd)

        # if not exist：本地新建 update_description.txt; 或者, 将文件 update_description.txt 清空
        # with open('./update_description.txt', 'a+', encoding='utf-8') as f:
        #     f.truncate(0)

        # 初始化 上传的文件 为 None
        self.fileName_choose = None
        self.filetype = None

        # 根据需求个性化调整
        self.setWindowTitle("upload_model_file")

        # 远程 ssh 连接 控件设置
        # 设置 提示 内容 username & password
        self.ssh_username.setPlaceholderText("username@host_ip")
        self.ssh_password.setPlaceholderText("password")
        # 绑定 “连接” 按钮 至键盘回车键
        self.ssh_password.returnPressed.connect(self.slot_btn_ssh_connect)

        # 设置 ssh_connect_btn
        self.ssh_connect_btn.clicked.connect(self.slot_btn_ssh_connect)
        self.ssh_username.textChanged.connect(self.slot_ssh_connect_btn_changed)
        self.ssh_password.textChanged.connect(self.slot_ssh_connect_btn_changed)
        self.ssh_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # "清空" 按钮 信号
        self.clear_inhalt.clicked.connect(self.slot_btn_clear_inhalt)

        # "保存" 按钮 信号
        self.save_inhalt.clicked.connect(self.slot_btn_save_inhalt)
        # 实时跟踪 QTextEdit 内容是否有变化， 如若有变化，设置 "保存" 按钮 的状态 为 可点击
        self.inhalt.textChanged.connect(self.slot_inhalt_changed)

        # “选择文件”  按钮 信号
        self.file_select.clicked.connect(self.slot_btn_file_select)

        # 设置 include_onnx_file 默认值为 选中
        self.include_onnx_file.setChecked(True)

        # "上传文件" 按钮 处理
        self.file_upload_btn.setEnabled(False)  # 默认上传文件按钮不可点击，除非 ssh 连接成功
        self.file_upload_btn.clicked.connect(self.slot_btn_file_upload)
        # self.target_folder.returnPressed.connect(self.slot_btn_file_upload)

        # target_folder 提示信息设置
        self.target_folder.setPlaceholderText("输入文件上传位置...")

    # 通过 paramiko 从 远程服务器 下载 update_description.txt 文件
    def download_from_remote(self, remote_file_path, local_file_path):
        t = paramiko.Transport((self.ssh_username.text().split('@')[1]))
        t.connect(username=self.ssh_username.text().split('@')[0], password=self.ssh_password.text())
        stfp = paramiko.SFTPClient.from_transport(t)
        stfp.get(remote_file_path, local_file_path)
        t.close()

    # 重写 关闭窗口 事件, 以关闭 ssh 连接
    def closeEvent(self, event):
        # reply = QtWidgets.QMessageBox.question(self, "上传模型平台", "是否退出该程序？",
        #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #                                        QtWidgets.QMessageBox.No)

        event.accept()
        self.close()
        # 确认窗口关闭后，关闭 ssh 连接
        self.ssh_connect.close()

    def slot_btn_file_select(self):
        self.fileName_choose, self.filetype = QtWidgets.QFileDialog.getOpenFileNames(self,
                                                                          "选择要上传的文件",
                                                                          self.cwd,
                                                                          "All Files (*);; "
                                                                          "Text Files (*.txt);; "
                                                                          "PT Files (*.pt);;"
                                                                          "ONNX File (*.onnx)")

        if not self.fileName_choose:
            print("\n取消选择")
            return

        # 尝试从 远程服务器 下载 update_description.txt 文件
        file_in_server_location = self.target_folder.text()
        try:
            self.download_from_remote(os.path.join(file_in_server_location, 'update_description.txt'), os.path.join(self.cwd, 'update_description.txt'))
        except Exception as e:
            print(e)
            with open('./update_description.txt', 'a+', encoding='utf-8') as f:
                f.truncate(0)

        # 选择了 onnx 文件，指定选中onnx便以为tvm的tar包解压后的文件
        # 选择模型文件， 直接编译， 解压，选中文件，一步到位， 上传部分，留到 upload 函数处理
        # 编译
        if self.include_onnx_file.isChecked():
            onnx_file = [file for file in self.fileName_choose if file.endswith('.onnx')]
            try:
                net_convert.compile_onnx_to_tvm(onnx_file[0])
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "编译文件出错啦！！！", str(e))
                return
            os.mkdir('./oghr_controller')
            os.system(f'tar -xvf ./oghr_controller.tar -C ./oghr_controller')
            model_files = os.listdir('./oghr_controller')
            for file in model_files:
                self.fileName_choose.append(os.path.join(self.cwd, 'oghr_controller', file))

        print("!!!!!!!!!!", self.fileName_choose)

        # 选择的文件中不包括 onnx 文件
        # 被选中的文件信息：包括 name, size, ctime, mtime
        file_info_dic = self.get_file_info(self.fileName_choose)

        # 将被选中的文件的基本信息填入 update_description.txt 文件中
        with open('./update_description.txt', 'a+', encoding='utf-8') as f:
            f.write(f"{'=' * 30}{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}{'=' * 30}\n\n")
            for file_info in file_info_dic:
                for key, value in file_info.items():
                    f.write(f"{key}: {value}\n")
                f.write("\n")

        # 点击选择文件后，才能点击上传按钮
        self.file_upload_btn.setEnabled(True)
        # print("\n你选择的文件是： ")
        # print(self.fileName_choose)
        # print("文件筛选器类型： ", self.filetype)

    def slot_btn_file_upload(self):
        print("上传文件 槽函数")
        print("self.fileName_choose:", self.fileName_choose)
        if self.fileName_choose:
            print(f"要上传的文件为： {self.fileName_choose}")
            # 测试位置
            # target_folder = "/home/enpht/test_upload_model_file/"  # 将文件传到的位置
            # 正式位置
            target_folder = self.target_folder.text()
            sftp = self.ssh_connect.open_sftp()

            # 通过 ssh 传输文件
            for file in self.fileName_choose:
                # file_to_upload_target = os.path.join(target_folder, os.path.basename(file))  # windows 的路径分隔符为 \ , ubuntu 的路径分隔符为 /
                file_to_upload_target = os.path.join(target_folder, os.path.basename(file))
                try:
                    sftp.put(file, file_to_upload_target)
                except Exception as e:
                    print(e)
                    QtWidgets.QMessageBox.critical(self, "上传文件出错啦！！！", str(e))

            # 点击上传后，除了上传模型文件外，还要上传 update_description.txt 文件
            sftp.put(os.path.join(self.cwd, 'update_description.txt'), os.path.join(target_folder, 'update_description.txt'))

            sftp.close()

        # 上传文件完毕后，删除解压出来的文件夹
        os.system('rm -rf ./oghr_controller')
        # 点击上传后，不可再次点击
        self.file_upload_btn.setEnabled(False)

    def slot_btn_clear_inhalt(self):
        self.inhalt.clear()

    def slot_btn_save_inhalt(self):
        with open('./update_description.txt', 'a+', encoding='utf-8') as f:
            f.write(f"{self.inhalt.toPlainText()}\n\n")
            f.write(f"{'=' * 30}Submit by: {socket.gethostname()}{'=' * 30}\n\n")
        print(self.inhalt.toPlainText())

        # 点击 “保存” 按钮后， 再次将该按钮状态设置为 不可点击
        self.save_inhalt.setEnabled(False)

    def slot_inhalt_changed(self):
        self.save_inhalt.setEnabled(True)

    def slot_btn_ssh_connect(self):
        ssh_username = self.ssh_username.text().split("@")
        ssh_password = self.ssh_password.text()
        try:
            self.ssh_connect.connect(hostname=ssh_username[1], username=ssh_username[0], password=ssh_password, timeout=3)
            self.ssh_connect_btn.setEnabled(False)
            self.ssh_connect_btn.setStyleSheet("background-color: green")
            self.file_upload_btn.setEnabled(True)  # ssh 连接成功才能点击上传文件按钮
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(self, "ssh连接出错啦！！！", str(e))
            self.file_upload_btn.setEnabled(False)  # ssh 连接失败，则不能点击上传文件按钮
            self.ssh_connect_btn.setStyleSheet("background-color: red")

    def slot_ssh_connect_btn_changed(self):
        self.ssh_connect_btn.setEnabled(True)

    # 获取文件基本信息
    def get_file_info(self, file_path_list: list) -> list:
        file_info = []
        for file_path in file_path_list:
            temp_dic = {
                            "file_name": os.path.basename(file_path),
                            "file_size": f"{round(os.path.getsize(file_path) / 1024, 2)} KB",
                            "create_time": f"{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(file_path).st_ctime))}",
                            "modify_time": f"{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(file_path).st_mtime))}"
                        }
            file_info.append(temp_dic)
        return file_info


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    uploadplatform = uploadPlatform()
    uploadplatform.show()
    sys.exit(app.exec_())