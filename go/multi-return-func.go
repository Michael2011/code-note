// multi-return-func
package main

import (
	"fmt"
)

func vals() (int, int) {
	return 3, 7
}


func main() {
	a, b := vals()
	fmt.Println("%d -> %d", a, b)	
	
	_, c := vals()
	fmt.Println(c)
}
