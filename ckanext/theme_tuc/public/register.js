document.getElementById("check2").onclick = function () {
    document.getElementById("organization").style.display = 'none';
    document.getElementById("individual").style.display = 'block';
};

document.getElementById("check1").onclick = function () {
    document.getElementById("individual").style.display = 'none';
    document.getElementById("organization").style.display = 'block';
};