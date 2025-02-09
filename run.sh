#!/bin/bash
recipename=$(rofi -dmenu -p "recipe:")
if [ -n "$recipename" ]; then
    echo "You entered: $recipename"
    out=$(scrapeOpenEmbedded -p -s "$recipename" | rofi -dmenu)
    echo "$out" | xclip -selection clipboard
fi
