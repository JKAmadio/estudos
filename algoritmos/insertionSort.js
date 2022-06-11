/*
 * ORDENAÇÃO POR INSERÇÃO (INSERTION SORT)
 * (eficiente para ordenação de pequeno número de elementos)
 *
 * Entrada: uma sequência de n números (a1, a2,...,an)
 * Saída: uma reordenação (a'1, a'2,...,a'n) tal que a'1<=a'2<=...<=a'n
 *
 * Exemplo: Iniciamos com a mão esquerda vazia e algumas cartas viradas para baixo
 *          Em seguida, retiramos uma carta de cada vez da mesa e a inserimos na
 *          posição correta da mão esquerda. Para encontrar a posição correta para
 *          uma carta, nós a comparamos com cada uma das cartas que já estão na mão,
 *          da direita para a esqueda. Em todas as vezes, as cartas que seguramos na
 *          mão esquerda são ordenadas, e essas cartas eram as que estavam na parte
 *          superior da pilha sobre a mesa.
 *
*/

function crescentInsertionSort(numberList) {
  for (let j = 1; j < numberList.length; j++) {
    key = numberList[j];
    i = j - 1;
    while(i >= 0 && numberList[i] > key) {
      numberList[i + 1] = numberList[i];
      i--;
    }
    numberList[i + 1] = key;
  }
  return numberList;
}

function decrescentInsertionSort(numberList) {
  for (let j = 1; j < numberList.length; j++) {
    key = numberList[j];
    i = j - 1;
    while(i >= 0 && numberList[i] < key) {
      numberList[i + 1] = numberList[i];
      i--;
    }
    numberList[i + 1] = key;
  }
  return numberList;
}

