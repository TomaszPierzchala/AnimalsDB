#!/bin/bash
MYSQL='/usr/local/mysql/bin/mysql'
USER='dataload'

echo Balbc
$MYSQL -u "$USER" -p"$(cat .passwd)" < load.Balbc.sql

echo Balbc_porody
$MYSQL -u "$USER" -p"$(cat .passwd)" < load.Balbc_porody.sql

echo C57Bl6
$MYSQL -u "$USER" -p"$(cat .passwd)" < load.C57Bl6.sql

echo C57Bl6_porody
$MYSQL -u "$USER" -p"$(cat .passwd)" < load.C57Bl6_porody.sql
