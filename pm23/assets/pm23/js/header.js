let burger = document.getElementById('burger'),
    header = document.getElementById('header'),
    body = document.getElementById('body');

burger.addEventListener('click', () => {
    if (header.classList.contains('_active')) {
        header.classList.remove('_active');
        burger.classList.remove('_active');
        body.classList.remove('_noscroll');
    } else {
        header.classList.add('_active');
        burger.classList.add('_active');
        body.classList.add('_noscroll');

        header.addEventListener('click', el => {
            if (el.target == header) {
                header.classList.remove('_active');
                burger.classList.remove('_active');
                body.classList.remove('_noscroll');
            }
        });
    }
});