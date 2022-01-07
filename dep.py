import os

def listdir(dir_name):
    return os.listdir(f"./public/{dir_name}")

if __name__ == "__main__":
    os.system("hexo clean && hexo generate")

    years = [str(y) for y in range(2022,2222)]

    first_dirs = os.listdir("./public")
    target_dirs = []
    for d in first_dirs:
        if d in years:
            target_dirs.append(d)

    html_path_list = []
    months = list(map(listdir, target_dirs))
    for i in range(len(target_dirs)):
        for m in months[i]:
            html_path_list.append(f"./public/{target_dirs[i]}/{m}/")

    dates = list(map(os.listdir, html_path_list))
    dates_path = []
    for i in range(len(html_path_list)):
        for date in dates[i]:
            dates_path.append(html_path_list[i]+date+"/")

    mddirs = list(map(os.listdir, dates_path))
    index_html_path = []
    for i in range(len(dates_path)):
        for md in mddirs[i]:
            index_html_path.append(dates_path[i]+md+"/"+"index.html")
    
    # ========== mathjax =============
    for html in index_html_path:
        with open(html, "r") as f:
            lines = f.readlines()
        
        for i in range(len(lines)):
            if lines[i] == "<head>\n":
                head_index = i
                break
        
        insert_string = "    <link href=\"https://cdn.bootcss.com/KaTeX/0.7.1/katex.min.css\" rel=\"stylesheet\">\n"
        if insert_string not in lines:
            new_lines = lines[:head_index+1] + [insert_string] + lines[head_index+1:]

            with open(html, "w+") as f:
                for line in new_lines:
                    f.write(line)
   
    # ========== jpg png ==============
    os.system("cp source/_posts/*.jpg public/img/")
    os.system("cp source/_posts/*.png public/img/")
    for html in index_html_path:
        with open(html, "r") as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            if "<img src=" in line:
                new_line = line[:10] + "/img/" + line[10:]
                new_lines.append(new_line)
            else:
                new_lines.append(line)
                
        with open(html, "w+") as f:
            for line in new_lines:
                f.write(line)

    os.system("hexo deploy")
