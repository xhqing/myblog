# myblog
```
# set alias in ~/.zhsrc as follows:
alias new="python3 new.py"
alias dep="python3 deploy.py"
```

```bash
# confirm current dir is /xxx/xxx/.../myblog
pwd # like this: /Users/mac/Documents/projects/myblog

# new a post
new post_title_name # after create a post in ./source/_post it will open typora automatically

# generate all html files and deploy on github
dep # it will delete the public dir and rebuid dirs and generate all html files and deploy on github
```

it's based on hexo, know more about it [here](https://hexo.io).

# License
MIT



