import os, glob
import markdown
import datetime 

path = 'blog-html'
files = glob.glob(os.path.join(path, '*.html'))
for filename in files:
    os.remove(filename)

path = 'blog-md'
with open("listify.js", 'w') as g:
    g.writelines(
"""
function listify() {
    var cnt = 0;
    var lst = [];
    var update = [];
"""        
    )
    files = glob.glob(os.path.join(path, '*.md'))
    files.sort(key=os.path.getmtime, reverse=True)
    
    for filename in files:
        with open(filename,  encoding="utf-8", mode = 'r') as f: # open in readonly mode
            # do your stuff
            print(str(filename))
            text = f.read()
            html = markdown.markdown(text)
            # print(str(html))

        with open(f"blog-html/{str(filename)[8:-3]}.html", 'w') as f:
            f.writelines("""
<link rel="stylesheet" href="style.css">
                         
""")
            f.write(html)

        if (str(filename)[8:-3] == "default"):
            continue
        #append to listify() command
        g.writelines(
f"""
    lst.push("{str(filename)[8:-3]}");
    update.push("{datetime.datetime.fromtimestamp(os.path.getctime(filename)).strftime('%Y-%m-%d')}")
"""
        )
    g.writelines(
f"""
    var return_string = "<table><tr class='blog-sidebar'><td class='sidebar-title'>Title:</td><td class='sidebar-date'>Last Update:</td></tr>";
    for(let i = 0; i< lst.length; i++) {{
        return_string += `
            <tr id="blog-${{lst[i]}}">
                <td class="article-title" onclick="render_blog('${{lst[i]}}')">
                    ${{lst[i]}}
                </td> 
                <td class="article-date">
                    ${{update[i]}}
                </td>
            </tr>
        `
    }}
    return_string += "</table>"
    document.getElementById("list").innerHTML = return_string;
"""        
    )
    g.writelines("""}""")