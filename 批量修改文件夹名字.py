import os

# 文件夹路径
folder_path = 'D:\\论文\格式'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 如果文件名不是Word文档，则跳过
    if not filename.endswith('.docx'):
        continue

    # 生成新的文件名 把XXX换位AAA XXX换为BBB
    new_filename = filename.replace('XXX', 'AAA')
    new_filename = new_filename.replace('XXX', 'BBB')

    # 生成文件的完整路径
    old_filepath = os.path.join(folder_path, filename)
    new_filepath = os.path.join(folder_path, new_filename)

    # 重命名文件
    os.rename(old_filepath, new_filepath)
