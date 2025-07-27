#!/bin/bash

# Set default values
apimSerial="WWWWWWWW"
magicNum=0

echo "Unpacking with APIM Serial: $apimSerial, Magic Number: $magicNum"

# crypto_pack_old -u SyncExtPack/install.bin OutPack $apimSerial $magicNum
./crypto_pack -u SyncExtPack/install.bin OutPack $apimSerial $magicNum
# ./crypto_pack -u SyncExtPack/update.bin OutPack $apimSerial $magicNum
# crypto_pack_old -u SyncExtPack/update.bin OutPack $apimSerial $magicNum
# ./crypto_pack -u SyncExtPack/update.bin OutPack $apimSerial $magicNum
# ./crypto_pack -u SyncExtPack/pack_install.bin OutPack $apimSerial $magicNum

echo "Press any key to continue..."
read -n 1 -s
