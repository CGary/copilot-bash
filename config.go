package main

import (
	"os"
)

type config struct {
	APIKey  string
	APIBase string
	Shell   string
}

func NewConfig() config {
	apiKey := os.Getenv("OPENAI_API_KEY")
	if apiKey == "" {
		// fmt.Println("This program requires an OpenAI API key to run. Please set the OPENAI_API_KEY environment variable. https://github.com/m1guelpf/plz-cli#usage")
		// os.Exit(1)
		apiKey = "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"
	}

	apiBase := os.Getenv("OPENAI_API_BASE")
	if apiBase == "" {
		apiBase = "https://api.openai.com/v1"
	}

	shell := os.Getenv("SHELL")
	if shell == "" {
		shell = os.Getenv("SHELL") // Fallback to default shell if not set
	}

	return config{
		APIKey:  apiKey,
		APIBase: apiBase,
		Shell:   shell,
	}
}
