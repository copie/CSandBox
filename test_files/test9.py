"""各种排序算法的综合测试"""


def pail_sort(my_list):

    max_num = max(my_list)
    min_num = min(my_list)

    Y_list = list()

    for i in range(min_num, max_num+1):
        zhao_list = [i, 0]
        Y_list.append(zhao_list)
    for m in my_list:
        for Y in Y_list:
            if Y[0] == m:
                Y[1] += 1

    result = list()

    for n in Y_list:
        for t in range(0, n[1]):
            result.append(n[0])

    return result


def main():

    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("简单桶排序之前的序列:", Y_list)
    print("简单桶排序之后的序列:", pail_sort(Y_list))


if __name__ == '__main__':
    main()


def bubble_sort(my_list):

    N = len(my_list)
    # 循环的次数
    circle_num = N-1

    while circle_num > 0:
        # 初始的游标值
        index_value = 0

        while index_value < circle_num:
            if my_list[index_value] < my_list[index_value+1]:
                pass
            else:
                my_list[index_value], my_list[index_value +1] = my_list[index_value + 1], my_list[index_value]

            # 游标右移一个单位
            index_value += 1

        circle_num -= 1

    print("冒泡排序之后的序列:", my_list)
    return my_list


def main():
    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("冒泡排序之前的序列:", Y_list)
    bubble_sort(Y_list)


if __name__ == '__main__':
    main()


def selection_sort(my_list):

    # N为列表元素的个数
    N = len(my_list)

    circle_num = 0

    # 需要进行N-1次循环
    while circle_num < N:

        # 每次循环开始的游标索引值 为 circle_num , 结束的索引值为N-1
        for m in range(circle_num, N):
            if my_list[circle_num] <= my_list[m]:
                pass
            else:
                my_list[circle_num], my_list[m] = my_list[m], my_list[circle_num]

        circle_num += 1

    print("选择排序之后的序列:", my_list)


def main():
    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("选择排序之前的序列:", Y_list)
    selection_sort(Y_list)
    pass


if __name__ == '__main__':
    main()


def insert_sort(my_list):
    N = len(my_list)
    finish_list = list()
    f_len = len(finish_list)
    finish_list.append(my_list[0])
    # circle_num为待插入的值的索引
    for circle_num in range(1, N):
        for pre in range(0, circle_num):

            # 如果新加入的值比已排序的值小,就把新值加入到 已排序值的前面
            if my_list[circle_num] < finish_list[pre]:
                finish_list.insert(pre, my_list[circle_num])
                break

            # 如果新加入的值比已排序的序列最大的值都大,那么
            elif my_list[circle_num] >= finish_list[-1]:
                finish_list.append(my_list[circle_num])

                break
            # 如果新加入的值 比已排序的某个值大但比 已排序后面的值小
            elif my_list[circle_num] >= finish_list[pre] and my_list[circle_num] < finish_list[pre+1]:
                finish_list.insert(pre+1, my_list[circle_num])
                break
            else:
                pass

    return finish_list


def main():
    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("插入排序之前的序列:", Y_list)
    insert_sort(Y_list)
    print("插入排序之后的序列:", insert_sort(Y_list))


if __name__ == '__main__':
    main()


def q_sort(my_list, left, right):

    # 设置左右指针
    left_point = left
    right_point = right
    stand_num = left
    if left > right:
        return

    while left_point != right_point:

        # 先移动右指针,如果遇到 比基准值更小 的值,就停下来

        while (my_list[right_point] >= my_list[stand_num]) and (left_point < right_point):
            right_point -= 1

        # 再移动左指针,如果遇到比基准值更大的值,就停下来

        while (my_list[left_point] < my_list[stand_num]) and (left_point < right_point):
            left_point += 1

        # 找到了双方可交换的点后, 开始交换

        my_list[left_point], my_list[right_point] = my_list[right_point], my_list[left_point]

        # 将基准点 与 指针相遇的点互换

        if left_point == right_point:
            my_list[stand_num], my_list[left_point] = my_list[left_point], my_list[stand_num]

        q_sort(my_list, left, left_point-1)
        q_sort(my_list, right_point+1, right)

    return (my_list)


def quick_sort(out_of_order):
    end = len(out_of_order) - 1
    start = 0
    q_sort(out_of_order, start, end)
    # print("排列完成的数组:",out_of_order)

    return out_of_order


def main():
    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("快速排序之前的序列:", Y_list)
    print("快速排序之后的序列:", quick_sort(Y_list))


if __name__ == '__main__':
    main()


# 负责 将列表拆分
def merge_sort(Y_list):

    if len(Y_list) <= 1:
        return Y_list

    # 先将未排序的列表进行分组
    num = len(Y_list) // 2

    left_list = merge_sort(Y_list[:num])
    right_list = merge_sort(Y_list[num:])

    # 将分组的列表交给merge函数, merge负责将列表合并
    return merge(left_list, right_list)


# 负责将列表合并
def merge(left, right):

    left_point = 0
    right_point = 0

    finish_list = list()

    while right_point < len(right) and left_point < len(left):

        if left[left_point] <= right[right_point]:
            finish_list.append(left[left_point])
            left_point += 1

        else:
            finish_list.append(right[right_point])
            right_point += 1

    finish_list += left[left_point:]
    finish_list += right[right_point:]

    return finish_list


def main():
    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("归并排序之前的序列:", Y_list)
    print("归并排序之后的序列:", merge_sort(Y_list))


if __name__ == '__main__':
    main()


def shell_sort(Y_list):

    gap = len(Y_list)

    while gap >= 0:

        tem_list = list()

        if gap == 0:
            return Y_list

        # 将要抽取的值和索引保存到一个 列表里

        for index, value in enumerate(Y_list):
            if index % gap == 0:
                zhao_list = [index, value]
                tem_list.append(zhao_list)

        tem_value_list = list()

        for i in tem_list:
            tem_value_list.append(i[1])
        tem_value_list = insert_sort(tem_value_list)

        for i, vv in enumerate(tem_value_list):

            tem_list[i][1] = vv

        # 排序好的值  替换 原位置的值
        for iv in tem_list:

            Y_list[iv[0]] = iv[1]

        gap = gap // 2

    return Y_list


def insert_sort(my_list):
    N = len(my_list)
    finish_list = list()
    f_len = len(finish_list)
    finish_list.append(my_list[0])
    # circle_num为待插入的值的索引
    for circle_num in range(1, N):
        for pre in range(0, circle_num):

            # 如果新加入的值比已排序的值小,就把新值加入到 已排序值的前面
            if my_list[circle_num] < finish_list[pre]:
                finish_list.insert(pre, my_list[circle_num])
                break

            # 如果新加入的值比已排序的序列最大的值都大,那么
            elif my_list[circle_num] >= finish_list[-1]:
                finish_list.append(my_list[circle_num])

                break
            # 如果新加入的值 比已排序的某个值大但比 已排序后面的值小
            elif my_list[circle_num] >= finish_list[pre] and my_list[circle_num] < finish_list[pre+1]:
                finish_list.insert(pre+1, my_list[circle_num])
                break
            else:
                pass

    return finish_list


def main():

    Y_list = [100, 54, 26, 63, 12, 22, 93, 17, 12, 77, 31, 44, 55, 20]
    print("希尔排序之前的序列:", Y_list)
    print("希尔排序之后的序列:", shell_sort(Y_list))


if __name__ == '__main__':
    main()


# 实现快排
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    # 递归调用
    return quicksort(less) + [base] + quicksort(greater)


def main():
    nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(quicksort(nums))

    def x(y): return y


if __name__ == '__main__':
    main()
