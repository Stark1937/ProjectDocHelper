import argparse
import os
from projectdochelper.generate import generate_docs
from projectdochelper.server import start_service

def parse_args():
    parser = argparse.ArgumentParser(description="ProjectDocHelper")
    parser.add_argument("--path", help="指定文档路径")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.path:
        if os.path.exists(args.path):
            start_service(args.path)
        else:
            print("错误：路径不存在")
    else:
        choice = input("请选择：1. 生成新文档  2. 输入文档路径\n输入选项 (1/2): ")
        if choice == "1":
            generate_docs()
            start_service("docs")
        elif choice == "2":
            path = input("请输入文档路径: ")
            if os.path.exists(path):
                start_service(path)
            else:
                print("错误：路径不存在")
        else:
            print("无效选项")

if __name__ == "__main__":
    main()