// variadic-func
package main

import (
	"fmt"
)

func sum(nums ... int) {
	fmt.Println(nums)
	
	total := 0
	for _,num := range nums {
		total += num
	}
	fmt.Println(total)
}


func main() {
	fmt.Println("Hello World!")
	sum(1,2,3)
	sum(12,3,5,4,5)
	
	nums := []int{1,2,3,4,5}
	
	sum(nums ...)
}
