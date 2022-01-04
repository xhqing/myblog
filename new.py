import os
import sys

if __name__ == "__main__":
    
    try:
        os.remove("./nohup.out")
    except:
        pass

    post_title = sys.argv[1]
    os.system(f"nohup hexo new {post_title}")

    with open("./nohup.out", "r") as f:
        sec_line = f.readlines()[1][:-1]
        
    print(sec_line)
    print(sec_line.split("/"))
        
    mdfile_path = "./source/_posts/" + sec_line.split("/")[-1]
    print(mdfile_path)

    with open(mdfile_path, "r") as mdf:
        mdf_lines = mdf.readlines()

    last_line = mdf_lines[-1]
    mdf_lines[-1] = "mathjax: true\n"
    mdf_lines.append(last_line)
    print(mdf_lines)

    with open(mdfile_path, "w+") as mdf:
        for string in mdf_lines:
            mdf.write(string)

    os.system(f"open {mdfile_path}")
