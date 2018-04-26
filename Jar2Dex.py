import os


def check_source_path(source_path):
    if os.path.exists(source_path) & os.path.isdir(source_path):
        return True
    else:
        print("输入的不是文件夹或者路径不存在,请重新输入!")
        return False


def check_target_path(target_path):
    if os.path.exists(target_path) & os.path.isdir(target_path):
        return True
    else:
        print("输出路径不是文件夹,请重新输入!")
        return False


def jar_to_dex(source_path, target_path):
    files = os.listdir(source_path)
    if len(files) == 0:
        print(source_path + "目录下无文件!")
    else:
        for file in files:
            file_path = source_path + '\\' + file
            if os.path.isfile(file_path) & file.endswith(".jar"):
                name = file.replace(".jar", "")
                print("name:" + name)
                dex_path = target_path + '\\' + name + '.dex'
                jar_path = source_path + '\\' + name + '.jar'
                commnad = 'dx --dex --output ' + dex_path + ' ' + jar_path
                print("commnad:" + commnad)
                os.system(commnad)
            else:
                print(file_path + "不是Jar文件!")


source_path = input("请输入jar包所在目录:\n")
while not check_source_path(source_path):
    source_path = input("请输入jar包所在目录:\n")
target_path = input("请输入dex包输出目录:\n")
while not check_target_path(target_path):
    targetPath = input("请输入dex包输出目录:\n")
jar_to_dex(source_path, target_path)
