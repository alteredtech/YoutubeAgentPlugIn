@echo off
echo This will stage all and commit to master branch
set /p commit=Please enter your commit: 
git stage -A && git commit -m "%DATE% %commit% %ComputerName%" && git push