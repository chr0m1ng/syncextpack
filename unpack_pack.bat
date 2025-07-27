@echo off
set apimSerial=WWWWWWWW
set magicNum=0

REM crypto_pack_old.exe -u SyncExtPack/install.bin OutPack %apimSerial% %magicNum%
crypto_pack.exe -u SyncExtPack/install.bin OutPack %apimSerial% %magicNum%
REM crypto_pack.exe -u SyncExtPack/update.bin OutPack %apimSerial% %magicNum%
REM crypto_pack_old.exe -u SyncExtPack/update.bin OutPack %apimSerial% %magicNum%
REM crypto_pack.exe -u SyncExtPack/update.bin OutPack %apimSerial% %magicNum%
REM crypto_pack.exe -u SyncExtPack/pack_install.bin OutPack %apimSerial% %magicNum%
pause