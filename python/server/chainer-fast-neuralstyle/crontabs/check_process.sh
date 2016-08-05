#!/bin/bash
source /etc/profile

if [ `ps -aux | grep "svn" | grep -v 'grep' | wc -l` -lt 1 ]
then
	#使用svn更新数据，只能运行一个svn
	svn up
fi

cd /data/htdocss/chainer-fast-neuralstyle/workspace/chainer-fast-neuralstyle
source /data/htdocss/chainer-fast-neuralstyle/bin/activate

if [ `ps -aux | grep "python2.7 work.py -g 0 -e us" | grep -v 'grep' | wc -l` -lt 1 ]
then
	nohup python2.7 work.py -g 0 -e us > /dev/null &
	# /bin/bash /data/htdocss/chainer-fast-neuralstyle/workspace/chainer-fast-neuralstyle/crontabs/run.sh
fi

if [ `ps -aux | grep "python2.7 work.py -g 1 -e us" | grep -v 'grep' | wc -l` -lt 1 ]
then
	nohup python2.7 work.py -g 1 -e us > /dev/null &
	# /bin/bash /data/htdocss/chainer-fast-neuralstyle/workspace/chainer-fast-neuralstyle/crontabs/run.sh
fi

if [ `ps -aux | grep "python2.7 work.py -g 2 -e us" | grep -v 'grep' | wc -l` -lt 1 ]
then
	nohup python2.7 work.py -g 2 -e us > /dev/null &
	# /bin/bash /data/htdocss/chainer-fast-neuralstyle/workspace/chainer-fast-neuralstyle/crontabs/run.sh
fi

if [ `ps -aux | grep "python2.7 work.py -g 3 -e us" | grep -v 'grep' | wc -l` -lt 1 ]
then
	nohup python2.7 work.py -g 3 -e us > /dev/null &
	# /bin/bash /data/htdocss/chainer-fast-neuralstyle/workspace/chainer-fast-neuralstyle/crontabs/run.sh
fi
