package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"time"

	"github.com/gidoBOSSftw5731/log"
)

const (
	statusURL = "http://10.10.10.3/status"
)

var (
	isOpen = true
)

func main() {
	log.SetCallDepth(4)

	for {
		response, _ := http.Get(statusURL)

		//defer response.Body.Close()

		responseData, _ := ioutil.ReadAll(response.Body)

		responseString := string(responseData)

		if responseString == "1" {
			isOpen = true
		} else if responseString == "0" {
			isOpen = false
		}

		fmt.Println(isOpen)

		go response.Body.Close()

		time.Sleep(2 * time.Millisecond)
	}
}
