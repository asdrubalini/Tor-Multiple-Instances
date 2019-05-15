#!/bin/bash

if [ $# -eq 0  ]
    then
        echo "You need to specify torrc filename as commandline argument"
        exit
fi


sudo tor -f $1
