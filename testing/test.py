import numpy as np

# 从列表创建一维数组
data_list = [1, 2, 3, 4, 5]
array_1d = np.array(data_list)
print(f"一维数组: {array_1d}")
# 从列表创建二维数组
data_list_2d = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(data_list_2d)
print(f"二维数组: \n{array_2d}")


array_arange = np.arange(10)
print(f"使用 arange 创建的数组: {array_arange}")


# 使用 zeros 创建全 0 的一维数组
array_zeros_1d = np.zeros(5)
print(f"全 0 的一维数组: {array_zeros_1d}")
# 使用 zeros 创建全 0 的二维数组
array_zeros_2d = np.zeros((3, 3))
print(f"全 0 的二维数组: \n{array_zeros_2d}")


# 使用 ones 创建全 1 的一维数组
array_ones_1d = np.ones(5)
print(f"全 1 的一维数组: {array_ones_1d}")
# 使用 ones 创建全 1 的二维数组
array_ones_2d = np.ones((3, 3))
print(f"全 1 的二维数组: \n{array_ones_2d}")


# 使用 linspace 创建从 0 到 1 的 5 个等间距的数组
array_linspace = np.linspace(0, 1, 5)
print(f"使用 linspace 创建的数组: {array_linspace}")


# 查看一维数组的形状
shape_1d = array_1d.shape
print(f"一维数组的形状: {shape_1d}")
# 查看二维数组的形状
shape_2d = array_2d.shape
print(f"二维数组的形状: {shape_2d}")