// timer-demo
package main

import (
	"fmt"
	"time"
)

func main() {
		timer1 := time.NewTimer(time.Second * 2)
		
		<-timer1.C
		fmt.Println("timer 1 expired")
		
		timer2 := time.NewTimer(time.Second)
		go func() {
			<-timer2.C
			fmt.Println("timer 2 expired")
		}()
	
		fmt.Println(time.Second * 10)
		/*
		stop2 := timer2.Stop()
		if stop2 {
			fmt.Println("Timer 2 stoped")
		}
		*/
	
}
