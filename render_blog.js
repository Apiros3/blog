
function render_blog(path) {
    // console.log(path)
    document.getElementById("content").innerHTML = `
        <iframe src="blog-html/${path}.html" title="${path}" frameBorder="0"></iframe>
    `
}
