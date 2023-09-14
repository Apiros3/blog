
function init() {
    document.querySelectorAll('.external a').forEach((el) => {
        el.setAttribute('rel', 'noopener noreferrer');
        el.setAttribute('target', '_blank');
    });
}
