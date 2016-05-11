function getKeyCode(e) {
    e = e || window.event;
    return (e.keyCode || e.which);
}

window.onload = () => {
    document.onkeypress = function(e) {
        console.log(getKeyCode(e));
    };
};
