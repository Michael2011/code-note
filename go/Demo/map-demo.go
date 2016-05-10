// map-demo
package main

import (
	"fmt"
)

func main() {
	m := make(map[string] int)
	
	m["k1"] = 7
	m["k2"] = 12
	
	fmt.Println("new map", m)
	
	v1 := m["k1"]
	fmt.Println("get map: ", v1, len(m))
	
	delete(m, "k1")
	fmt.Println("after delete: ", m)
	
	_, prs := m["k1"]
	fmt.Println("get delete value", prs)
	
	n := map[string]int{"foo":1, "bar": 2}
	fmt.Println(n)
}
