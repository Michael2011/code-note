// slices
package main

import (
	"fmt"
)

func main() {
	s := make([]string, 3)
	fmt.Println("tmp: ", s)
	
	
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set s: ", s)
	
	
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("new s: ", s)
}
