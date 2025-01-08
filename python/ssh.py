import paramiko

# 服务器的IP地址
hostname = 'qa01'

# 用户名和密码的组合
credentials = [
    ('user1', 'pass1'),
    ('nrduser1', '123456'),
    ('user3', 'pass3'),
]

# 创建SSH客户端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 遍历用户名和密码组合
for username, password in credentials:
    try:
        # 尝试连接到服务器
        client.connect(hostname, username=username, password=password)
        print(f'Successfully connected with username: {username} and password: {password}')
        
        # 执行命令
        command = 'ls -l'  # 你想要执行的命令
        stdin, stdout, stderr = client.exec_command(command)

        # 获取命令输出
        output = stdout.read().decode()
        error = stderr.read().decode()

        # 打印输出
        if output:
            print("Output:")
            print(output)
        if error:
            print("Error:")
            print(error)

        # 连接成功后可以选择退出循环
        break

    except paramiko.AuthenticationException:
        print(f'Failed to connect with username: {username} and password: {password}')
    except Exception as e:
        print(f'Error occurred: {e}')
    
    finally:
    # 关闭SSH连接
        client.close()