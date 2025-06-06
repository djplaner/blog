#!/bin/zsh

# build the static html in ~/blog2
mkdocs build
# generate the page index in ~/memex_site
python3 -m pagefind --site ~/blog2
# remove the old pagefind index in ~/memex
rm -rf ~/blog/docs/pagefind
# update ~/memex pagefind index
cp -pfr ~/blog2/pagefind ~/blog/docs/pagefind
