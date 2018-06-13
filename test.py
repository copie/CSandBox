import os
import subprocess
path = os.getcwd()+"/test_files/"
test_files = os.listdir(path)
test_files = [path + file_ for file_ in test_files]
print("获取测试所用的文件成功")
for file_name in test_files:
    with open(file_name) as file_:
        line = file_.readline()
        print(line.strip())

    run_code = subprocess.run(
        ["python", 'csandbox.py', file_name],
        stdout=subprocess.PIPE,
        timeout=3
    )

    python = subprocess.run(["python", file_name],
                            stdout=subprocess.PIPE,
                            timeout=3
                            )

    if run_code.stdout == python.stdout:
        print("成功完成: "+file_name+" 的测试\n")
    else:
        print(file_name+" 测试失败")
        break
else:
    print("所有测试文件都测试完毕,没有问题")
