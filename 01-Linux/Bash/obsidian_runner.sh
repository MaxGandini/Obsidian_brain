#!/bin/bash
if [ -f "$1" ]; then
   nvim "$1"
else
   echo "Error: File path '$1' does not exist or is not accessible."
fi
