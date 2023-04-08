#此代码由chatgpt生成，经测试功能正确！
#function：PDF转图片；修改为任意格式；用图像化界面完成
#非常快速
#虽然没有import PyMuPDF，但是不安装的话会报错
import os
import fitz
import tkinter as tk
from tkinter import filedialog, messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("PDF转图片")
        # 创建按钮和标签
        self.open_button = tk.Button(master, text="打开PDF文件", command=self.open_pdf)
        self.convert_button = tk.Button(master, text="PDF转图片", command=self.pdf_to_png)
        self.file_label = tk.Label(master, text="未选择文件")
        # 显示按钮和标签
        self.open_button.pack()
        self.convert_button.pack()
        self.file_label.pack()
        self.folder_path = None

    def open_pdf(self):
        # 打开文件对话框，选择要转换的PDF文件
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.file_label.config(text=file_path)
            self.folder_path = os.path.splitext(file_path)[0] + "_images"
            os.makedirs(self.folder_path, exist_ok=True)

    def pdf_to_png(self):
        # 获取选择的PDF文件路径
        pdf_file = self.file_label.cget("text")
        if not pdf_file.endswith(".pdf"):
            messagebox.showwarning("错误", "请选择PDF格式的文件!")
            return
        if not self.folder_path:
            messagebox.showwarning("错误", "请先选择要保存的文件夹!")
            return
        # 打开PDF文件，将每一页转成PNG格式的图片
        with fitz.open(pdf_file) as doc:
            for i in range(doc.page_count):
                page = doc.load_page(i)
                pix = page.get_pixmap()
                output_file = os.path.join(self.folder_path, f"page{i+1}.png")
                pix.save(output_file)
        messagebox.showinfo("完成", "PDF转图片成功！")

# 在主线程中启动Tkinter应用程序
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
