// Aguarde até que o documento esteja completamente carregado
document.addEventListener("DOMContentLoaded", function () {
  // Função para criptografar um texto com a cifra de Cesar
  function encryptCesar(text, shift) {
    let result = "";

    for (let i = 0; i < text.length; i++) {
      let char = text[i];

      if (char.match(/[a-z]/i)) {
        const code = text.charCodeAt(i);

        if (char.match(/[A-Z]/)) {
          char = String.fromCharCode(((code - 65 + shift) % 26) + 65);
        } else if (char.match(/[a-z]/)) {
          char = String.fromCharCode(((code - 97 + shift) % 26) + 97);
        }
      }

      result += char;
    }

    return result;
  }

  // Função para decriptografar um texto com a cifra de Cesar
  function decryptCesar(text, shift) {
    return encryptCesar(text, 26 - shift);
  }

  // Função para exibir o resultado na div
  function showResult() {
    const inputText = document.querySelector(
      'textarea[name="inserttext"]'
    ).value;
    const option = document.querySelector("#opcao").value;
    const shift = parseInt(document.querySelector("#deslocamento").value);
    const resultadoDiv = document.querySelector("#resultado");

    if (option === "encrypt") {
      resultadoDiv.textContent =
        "Texto Encriptado: " + encryptCesar(inputText, shift);
    } else if (option === "decrypt") {
      resultadoDiv.textContent =
        "Texto Decriptado: " + decryptCesar(inputText, shift);
    } else {
      resultadoDiv.textContent = "";
    }
  }

  // Adicionar um ouvinte de evento ao botão para chamar a função showResult
  const button = document.querySelector(".botao");
  button.addEventListener("click", showResult);
});
