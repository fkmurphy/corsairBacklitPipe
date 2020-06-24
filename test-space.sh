#https://github.com/ckb-next/ckb-next/wiki/Animations#pipe
while true; \
do \
    [[ -n $(git status --porcelain | grep "^??") ]] \
        && echo "rgb space:0000ffff" > /tmp/ckbpipe012 \
        || echo "rgb space:5500ccff" > /tmp/ckbpipe012; \
    sleep 2.5; \
done;
