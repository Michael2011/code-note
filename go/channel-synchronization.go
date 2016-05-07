// channel-synchronization.go
package main

import (
	"fmt"
	"time"
)

func worker(done chan bool) {
	fmt.Println("work ...")
	time.Sleep(time.Second)
	fmt.Println("done")
	
	done <- true
}

func main() {
	
	done := make(chan bool, 1)
	go worker(done)
	
	<- done


}



