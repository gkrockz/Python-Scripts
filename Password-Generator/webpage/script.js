const upr_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lwr_chars = "abcdefghijklmnopqrstuvwxyz";
const numbers = "0123456789";
const spl_chars = '!$@.*_-';
const pattern = upr_chars + spl_chars + lwr_chars + numbers;
var password = document.getElementById("result");

function randomValue(value) {
    return Math.floor(Math.random()*value);
}

function copyPassword() {
    password.select();
    document.execCommand('copy');
    alert("Password Copied to ClipBoard")
}

function generatePass() {
    let length = document.getElementById('length').value;
    document.getElementById("pass-length").textContent = length;
    let tempPass = '';
    for(let i=0; i<length ; i++){
        let char = randomValue(pattern.length);
        tempPass += pattern.charAt(char);
    }
    password.value = tempPass;

}

generatePass();