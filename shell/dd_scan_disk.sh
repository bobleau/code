#!/bin/bash

# 设置要扫描的硬盘设备
DEVICE="/dev/sdX"  # 替换为实际的设备名称，例如 /dev/sda

# 设置读取块的大小和次数
BLOCK_SIZE="1M"  # 可以根据需要调整块的大小
NUM_READS=10      # 读取次数

# 设置读取速度限制（例如 5MB/s）
SPEED_LIMIT="5M"

# 设置日志文件
LOGFILE="dd_read_log.txt"

# 设备检查
if [ ! -b "$DEVICE" ]; then
    echo "设备 $DEVICE 不存在" | tee -a $LOGFILE
    exit 1
fi

# 清空日志文件内容（如果文件已存在）
if [ ! -e "$LOGFILE" ]; then
    touch $LOGFILE
elif ! > $LOGFILE; then
    echo "无法清空日志文件 $LOGFILE" | tee -a $LOGFILE
    exit 2
fi

# 执行读取操作
for i in $(seq 1 $NUM_READS); do
    echo "第 $i 次读取: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a $LOGFILE
    START_TIME=$(date +%s)
    if ! dd if=$DEVICE bs=$BLOCK_SIZE iflag=direct | pv -L $SPEED_LIMIT | dd of=/dev/null bs=$BLOCK_SIZE iflag=direct status=progress 2>&1 | tee -a $LOGFILE; then
        echo "读取设备 $DEVICE 失败" | tee -a $LOGFILE
        exit 3
    fi
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    echo "第 $i 次读取耗时: $DURATION 秒" | tee -a $LOGFILE
    sleep 1  # 每次读取之间暂停1秒
done

echo "读取完成" | tee -a $LOGFILE
