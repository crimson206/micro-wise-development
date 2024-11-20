#!/bin/bash

read -p "Enter the release tag: " release_tag

git checkout develop

git push origin develop

git checkout main

git push origin main

git push origin "$release_tag"

echo "Release $release_tag has been finished and pushed to the remote repository."
