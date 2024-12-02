#!/usr/bin/env bash
x=1

while [ $x -le 5 ]

do
        echo "This is the number $x"
        x=$(( $x + 1 ))
done

