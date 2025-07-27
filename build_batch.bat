@echo off

set list=WWWWWWWW YYYYYYYY
set magicNum=0

(for %%a in (%list%) do (
   start /b build_pack.bat %%a %magicNum%
))


pause