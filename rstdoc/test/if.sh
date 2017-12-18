#!/bin/bash
#================================================
#FileName   :scroeN_46_zhaojiedi.sh
#Author     :zhaojiedi
#Description:
#DateTime   :2017-12-18 14:43:18
#Version    :V1.0
#Other      :
#================================================

read -p "please you score :"   score

if [[ ! "$score" =~ ^[0-9]+$ ]];then
        echo -e  "\033[31myou enter wrong , must a digit\033[0m"
        exit 2
if [ "$score" -lt 60 ];then
        echo "you is 0-59" 
elif [ "$score" -lt 80 ];then
        echo " you is 60-80" 
elif [ "$score" -lt 100 ];then
        echo "you is 80-100" 
else
        echo "you enter a bit digit ,only in range 0-100"
fi
