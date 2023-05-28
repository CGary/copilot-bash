package main

import (
	"fmt"
	"os"
)

func run() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run main.go <input>")
		return
	}

	input := os.Args[1]
	fmt.Println("Input:", input)
}
