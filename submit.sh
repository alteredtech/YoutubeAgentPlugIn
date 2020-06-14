#!/bin/bash
echo 'This will stage all and commit to master branch'
read -p 'Enter your commit:' commit
git stage -A && git commit -m "$(date +%F) $commit $HOSTNAME" && git push