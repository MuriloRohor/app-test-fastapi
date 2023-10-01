async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais');
    const animais = response.data;
    const lista = document.getElementById('lista-animais');
    animais.forEach(animal => {
        const item = document.createElement('li');
        item.innerText = animal.nome;
        lista.appendChild(item)
    });
    
    
}

function app(){
    console.log("App iniciada!");
};

app();
carregarAnimais();