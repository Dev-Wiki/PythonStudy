# 从源仓库Fork某个单独的分支到新的仓库

import os

gitDir = input("请输入本地工作目录:\n")
if not os.path.exists(gitDir):
    print()
if os.path.isdir(gitDir):
    if len(os.listdir(gitDir)) == 0:
        os.chdir(gitDir)
        os.system('git init')
        sourceOrigin = input("请输入源仓库地址:\n")
        os.system('git remote add origin ' + sourceOrigin)
        sourceBranch = input("请输入源分支:\n")
        os.system('git fetch origin ' + sourceBranch)
        targetBranch = input("请输入目标分支:\n")
        os.system('git checkout -b ' + targetBranch + ' origin/' + sourceBranch)
        targetOrigin = input("请输入目标仓库地址:\n")
        os.system('git remote remove origin')
        os.system('git remote add origin ' + targetOrigin)
        os.system('git push --set-upstream origin master')
    else:
        print("工作目录为非空目录!!!")
else:
    print("输入的不是文件夹!!!")
