#!/bin/bash

# Parent repository 이름을 묻기
echo "Enter the parent repository name:"
read parent_repo

# 새로운 repository 이름 생성
dev_repo="${parent_repo}-dev"

# GitHub CLI를 사용하여 새로운 private repository 생성
gh repo create "$dev_repo" --private --description "Development repository for $parent_repo" --gitignore Python

# 결과 확인
if [ $? -eq 0 ]; then
    echo "Successfully created repository: $dev_repo"
    
    # 새로운 repository를 현재 디렉토리에 clone
    git clone "https://github.com/crimson206/$dev_repo.git"

else
    echo "Failed to create repository: $dev_repo"
fi
