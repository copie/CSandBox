"""for 的测试文件"""

for x in [1, 2, 3, 4, 5, 6, 6, 7, 5]:
    print(x)

for x in [1, 2, 3, 4, 5, 6, 6, 7, 5]:
    print(x)
else:
    print("正常结束")


for x in [1, 2, 3, 4, 5, 6, 7]:
    if x == 4:
        print("continue")
        continue
    if x == 5:
        break
    print(x)
else:
    print("正常结束")


def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
