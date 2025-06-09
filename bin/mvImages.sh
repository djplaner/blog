#!/bin/zsh
# mvImages.sh
# - find all images in ~/memex/docs and move them to ~/assets/memex/
#   maintaining the same directory structure

for file in `/usr/bin/find ~/blog/docs -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" `; do
    # get the directory structure of the file
    dir=$(dirname "$file")
    # get the relative path of the file
    rel_path=${dir#~/blog/docs/}
    # create the destination directory if it doesn't exist
    mkdir -p ~/assets/blog/$rel_path
    # move the file to the destination directory
    cp "$file" ~/assets/blog/$rel_path/
done
