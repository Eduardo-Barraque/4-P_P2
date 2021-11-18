function carregar_produtos() {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "{{ url_for('produtos') }}" );
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("produtos").innerHTML = xhr.response;
        }
    }
    xhr.send();
    return false;
    }
    document.getElementById("patrocinado").onload = function() {carregar_produtos()};