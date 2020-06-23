hex2rgb() {
    hex=$(echo "${1^^}" | sed 's/#//g')

    a=$(echo $hex | cut -c-2)
    b=$(echo $hex | cut -c3-4)
    c=$(echo $hex | cut -c5-6)

    r=$(echo "ibase=16; $a" | bc)
    g=$(echo "ibase=16; $b" | bc)
    b=$(echo "ibase=16; $c" | bc)

    echo $r$g$b"ff"
}

scrot /tmp/copycolor.png
eval $(xdotool getmouselocation --shell)
IMAGE=`convert /tmp/copycolor.png -depth 8 -crop 1x1+$X+$Y txt:-`
COLOR=`echo $IMAGE | grep -om1 '#\w\+'`
COLOR=${COLOR##\#}
echo "rgb "$COLOR"FF" > /tmp/ckbpipe012
