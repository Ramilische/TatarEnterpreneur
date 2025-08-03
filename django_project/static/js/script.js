function redirect(url)
{
    window.location.href = url;
}

function new_page(url) {
    window.open(url);
}

function show_popup(name, fio, sphere, city, link, photoname) {
    let popupNode = document.querySelector('#popup');
    let overlay = popupNode.querySelector('.overlay');
    let closebtn = popupNode.querySelector('.close-btn');
    function  openPopup() {
        popupNode.classList.add('active');
        let pathtophoto = "/static/images/" + photoname
        console.log(pathtophoto)
        document.getElementById('popup-photo').src=pathtophoto;
        document.getElementById('popup-name').innerHTML=name;
        document.getElementById('popup-fio').innerHTML='<strong>Владелец:</strong> '+fio;
        document.getElementById('popup-sphere').innerHTML='<strong>Сфера:</strong> '+sphere;
        document.getElementById('popup-city').innerHTML='<strong>Город:</strong> '+city;
        document.getElementById('popup-link').onclick=function () {new_page(link)}
    }
    function closePopup() {
        popupNode.classList.remove('active');
    }
    overlay.addEventListener('click', closePopup);
    closebtn.addEventListener('click', closePopup);
    openPopup();
}
