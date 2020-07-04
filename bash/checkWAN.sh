#!/bin/bash

while [ True ]; do
	if ping -q -c 1 -W 1 8.8.8.8 > /dev/null; then
		echo "IPv4 up "
	else
		echo "Ipv4 down"
	fi
	sleep 20
done
