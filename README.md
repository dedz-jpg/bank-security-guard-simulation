# Bank Security Guard Simulation 

Projeto que simula a rotina de um segurança de banco, responsável por controlar a entrada de clientes antes do horário de fechamento.

---

## Cenário do problema:

- O banco abre e funciona até as **18h**.
- O segurança fica verificando:

1. Se o horário atual já chegou às 18h:
   - Se sim → O segurança fecha o banco.
2. Se ainda for antes das 18h:
   - O segurança verifica se há clientes do lado de fora.
   - Se houver clientes → Ele os adiciona à fila de atendimento.

---

## Lógica aplicada:

- Controle de horário (simulado com uma variável `horario_atual`).
- Estrutura de repetição (`while`) para verificar o horário e a presença de clientes.
- Uso de lista para representar a **fila de atendimento**.
- Simulação de chegada de clientes.

---

## Exemplo de execução:

**Fila de clientes do lado de fora:**  
["Cliente 1", "Cliente 2", "Cliente 3"]

**Horário inicial:**  

17 horas

**Saída esperada:**

Horário atual: 17h
Cliente 1 adicionado à fila de atendimento.

Horário atual: 18h
São 18h. Banco fechado pelo segurança.


---

## Motivação:

Este projeto foi desenvolvido como parte dos meus estudos de **Lógica de Programação**, dentro do curso **Coding Essentials – Logic Building for Beginners (Udemy)**.

Foquei em treinar:

- Controle de fluxo com base em tempo
- Condições encadeadas (`if...else`)
- Manipulação de filas (listas)

---

## Tecnologias usadas:

- Python 3.x

---

## Sobre mim:

Sou André Ricardo, estudante em transição de carreira para a área de Tecnologia da Informação.  
Atualmente focado em desenvolver habilidades em **Python**, **Lógica de Programação**, além de explorar **Inteligência Artificial** e **Hardware**.
