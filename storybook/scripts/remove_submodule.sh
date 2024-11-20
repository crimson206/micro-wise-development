#!/bin/bash

read -p "Enter the submodule name to remove: " sub_repo_name
git config --local --remove-section submodule.$sub_repo_name
git rm --cached $sub_repo_name
rm -rf .git/modules/$sub_repo_name
