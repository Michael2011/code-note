// for-demo
package main

import (
	"fmt"
)

func main() {
	i := 1
	for i<3 {
		fmt.Println(i)
		i = i + 1
	}
	
	for i:=7; i<9; i++ {
		fmt.Println(i)
	}
	
	for {
		fmt.Println("loop")
		break
	}
	
	fmt.Println("Hello World!")
}
