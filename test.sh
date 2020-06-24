#https://github.com/ckb-next/ckb-next/wiki/Animations#pipe
while true; \
do \
    ping -c1 1.1.1.1 &>/dev/null \
        && echo "rgb zone1:00ff00ff" > /tmp/ckbpipe012 \
        || echo "rgb zone3:ff0000ff" > /tmp/ckbpipe012; \
    sleep 0.3; \
done;
