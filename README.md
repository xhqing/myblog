# myblog
```
# set alias in ~/.zhsrc as follows:
alias new="python3 new.py"
alias dep="python3 dep.py"
```

```bash
# confirm current dir is /xxx/xxx/.../myblog
# like this: /Users/mac/Documents/projects/myblog
pwd 

# new a post
# after create a post in ./source/_post it will open typora automatically
new title_name  

# it will delete the public dir and rebuid dirs and generate all html files
# and then deploy on github page, you can check blog after minutes 
dep
```

it's based on hexo, know more about it [here](https://hexo.io).

# theme
theme based on [hexo-theme-clean-blog](https://github.com/klugjo/hexo-theme-clean-blog).

# License
MIT



