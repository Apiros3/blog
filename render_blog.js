
function render_blog(path) {
    // console.log(path)
    document.getElementById("content").innerHTML = `
        <iframe src="blog-html/${path}.html" title="${path}" frameBorder="0"></iframe>
    `
}

function initial_blog_load() {

    const searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has('blog')) {
        render_blog(searchParams.get('blog'));
    }
    else {
        render_blog('default');
    }

}