#!/bin/bash
# Remove backslashes before slashes and other characters
cleaned_path=$(echo "$1" | sed 's/\\//g')

# Remove trailing '/.' if it exists
cleaned_path=$(echo "$cleaned_path" | sed 's/\/\.$//')

# Debugging line to verify the cleaned path
echo "Cleaned path: $cleaned_path" >> /home/Xilian/obsidian_runner_log.txt

# Open the file in Neovim, forcing it to stay in the foreground
nvim "$cleaned_path"

# Pause to keep the terminal window open (if needed for debugging)
read -p "Press any key to exit..."
