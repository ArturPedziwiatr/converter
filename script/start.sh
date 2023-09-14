#!/bin/bash

CRED='\033[1;31m'

if [[ ! -n $1 ]] || [[ ! -n $2 ]]; then
  echo -e "${CRED} Two arguments needed"
  exit 1
elif [[ ! -f $1 ]]; then
  echo -e "${CRED} File not found $1"
  exit 2
elif [[ ! -d $2 ]]; then
  echo -e "Folder not found $2"
  mkdir -p $2
fi

if [ ! -d './output/tmp' ]; then
  mkdir -p output/tmp
fi

FILE=$(python convert.py $1)
if [[ ! -n $FILE ]]; then
  echo -e "${CRED} Error with convert LAZ to LAS"
  exit 3
fi
echo $FILE

EPSG=$(entwine info $FILE | grep -Po '(?<=EPSG:)\d+')
if [[ ! -n $EPSG ]]; then
  echo -e "${CRED} Cannot found EPSG"
  exit 4
fi
echo $EPSG

./gocesiumtiler -i $FILE -o $2 -e $EPSG
rm $FILE