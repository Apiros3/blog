import os, glob
import markdown
import datetime 

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
    files.sort(key=os.path.getctime, reverse=True)
    
    for filename in files:
        with open(filename, 'r') as f: # open in readonly mode
            # do your stuff
            print(str(filename))
            text = f.read()
            html = markdown.markdown(text)
            # print(str(html))

        with open(f"blog-html/{str(filename)[8:-3]}.html", 'w') as f:
            f.write(html)

        #append to listify() command
        g.writelines(
f"""
    lst.push("{str(filename)[8:-3]}");
    update.push("{datetime.datetime.fromtimestamp(os.path.getctime(filename)).strftime('%Y-%m-%d')}")
"""
        )
    g.writelines(
f"""
    var return_string = "<table>";
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