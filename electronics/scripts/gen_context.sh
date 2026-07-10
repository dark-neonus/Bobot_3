#!/bin/bash

# Iterate over the arguments safely, handling spaces in filenames
for file in "$@"; do
    # Ensure the file actually exists before trying to read it
    if [ -f "$file" ]; then
        printf "\n\`\`\`%s\n" "$(basename "$file")"
        cat "$file"
        printf "\n\`\`\`\n"
    else
        echo "Warning: File '$file' not found." >&2
    fi
done
