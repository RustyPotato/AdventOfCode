#!/bin/bash

if [ -z "$1" ] || [ ! -e "$1.cob" ]
then
  echo "To run this script, use the following format:"
  echo "./build.sh <Day1>"
  echo "Where Day1 is the name of the .cob file to compile (and run)"
  return
fi

cobc -free -x -o $1.exe $1.cob && ./$1.exe && rm ./$1.exe

