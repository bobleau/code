#!/bin/bash

# 服务器列表存储文件
SERVER_LIST="servers.txt"
REMOTE_PATH="/tmp/remote_script.sh"  # 远程服务器上存放脚本的路径

# 帮助信息
usage() {
    echo "Usage: $0 [-c \"command1; command2\"] [-s script.sh]"
    echo "  -c  远程执行单条或多条命令 (用分号分隔)"
    echo "  -s  远程上传并执行本地脚本"
    echo "  -h  显示帮助信息"
    exit 1
}

# 检查 sshpass 是否安装
if ! command -v sshpass &> /dev/null; then
    echo "sshpass 未安装，正在尝试安装..."
    sudo apt-get update && sudo apt-get install -y sshpass
fi

# 解析参数
COMMAND=""
SCRIPT=""
while getopts "c:s:h" opt; do
    case "$opt" in
        c) COMMAND="$OPTARG" ;;
        s) SCRIPT="$OPTARG" ;;
        h) usage ;;
        *) usage ;;
    esac
done

if [[ -z "$COMMAND" && -z "$SCRIPT" ]]; then
    echo "错误: 必须提供 -c 或 -s 选项"
    usage
fi

# 确保本地脚本存在（如果使用 -s 选项）
if [[ -n "$SCRIPT" && ! -f "$SCRIPT" ]]; then
    echo "错误: 本地脚本 $SCRIPT 不存在！"
    exit 1
fi

# 读取服务器列表并执行操作
while IFS=',' read -r REMOTE_USER REMOTE_HOST REMOTE_PASS; do
    if [[ -n "$COMMAND" ]]; then
        echo "正在远程执行命令: ${REMOTE_HOST}"
        sshpass -p "${REMOTE_PASS}" ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} "$COMMAND"
        echo "服务器 ${REMOTE_HOST} 命令执行完成"
    fi

    if [[ -n "$SCRIPT" ]]; then
        echo "正在上传脚本到服务器: ${REMOTE_HOST}"
        sshpass -p "${REMOTE_PASS}" scp -o StrictHostKeyChecking=no "$SCRIPT" ${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}

        echo "正在远程执行脚本: ${REMOTE_HOST}"
        sshpass -p "${REMOTE_PASS}" ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} "chmod +x ${REMOTE_PATH} && sudo ${REMOTE_PATH}"

        echo "服务器 ${REMOTE_HOST} 脚本执行完成"
    fi
done < ${SERVER_LIST}

echo "所有服务器任务执行完成"