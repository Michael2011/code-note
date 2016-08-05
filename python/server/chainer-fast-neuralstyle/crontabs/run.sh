#!/bin/bash
ps -ef | grep 'python2.7 work.py' | gawk '{print $2}' | xargs kill -9
sleep 5

source /data/htdocss/chainer-fast-neuralstyle/bin/activate
cd /data/htdocss/chainer-fast-neuralstyle/workspace/chainer-fast-neuralstyle

nohup python2.7 work.py -g 0  -e us > /dev/null &
nohup python2.7 work.py -g 1  -e us > /dev/null &
nohup python2.7 work.py -g 2  -e us > /dev/null &
nohup python2.7 work.py -g 3  -e us > /dev/null &
