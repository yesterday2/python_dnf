#!/bin/bash

str="hello world"
str1=".png"
str2=".json"
PNG_NUM=800

demoFunc(){
	echo "hello world"
	for((i=1;i<$PNG_NUM;i++));
	do
		jsonname=$i$str2
		echo "ith json name" $jsonname
		if [ ! -f "$jsonname" ]; then
			echo $i"th"$jsonname" not exist"
		        j=$i
		        for((;j<$PNG_NUM ;j++));
		        do
		                jname=$j$str2
		                if [ -f "$jname" ]; then
		                break
		                fi
		        done
		        if [ $j -ge $PNG_NUM ] ; then
		                echo "end here json not exist i= "$i 
				for((;i<PNG_NUM;i++));
		                do
		                        ipngname=$i$str1
					if [ -f "$ipngname" ] ; then
			                        rm $ipngname			
						echo "rm file = "$ipngname
					fi
		                done
		               	exit
		        fi
			echo $j" json file exist"
		        jjsonname=$j$str2
		        jpngname=$j$str1

		        ijsonname=$i$str2
		        ipngname=$i$str1

		        ipng=$i$str1
		        echo "excute replace operationa i="$i "j="$j $jjsonname $ijsonname $jpngname $ipngname
			mv $jjsonname $ijsonname
		        mv $jpngname $ipngname
	
		fi
		echo $jpgname
	done
	
}

makePng(){

	for((i=1;i<$PNG_NUM;i++));
	do
		ijsonname=$i$str2
		ipngname=$i$str1
		echo $i"th file : "$ijsonname $ipngname"is creating"
		touch $ijsonname
		touch $ipngname
	done
}

#生成10张图片
#makePng

#把没有json的图片去掉
demoFunc


