#!/bin/zsh

# build the static html in ~/blog2
mkdocs build
# generate the page index in ~/memex_site
python3 -m pagefind --site ~/blog2
# remove the old pagefind index in ~/memex
rm -rf ~/blog/docs/pagefind
# update ~/memex pagefind index
cp -pfr ~/blog2/pagefind ~/blog/docs/pagefind
# if --push is passed, push the changes to the remote repository
if [[ "$1" == "--push" ]]; then
    cd ~/blog2
    ssh djones@djon.es "rm -rf /home/djones/public_html/blog/pagefind/"
    rsync -azvuPh . djones@djon.es:/home/djones/public_html/blog/ --delete
    cd ~/memex
fi
