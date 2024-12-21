#!/bin/sh

# 群晖ping不通路由器，就自动关闭
# 应用场景：NAS接UPS，断电后路由器关机。NAS有UPS供电而继续运行。3分钟后，还ping不通，NAS就关机。

# 监控器的 IP 地址
MonitorIP=192.168.31.1

# 延迟时间
DelayTime=180s

# ping 监控器的 IP 地址
if ping $MonitorIP -W 2 -w 2 -c 2 | grep '^[0-9].*ms$' > /dev/null
then
  # ping 成功，打印消息
  echo "Power on."
else
  # ping 失败，发送警告消息
  synologset1 sys warn 0x11600036

  # 延迟一段时间
  sleep $DelayTime

  # 再次 ping 监控器的 IP 地址
  if ping $MonitorIP -W 2 -w 2 -c 2 | grep '[0-9].*ms$' > /dev/null
  then
    # ping 成功，发送警告消息
    synologset1 sys warn 0x11600035
  else
    # ping 失败，发送警告消息并关机
    synologset1 sys warn 0x11600037
    poweroff
  fi
fi

exit 0
