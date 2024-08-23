#!/bin/bash

# 设置要扫描的硬盘设备
DEVICE="/dev/sdX"  # 替换为实际的设备名称，例如 /dev/sda

# 设置日志文件路径
LOGFILE="usb_test.log"

# 输出带时间戳的函数
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $*" | tee -a $LOGFILE
}

# 设置最大写入次数（可选）
MAX_RUNS=100
COUNT=0

# 循环测试
while [ $COUNT -lt $MAX_RUNS ]; do
    log "开始第 $((COUNT+1)) 次写入..."
    pv --rate-limit 500k /dev/zero | sudo dd of=$DEVICE bs=4M status=progress 2>> $LOGFILE
    if [ $? -ne 0 ]; then
        log "写入出错！"
        break
    fi
    log "写入完成，开始验证数据..."
    
    # 读取数据并进行校验
    sudo dd if=$DEVICE bs=4M count=10 | cmp /dev/zero -
    if [ $? -ne 0 ]; then
        log "数据校验失败！"
        break
    fi
    
    log "数据校验成功，继续下一次写入..."
    COUNT=$((COUNT+1))
done
