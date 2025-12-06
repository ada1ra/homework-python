numbers = [1, 2, 3, 9, 3, 8, 478, 7]


def bubble_sort(nums):
    # значение для запуска цикла
    swap = True

    while swap:
        swap = False
        for i in range(len(nums) - 1):
            # проверяем, больше ли текущий элемент следующего
            if nums[i] > nums[i + 1]:
                # меняем элементы местами
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # перезапускаем цикл, для ещё одной проверки
                swap = True


bubble_sort(numbers)
print(numbers)
