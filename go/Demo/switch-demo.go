// switch-demo
package main

import (
	"fmt"
	"time"
)

func main() {
	i := 2
	switch i {
		case 1:
			fmt.Println("one")
			
		case 2:
			fmt.Println("two")
			
		default:
			fmt.Println("other")
	}
	
	switch time.Now().Weekday() {
		case time.Saturday, time.Sunday:
			fmt.Println("ti's the wenkend")
		default:
			fmt.Println("defautl")
	}
	
	t := time.Now()
	switch {
		case t.Hour() < 12:
			fmt.Println("12")
		default:
			fmt.Println("it's after noon")
	}



}
