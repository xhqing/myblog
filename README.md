# myblog
```
# set alias in ~/.zhsrc as follows:
alias new="python3 new.py"
alias gen="python3 gen.py"
alias dep="python3 dep.py"
```

```bash
# confirm current dir is /xxx/xxx/.../myblog
# like this: /Users/mac/Documents/projects/myblog
pwd 

# new a post
# after create a post in ./source/_post it will open typora automatically
new title_name  

# generate all html files
# it will delete the public dir and rebuid dirs and generate all html files
gen 

# deploy on github page, check blog after minutes 
dep
```

it's based on hexo, know more about it [here](https://hexo.io).

# License
MIT



