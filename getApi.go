package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
)

type ApiResponse struct {
	Origin string `json:"origin"`
}

func getApi() {
	backticks := "```"
	json := fmt.Sprintf(`{
		"top_p": 1,
		"stop": "%s",
		"temperature": 0,
		"suffix": "\n%s",
		"max_tokens": 1000,
		"presence_penalty": 0,
		"frequency_penalty": 0,
		"model": "text-davinci-003",
		"prompt": "Show me how create a file on Linux:\n%sbash\n#!/bin/bash\n"}`, backticks, backticks, backticks)

	jsonBody := []byte(json)
	bodyReader := bytes.NewReader(jsonBody)
	config := NewConfig()
	apiAddr := fmt.Sprintf("%s/completions", config.APIBase)
	req, err := http.NewRequest("POST", apiAddr, bodyReader)
	if err != nil {
		fmt.Println("Error al crear la petición:", err)
		wg.Done()
		return
	}
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Authorization", "Bearer "+config.APIKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error al enviar la petición:", err)
		wg.Done()
		return
	}
	defer resp.Body.Close()
	// Leer la respuesta del servidor
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error al leer la respuesta:", err)
		wg.Done()
		return
	}

	// Imprimir la respuesta del servidor
	fmt.Println(string(body))
	wg.Done()
}
