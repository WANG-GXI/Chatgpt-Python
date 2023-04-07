#此代码有chatgpt生成，经测试功能正确！
#function：修改为任意分辨率；修改为任意格式；用图像化界面完成
#非常快速
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class App():
    def __init__(self, master):
        self.master = master
        master.title("图片转换工具")

        # 创建选择文件夹按钮
        self.select_folder_button = tk.Button(master, text="选择文件夹", command=self.select_folder)
        self.select_folder_button.pack()

        # 创建选择保存路径按钮
        self.select_path_button = tk.Button(master, text="选择保存路径", command=self.select_path)
        self.select_path_button.pack()

        # 创建转换按钮
        self.convert_button = tk.Button(master, text="转换", command=self.convert)
        self.convert_button.pack()

        # 文件夹路径
        self.folder_path = ''

        # 保存路径
        self.save_path = ''

    def select_folder(self):
        # 弹出选择文件夹对话框
        self.folder_path = filedialog.askdirectory()

    def select_path(self):
        # 弹出选择保存路径对话框
        self.save_path = filedialog.askdirectory()

    def convert(self):
        # 遍历文件夹下的所有图片文件
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                    ".png") or filename.endswith(".gif"):
                # 转换为bmp格式
                img = Image.open(os.path.join(self.folder_path, filename))
                img = img.resize((640, 480))
                img.save(os.path.join(self.save_path, filename.split(".")[0] + ".bmp"))

        # 转换完成后弹出提示信息
        messagebox.showinfo("提示", "转换完成！")


# 创建GUI界面
root = tk.Tk()
app = App(root)
root.mainloop()