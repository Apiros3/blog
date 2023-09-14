
function listify() {
    var cnt = 0;
    var lst = [];
    var update = [];

    lst.push("opalってアプリ");
    update.push("2023-09-14")

    lst.push("main-page案");
    update.push("2023-09-13")

    lst.push("買いたいものリスト");
    update.push("2023-09-13")

    lst.push("ブログ作った話");
    update.push("2023-08-19")

    lst.push("About");
    update.push("2023-08-18")

    var return_string = "<table><tr class='blog-sidebar'><td class='sidebar-title'>Title:</td><td class='sidebar-date'>Last Update:</td></tr>";
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