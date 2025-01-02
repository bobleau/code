#!/bin/bash

# 定义远程主机和文件路径
REMOTE_USER="user"
REMOTE_HOST="192.168.1.100"
FILE1="/home/user/docs/file1.txt"
FILE2="/home/user/images/image1.png"
LOCAL_DESTINATION="/home/localuser/backup/"

# 拷贝 file1.txt
scp "$REMOTE_USER@$REMOTE_HOST:$FILE1" "$LOCAL_DESTINATION"

# 检查 file1.txt 是否拷贝成功
if [ $? -eq 0 ]; then
    echo "file1.txt copied successfully. Skipping image1.png."
else
    echo "file1.txt copy failed. Attempting to copy image1.png."
    # 拷贝 image1.png
    scp "$REMOTE_USER@$REMOTE_HOST:$FILE2" "$LOCAL_DESTINATION"
fi
