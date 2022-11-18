#!/bin/sh

# systray battery icon
cbatticon -u 20 -i notification -c "poweroff" -l 15 -r 3 &
udiskie &
feh --bg-scale /home/ducuara/Pictures/196720.jpg &
picom &
run volumenicon &
