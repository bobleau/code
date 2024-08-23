#!/bin/bash

# 设置要扫描的硬盘设备
DEVICE="/dev/sdX"  # 替换为实际的设备名称，例如 /dev/sda

# 设置读取块的大小和次数
BLOCK_SIZE="1M"  # 可以根据需要调整块的大小
NUM_READS=10      # 读取次数

# 设置日志文件
LOGFILE="dd_read_log.txt"

# 清空日志文件内容（如果文件已存在）
> $LOGFILE

# 执行读取操作
for i in $(seq 1 $NUM_READS); do
    echo "第 $i 次读取: $(date)" | tee -a $LOGFILE
    dd if=$DEVICE of=/dev/null bs=$BLOCK_SIZE iflag=direct status=progress 2>&1 | tee -a $LOGFILE
    sleep 1  # 每次读取之间暂停1秒
done

echo "读取完成" | tee -a $LOGFILE
