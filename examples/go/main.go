package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Fprintln(os.Stderr, "tg_username_full is retired and no longer accepts new tasks. Review the current Telegram Username/Profile products before choosing a supported task_type.")
	os.Exit(1)
}
