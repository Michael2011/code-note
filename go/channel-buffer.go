// channel-buffer
package main

import (
	"fmt"
)

func main() {
	message := make(chan string, 2)

	message <- "channel"
	message <- "buffer"

	// message <- "test"

	fmt.Println( <-message)
	fmt.Println( <-message)
	


}
