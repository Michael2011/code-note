// range-emo
package main

import (
	"fmt"
)

func main() {
	nums := []int{1,2,3,4,5,6}
	sum := 0
	
	for _,num := range nums {
		sum += num
	}
	
	fmt.Println("sum:", sum)
	
	for i,num := range nums {
		fmt.Println("index: %s value: %s", i, num)
	}
	
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k,v := range kvs {
		fmt.Printf("%s -> %s \n", k, v)
	}
	
	for i, c := range "golang" {
		fmt.Println(i, c)
	}
	
	
	fmt.Println("Hello World!")
}
