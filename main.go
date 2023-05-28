package main

import (
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	wg.Add(1)
	go getApi()
	run()
	wg.Wait()
}
