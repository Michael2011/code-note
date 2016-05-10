// struct-demo
package main

import (
	"fmt"
)

type person struct {
	name string
	age int
}


func main() {
	
	fmt.Println(person{"bob", 20})
	
	fmt.Println(person{name: "boob", age: 30})
	fmt.Println(person{name: "bb"})
	
	fmt.Println(&person{name:"Anna", age:20})
	
	
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)
	
	sp := &s
	fmt.Println(sp.age)
	
	sp.age = 51
	fmt.Println(s)
}
