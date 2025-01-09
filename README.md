# Locadora de Veículos
Este software que eu desenvolvi ele tem o intuito de catalogar carros e o aluguel desses carros 

- Ao inicia-lo você será capaz de definir um nome a locadora
- Após definir o nome da locadora você, sera apresentado um menu com as seguintes opções

(1) Veículos
(2) Clientes
(3) Mudar o nome da locadora
(4) Alugar
(0) Sair e Salvar

## Ao acessar o menu de Veículos vão aparecer as opções:

(1) Adicionar veículos

- Ao adicionar veiculos inputs vão aparecer para colocar cada carácteristica do veículo que deseja adicionar e deposita esse veículo em uma lista através de 
locadora.add_veiculos(veiculo).

**Fique atento ao adicionar veículos para selecionar o tipo certo de veículo (carro ou moto), pois caso o contrário a adição do veículo será cancelada.**

(2) Listar veículos

- Acessar a opção listar veículos lista os veículos através da função locadora.listar_veiculos() que acessa a lista de veículos e mostra eles através da função 
mostrar_veiculo.

(3) Remover veículos

- Remove veículos ao chamar a lista de veículos com listar_veiculos() e seleciona um número da lista através da função listar_veiculos(select=True) tirando o veículo da lista através de .pop().

(4) Editar veículos

- Edita os veículos com o método editar_veiculos que lista os veiculos e seleciona o número do veículo através de listar_veiculos(select=True) e após isso mostra
todos os atributos da classe veículos e apresenta um input para selecionar o atributo e muda-lo.

**Alguns atributos não podem ser mudados, pois poderiam causar erros, o atributo da classe veiculos que não pode ser mudado é tipo.**

### Ao acessar o menu de Clientes vão aparecer as opções:

(1) Adicionar clientes

- Ao adicionar clientes como em veículos inputs vão aparecer para colocar cada carácteristica do cliente que deseja adicionar e deposita esse cliente em uma lista 
através de locadora.add_clientes(cliente).

**Atenção para colocar 11 digitos no telefone.**

(2) Listar clientes

- Acessar a opção listar clientes lista os clientes através da função locadora.listar_clientes() que acessa a lista de clientes e mostra eles através da função 
mostrar_clientes.

(3) Remover clientes

- Remove clientes ao chamar a lista de clientes com listar_clientes() e seleciona um número da lista através da função listar_clientes(select=True) tirando o cliente da lista através de .pop().

(4) Editar clientes

-Edita os clientes com o método editar_clientes que lista os clientes e seleciona o número do cliente através de listar_veiculos(select=True) e após isso mostra
todos os atributos da classe clientes e apresenta um input para selecionar o atributo e muda-lo.

**Alguns atributos não podem ser mudados, pois poderiam causar erros, os atributo da classe clientes que não pode ser mudado é *veiculo alugado e data de devolução.**

Ao acessar o menu de Alugar vão aparecer as seguinte opções:

(1) Alugar veículo

-Mostra a lista de clientes cadastrado e de veiculos, selecionar o cliente e o veículo faz com que o software peça a quantidade de dias que o veículo vai ser alugado e calcula o valor total e pergunta se você concorda em alugar o carro, após esse processo o veículo é atribuido ao cliente e subtraido da quantidade. Ao acessar listar clientes será possível visualizar os veículos alugados e as datas de devolução para determindo cliente.

**Veículos que possuem a quantidade=0 vão aparecer como "Todos os veículos deste modelo estão alugados." no atributo de quantidade e não poderam ser alugados.**

**Veículos possuem datas de devolução e caso esteja na data da devolução ou tenha passado dela será exibido "Hoje" ou "Data de devolução passou" respectivamente.**

(2) Devolver veiculo

-Mostra a lista de clientes e de veículos alugados (caso o cliente tenha alugado algum veículo) e pede para selecionar o veículo que deseja devolver adicionando a quantidade do veículo devolta e retirando o veículo da lista de veículos alugados pelo cliente.

**O software é salvo automáticamente ao sair e é carregado ao entrar devolta nele.**
