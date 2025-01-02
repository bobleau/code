@echo off

set REMOTE_USER=user
set REMOTE_HOST=192.168.1.100
set PASSWORD=your_password
set FILE1=/home/user/docs/file1.txt
set FILE2=/home/user/images/image1.png
set LOCAL_DESTINATION=C:\local\backup\

:: 拷贝 file1.txt
pscp -pw %PASSWORD% %REMOTE_USER%@%REMOTE_HOST%:%FILE1% %LOCAL_DESTINATION%

:: 检查 file1.txt 是否拷贝成功
if %errorlevel%==0 (
    echo file1.txt copied successfully. Skipping image1.png.
) else (
    echo file1.txt copy failed. Attempting to copy image1.png.
    :: 拷贝 image1.png
    pscp -pw %PASSWORD% %REMOTE_USER%@%REMOTE_HOST%:%FILE2% %LOCAL_DESTINATION%
)

exit /b
