import os


# --------------------------------------------------
# 用os.getcwd()做为Mock
def foo_getcwd():
    # 返回 os.getcwd()
    print(os.getcwd())
    return os.getcwd()
