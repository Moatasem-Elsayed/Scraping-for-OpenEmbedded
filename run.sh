#!/bin/bash
path=$(dirname "$0")
recipename=$(rofi -dmenu -p "recipe:")
if [ -n "$recipename" ]; then
    echo "You entered: $recipename"
    out=$(python "$path"/openEmbedded.py "$recipename" | rofi -dmenu)
    echo "$out" | xclip -selection clipboard
fi
