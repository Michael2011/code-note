// non-blocking-channel-operations.go 
package main

import (
	"fmt"
)

func main() {
	messages := make(chan string)
	signals	 := make(chan bool)
	
	select {
		case msg := <-messages:
			fmt.Println("recived messages: ", msg)
		default:
			fmt.Println("no messages")
	}
	
	msg := "hi"
	select {
		case messages <- msg:
			fmt.Println("send messages:", msg)
		default:
			fmt.Println("no send")
	}

	select {	
		case msg := <-messages:
			fmt.Println("received messages: ", msg)
			
		case sig := <-signals:
			fmt.Println("received signals: ", sig)
			
		default:
			fmt.Println("no activity")
	}

}
