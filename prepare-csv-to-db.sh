#!/bin/bash
FILE=$1
SET_NULLS="sed -rI bk 's/,,/,\\N,/g'"
REMOVE_DQOUTE="sed -rI bk 's/\"//g'"

[ -z "$FILE" ] && echo "CSV file as the only one argument is needed" && exit 1

echo $SET_NULLS $FILE
eval $SET_NULLS $FILE
eval $SET_NULLS $FILE
eval $REMOVE_DQOUTE $FILE
eval $REMOVE_DQOUTE $FILE

