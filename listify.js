
function listify() {
    var cnt = 0;
    var lst = [];
    var update = [];

    lst.push("About");
    update.push("2023-08-18")

    lst.push("test");
    update.push("2023-08-18")

    var return_string = "<table>";
    for(let i = 0; i< lst.length; i++) {
        return_string += `
            <tr id="blog-${lst[i]}">
                <td class="article-title" onclick="render_blog('${lst[i]}')">
                    ${lst[i]}
                </td> 
                <td class="article-date">
                    ${update[i]}
                </td>
            </tr>
        `
    }
    return_string += "</table>"
    document.getElementById("list").innerHTML = return_string;
}