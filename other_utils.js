

import { question } from "readline-sync"

function saltar_linha() {
  exibir('\n')
}

function exibir(conteudo) {
  console.log(conteudo)
}

function relatorio() {
  exibir('\n========== RELATÓRIO ==========')
}

function fim() {
  exibir('========== FIM ==========\n')
}

function entrada_num(conteudo) {
  return Number(question(conteudo + ' -----> '))
}

function entrada_txt(conteudo) {
  return question(conteudo + ' -----> ')
}

// Para uso em loops numéricos
function eh_numero(alvo) {
  return isNaN(alvo)
}

// Converte números que precisam ter casas decimais reduzidas
function num_decimal(number, casas) {
  return Number(number.toFixed(casas))
} 

// Usar em condições numéricas onde apenas um valor é comparado (até onde pode ir)
function numero_ate(alvo, max) {
  return alvo <= max
}

// Usar em condições numéricas onde um valor está entre um limite mínimo e máximo
function numero_esta_entre(valor_ref, min, max) {
  return valor_ref >= min && valor_ref <= max
}

// Quanto um valor vale do outro em porcentagem
function esse_vale_quanto_desse(valor_comparado, valor_alvo) {
  // O valor sofre um arredondamento leve
  return num_decimal((valor_alvo / valor_comparado) * 100, 1)
}

// Só para calcular montante
function juros_compostos(capital, taxa, periodo) {
  // É esperado que a taxa já tenha sido convertida
  // Em cálculos comuns, costuma-se diminuir as casa no cálculo após a *
  // Essa função deixa o valor original sem abreviação
  // A abreviação fica para o retorno
  let montante = capital * Math.pow(1 + taxa, periodo)
  return num_decimal(montante)
}

// Controlar menor e maior valor em um loop apenas por troca de valores nas variáveis
function loop_num_min_max(valor_ref) {
  let contador = 0
  let min = Infinity
  let max = -min
  let entrada = 0

  while (contador < valor_ref) {
    entrada = entrada_num('Digite um número')
      if (entrada <= min) {
        min = entrada
      }
      if (entrada >= max) {
        max = entrada
      }
      contador++
  }
  return `${min}, ${max}`
}

saltar_linha() 
relatorio()                              // usar antes das saídas
exibir('Javascript')
// exibir(entrada_num('Digite algo'))
// exibir(entrada_txt('Digite algo'))
// exibir(loop_num_min_max(2))
exibir(eh_numero(0))
exibir(num_decimal(187.44963, 2))        // é preferencial que o valor seja de fato um número (evitar string numérica)
exibir(numero_ate(251, 250))             // útil p/ funções com 1 condição numérica com <= (alvo, max) (aplicar 1 em cada condição, exceto else)
exibir(numero_esta_entre(26, 0, 25))
exibir(esse_vale_quanto_desse(90, 89))   // retorno da porcentagem
exibir(juros_compostos(4000, 8/100, 18)) // preciso
fim()

// Devo lembrar:
// Em questões com cálculos de juros, SEMPRE: valor_dado / 100 (inclusive na fórmula de juros)
// Em condições de tanto até (2 valores numéricos mín e máx), o operador + apropriado é: <=
// Em condições que um "let" é usado multiplas vezes em condições, instanciar somente o "let", deixando o retorno p/ fora das condições
