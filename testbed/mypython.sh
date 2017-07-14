#!/bin/bash
if [ $# -eq 0 ]
then
  ~/anaconda3/bin/python3
else
  ~/anaconda3/bin/python3 $1
fi
