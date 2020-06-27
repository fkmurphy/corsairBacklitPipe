#https://github.com/ckb-next/ckb-next/wiki/Animations#pipe
while true; \
do \
    # para K55 zone1, zone2 y zone3 son las secciones del teclado
    # de izquierda a derecha
    ping -c1 1.1.1.1 &>/dev/null \
        && echo "rgb zone1:00ff00ff" > /tmp/ckbpipe012 \
        || echo "rgb zone3:ff0000ff" > /tmp/ckbpipe012; \
    sleep 0.3; \
done;
