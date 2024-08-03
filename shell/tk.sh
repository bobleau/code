#!/bin/bash
# 查找MD5还原TK

# 从远程服务器获取测试结果，并通过grep过滤，然后保存到本地的md5cut文件
ssh nrduser1@$2 "/opt/radar_software/unittest --gtest_filter=ModIOTest.GetVersion | grep tr_rf_" > md5cut

# 读取md5cut文件，并对每一行进行处理
cat -A md5cut | while read id;
do
    md5=`echo $id | cut -d"^" -f1`
    # 在key文件中查找md5值，并将结果添加到Radar_${1}_TR_SN.txt文件中
    grep $md5 key | cut -d" " -f1 | tee -a Radar_${1}_TR_SN.txt
done

