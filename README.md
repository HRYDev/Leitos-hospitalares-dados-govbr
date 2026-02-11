# Leitos-hospitalares-dados-govbr
O sistema foi desenvolvido para exibição de informações sobre leitos hospitalares, tem como principal objetivo coleta e no processamento de dados a respeito do tema, de fontes oficiais. Trabalho faculdade realizado em grupo de 5 pessoas em 2025.

Dissertação:

Desenvolvimento de um sistema para monitoramento de leitos hospitalares com base em dados abertos

tópico 1 - Funcionamento do sistema para exibição de informações sobre leitos:
O sistema foi desenvolvido para exibição de informações sobre leitos hospitalares, tem como principal objetivo coleta e no processamento de dados a respeito do tema, de fontes oficiais. A origem, utilidade e a atualidade desses dados são detalhadas a seguir.

Origem e utilidade dos dados:
A base de dados do sistema é composta por informações públicas disponibilizadas por órgãos do Governo Federal. A principal fonte de coleta é o portal https://dados.gov.br/home (Site do Governo Federal Brasileiro), que consolida conjuntos de dados abertos de diversas áreas, incluindo a saúde. Especificamente, foram utilizados os diretórios referentes ao tema escolhido, leitos hospitalares.
Complementarmente, foi integrada ao sistema de leitos os dados da API de Dados Abertos do Ministério da Saúde, gerenciada pelo DEMAS (Departamento de Monitoramento, Avaliação e Disseminação de Informações Estratégicas em Saúde). O acesso a essa API, disponível no endereço https://apidadosabertos.saude.gov.br/ contribuiu para o sistema, com informações necessárias para o desenvolvimento do script.

[‘’ foi utilizado para contribuir para o script. O diretório disponível em: https://apidadosabertos.saude.gov.br/v1/#/Assistência%20à%20Saúde/get_assistencia_a_saude_hospitais_e_leitos ‘’]

 É crucial destacar que, para manter o foco e a relevância regional ampla, o foco da coleta foi expandido, dados coletados de leitos localizados em diferentes regiões pelo país.

Atualidade dos dados:
Quanto à atualidade das informações, os conjuntos de dados utilizados são atuais e atualizados diretamente pelas fontes oficiais. Tanto o portal dados.gov.br quanto a API do Ministério da Saúde (também disponível através do portal dados gov br) do fornecem de forma explicita, as datas da última atualização. O que garante a confiabilidade temporal dos dados. Dessa forma, o sistema é capaz de exibir as informações mais recentes disponibilizadas pelos órgãos oficiais no momento da consulta, exibindo o catálogo mais atual possível, de disponibilidade de leitos e outras informações usadas a respeito do tema. Para o desenvolvimento e testes deste script, foram utilizados os conjuntos de dados mais recentes disponíveis no período de desenvolvimento do script, referentes ao ano.

[“Acessando o site Gov.br dados, ao pesquisar por leitos, é possível visualizar catálogos dos resultados exibidos – ficando visível as datas exatas das últimas atualizações. Todos os dados utilizados no script desenvolvido são de 2024 a 2025 adiante.’’]

Como os dados sobre leitos são exibidos no sistema:
A interface de exibição das informações foi projetada priorizando a clareza na busca e a organização dos dados para o usuário final. Em vez de apresentar todas as informações de uma vez em uma tabela ou lista, o sistema adota uma estrutura de menu expansível e visualização de gráficos.

Nessa primeira interface, a primeira que o usuário verá assim que acessar, as opções de visualização são organizadas em um menu ordenado, onde cada item representa uma informação a respeito do “status” geral do leito. Inicialmente, o usuário visualiza apenas os títulos das categorias principais (por exemplo, o nome do tipo de leito). Para acessar os detalhes completos, o usuário deve interagir com o item desejado, clicando sobre ele para expandir o tópico e revelar as informações desejadas.

A visualização em Menu é uma opção comum e frequentemente a mais adequada para exibir conjuntos de dados como leitos hospitalares, exatamente porque estes dados são categóricos e estruturados de forma individual (cada categoria uma informação isolada), se assemelhando a uma lista de opções. Em desvantagem, o menu expansível não é muito dinâmico, sendo em contrapartida limitado as informações somente relacionadas ao tópico escolhido ou pesquisado, também os dados por não ficarem expostos, o usuário já deve ter em mente uma ideia mínima da informação que deseja visualizar.

A Visualização em gráficos no contexto dados de leitos:

Enquanto gráficos (como barras ou pizzas) são muito mais específicos para fornecer uma visão geral e visual (ex.: número total de leitos por região, desenhada no gráfico de pizza). Dinâmicos visualmente exibindo conteúdo complexos de forma simples, a visualização em gráfico se torna extremamente rápida, mesmo para conjuntos de dados muito grandes, uma vantagem crítica sobre ferramentas de planilhas. Um script que gera gráficos com essas bibliotecas é totalmente ajustável. se os dados de origem forem atualizados, basta executar o script novamente para gerar todos os gráficos atualizados, assim como gráficos de barras para comparações entre várias categorias relacionadas como o status dos leitos.
Porém, diferentemente de um número exato, gráficos estão sujeitos à interpretação subjetiva do usuário, sem títulos claros ou legendas exibidas, o significado pode ser facilmente distorcido.

[“Um menu, semelhante a uma lista, onde de forma ordenada as informações estão organizadas contidas dentro de cada tópico fechado, onde o usuário precisa acessar uma informação por vez para acessar os dados. Também com implementação e auxílio visual dos gráficos como resultado do script”]

Tópico 2 - Principais categorias de leitos do script:
O script apresenta dados organizados em categorias específicas, que permitem ao usuário acessar informações relacionadas à leitos. Serão apresentadas categorias a seguir:

Leitos regulares e leitos SUS:
O usuário encontra presente no script dados organizados em gráficos detalhando a disponibilidades de leitos por região. As informações são compiladas a partir dos dados abertos do Ministério da Saúde e podem incluir:

Filtragem por Região: Permitindo que o usuário visualize de forma ampla os dados, classificados especificamente por região de impacto. De acordo com os dados exibidos, é o número total de leitos existentes, oferecendo uma visão geral do cenário atual.

O gráfico de barras revela com clareza as profundas desigualdades regionais na distribuição e no tipo de leitos de saúde regulares e SUS:

 
Sudeste e Nordeste se destacam com os maiores números absolutos de leitos, tanto regulares (privados) quanto SUS. O Sudeste lidera com folga em leitos privados, refletindo sua concentração econômica. Já o Nordeste apresenta uma quantidade expressiva e com uma divisão relativamente equilibrada entre os leitos regulares e SUS, indicando uma infraestrutura mais mista.
Sul e Centro-Oeste possuem perfis intermediários. O Sul tem uma base sólida de leitos, enquanto o Centro-Oeste, apesar do menor número absoluto total, mostra uma presença notável de leitos privados em relação ao número de leitos SUS.
A Região Norte é a mais escassa, com os menores números absolutos de leitos totais, a diferença para as outras regiões é abismal, evidenciando uma grave carência de infraestrutura de saúde como um todo.


Distribuição Geográfica dos Leitos: Gráfico script
O gráfico a seguir demonstra visualmente as distribuições de leitos SUS por região, evidenciando uma desigualdade regional:

 

Região Sudeste: possui a maior quantidade de leitos do SUS, com 36.1k leitos, o que corresponde à maior fatia do gráfico. No entanto, em números absolutos, o SUS no Sudeste é o maior do país, atendendo a uma população enorme. Essa quantidade reflete a região mais populosa do país, com alta concentração populacional e grandes metrópoles, no entanto, podem gerar uma demanda massiva por serviços de saúde, que pode não ser atendida mesmo com o maior número de leitos.

Região Nordeste: é a segunda região com mais leitos do SUS, totalizando 30.5k. Que representa a segunda maior fatia da distribuição nacional, atrás apenas do Sudeste. Essa quantidade é fundamental para a região, que historicamente sempre enfrenta desafios e desigualdades no acesso a serviços.

Região Sul: apresenta a terceira maior quantidade de leitos, com 16.3k. Região que possui uma quantidade intermediária em relação ao resto do país. A região Sul e Sudeste, juntas, concentram quase a maioria dos leitos hospitalares do Brasil.
Região Norte: possui a segunda menor quantidade de leitos, com 8.6k. Que vive uma situação de maior fragilidade e atenção à saúde, com dificuldades logísticas e acesso a populações em áreas remotas.
Região Centro-Oeste: possui a menor quantidade de leitos do SUS, com 8.5k. o menor número de leitos SUS, com essa minoria, em um território vasto e com cidades dispersas, pode representar um desafio para a logística e acesso à saúde em áreas especificas.

Quantidade de pessoas na fila de leitos:
Esta categoria mapeia a demanda (visualizando dados script) e apresenta uma aproximação das filas de espera por leitos, geralmente em tempo próximo do real (dependente da atualização do banco de dados Gov.br). A vantagem da informação desses dados é operacional e prática, permitindo que isso ajude os profissionais da saúde na tomada de decisões, como a redistribuição de pacientes entre hospitais ou o acionamento de leitos extras em situações de alta demanda.

Veja a seguir a imagem explicativa sobre o processo de acesso a uma vaga de leito:

 [referencias: https://saude.rs.gov.br/regulacao-hospitalar - Secretaria da saúde Gov RS]
Ponto de origem começa com um paciente que precisa de internação. Isso pode acontecer em um pronto-socorro, uma consulta ambulatorial, ou via transferência de uma unidade de saúde menor. A necessidade de um leito hospitalar (seja clínico, cirúrgico ou UTI) é registrado no sistema interno do hospital, caso um hospital tenha um leito disponível, o paciente é internado diretamente na unidade. A fila começa quando não há leitos disponíveis no local.
Ao visualizar o volume de pessoas aguardando por um leito, é feita a redistribuição dos pacientes entre hospitais da mesma região, balanceando a carga (internados) e reduzindo tempos de espera. Enquanto o paciente não é alocado, o nome do paciente permanece na lista de espera, é essa lista, compilada a partir de centenas de hospitais, que alimenta o banco de dados governamental que o script desenvolvido acessa.

Leitos ocupados:
Há um paciente clinicamente instalado no leito, ou seja, o processo de internação foi formalizado no sistema do hospital e os recursos, equipe médica, medicamentos, equipamentos estão sendo dedicados a esse paciente. Atualização desses casos seriam como nessa exemplificação, dados de entrada e saída, atualizados constantemente: Fluxo Contínuo: Leito VAGO → Leito OCUPADO → Leito VAGO. Leitos ocupados interferem diretamente com outras categorias, como aumento na quantidade de pessoas na fila e leitos disponíveis.

´´As análises a seguir mostram os resultados dos indicadores de
gestão operacional para esse grupo de hospitais entre 2021 e 2024
(Tabela 1). Esses indicadores foram calculados com base em uma
amostra de 65 instituições respondentes no Sistema de Indicadores
Hospitalares Anahp em 2024´´

 [referências: https://www.anahp.com.br/publicacoes “Observatório Anahp 2025 pag 183”]

A taxa de ocupação se mostra crescente, como mostra a tabela, aumentando de forma constante, o que pode indicar uma maior demanda por serviços hospitalares nesses últimos anos, especificamente em redes privadas, como indica a pesquisa Anahp 2025.

Leitos indisponíveis:
É o leito que habitualmente é utilizado para internação, mas que por qualquer razão não pode ser utilizado por questões internas do hospital, sejam consequentes por; manutenção, equipamentos, profissionais, infraestrutura. Isso é um problema comum no SUS e afeta a capacidade real de atendimento. 

Leitos sem estrutura representam uma lacuna entre a capacidade cadastral e a capacidade operacional do sistema de saúde. Observando outra exemplificação: o sistema mostra 100 leitos cadastrados, porém apenas 85 estão realmente disponíveis, o restante está indisponível. Logo o sistema atrasado em atualização de leitos realmente disponíveis; gestores hospitalares tomam decisões com análise de dados distorcidos: 15 leitos sem estrutura → 15 pacientes não atendidos por dia → Aumento direto no tempo de espera na fila.

Veja a terceira exemplificação, em relação a leitos contabilizados como disponíveis e bloqueados na instalação hospitalar local:

´´TAXA DE LEITOS-DIA BLOQUEADOS (TLDB) 
É o percentual de leitos-dia bloqueados em relação à capacidade instalada (referente aos leitos instalados). Indica o bloqueio de leitos por clínica e institucional. 
TLDB = (nº de leitos-dia bloqueados / (nº de leitos instalados x nº dias do mês)) x 100´´
[referencias: http://www.nih.saude.sp.gov.br/downloads/glossario_202005.pdf Glossário de Conceitos Núcleo de Informação Hospitalar]

A visualização de tais dados, se torna necessária para que gestores possam tomar decisões baseadas na capacidade real versus capacidade teórica, impactando diretamente na eficiência do sistema e na qualidade do atendimento.

Taxa de mortalidade hospitalar:
É um indicador que mede a proporção de óbitos em relação ao total de pacientes que saíram do hospital, casos relacionados a perfis de pacientes mais críticos, comorbidades, população mais idosa, cirurgias complexas e complicações clínicas.

Esses dados impactam diretamente na qualidade do serviço de saúde, além do registro de óbito, contribuem com vários tópicos relacionados, uma piora na qualidade do cuidado, infecção hospitalar, falhas em equipamentos ou agilizando a investigação dos casos de óbitos.

´´A qualidade dos dados é fundamental para garantir a validade do indicador. Duas fontes de dados principais são utilizadas nos estudos sobre mortalidade hospitalar: as bases de dados administrativos e os prontuários médicos. As análises da mortalidade hospitalar que se utilizam de bases de dados administrativos partem do pressuposto de que os hospitais utilizam procedimentos padronizados de coleta, codificação, definição de terminologia, classificação e nomenclatura para produzir essas informações. Mas raramente isto realmente acontece. Pode ocorrer grande variação na qualidade dos dados entre hospitais, afetando substancialmente os estudos comparativos (OTA, 1988). A produção de dados confiáveis exige padronização e atualização, o que implica em esforço apropriado e permanente para a melhoria da qualidade dos dados´´
[fonte: Artigo - Mortalidade hospitalar como indicador de qualidade: uma revisão disponível: https://www.scielo.br/j/csc/a/wb9RrKwXBLwFXtWgPWMrrZB/?lang=pt ]

Quantidade e adequação de itens nos leitos:
A quantidade de itens em leitos é a contagem dos elementos; equipamentos, insumos e recursos humanos. Todos os equipamentos, materiais e suprimentos necessários para que um leito hospitalar funcione adequadamente. A monitora desses dados ajuda a identificar e melhorar a alocação de recursos e resolução de problemas internos, assim ligado à qualidade e segurança do paciente. Os hospitais precisam garantir que os pacientes tenham à disposição todos os equipamentos e materiais para um tratamento seguro de qualidade, já que a falta de um item essencial pode levar a eventos adversos, impactando inclusive as taxas de mortalidade. 

Por meio de regulamentações, ANVISA com RDC Nº 7/2010, estabelece requisitos mínimos para a infraestrutura, equipamentos e materiais necessários em diferentes tipos de unidades e leitos:

´´A segurança do paciente diz respeito ao direito de toda pessoa receber cuidados de saúde sem sofrer danos evitáveis. Isso significa que os serviços de saúde devem estar organizados para prevenir falhas, identificar riscos com antecedência e corrigir problemas de forma rápida e eficaz´´ [Site Ministério da Saúde, disponível em: https://www.gov.br/saude/pt-br/composicao/saes/seguranca-do-paciente]

UTIs por tipo (adulto / pediátrico / neonatal)

A presença de UTIs de tipos específicos determina a capacidade de acolhimento para diferentes demandas clínicas: gestação de alto risco e mortalidade neonatal dependem de neonatologia; emergências pediátricas exigem UTIs pediátricas; epidemias respiratórias elevam demanda por UTIs adultas. Contar apenas “leitos gerais”, mascara essas diferenças. Um hospital com muitos leitos regulares pode não ter UTIs separadas para cada caso, a ausência delas correlaciona maior risco de mortalidade por condições dependentes dessas especificações. 

UTI pediátrica e neonatal:
A manutenção dessas unidades exige uma especialização ainda maior da equipe (médicos intensivistas pediátricos e neonatologistas, enfermeiros especializados) e equipamentos de alta precisão, o que as torna complexas e custosas. Essa disparidade gera um problema grave: uma criança ou um recém-nascido grave em uma cidade do interior muitas vezes precisa ser transferida para longe de sua família, em um processo complexo e arriscado chamado de "regulação". A escassez é ainda mais crítica para leitos pediátricos, que ficam em um "meio-termo" entre o neonatal e o adulto, mas com necessidades absolutamente específicas.

´´A unidade de terapia intensiva pediátrica (UTIP) é onde os enfermeiros prestam cuidados a crianças gravemente doentes ou feridas. Já a unidade de terapia intensiva neonatal (UTIN) cuida de bebês prematuros ou recém-nascidos com problemas de saúde para que tenham um início saudável´´
[referencias:https://www.intelycare.com/career-advice/picu-vs-nicu-whats-the-difference - site IntelyCare]

UTI adulto:
Numerosos e cheios, a demanda por esses leitos é constante e abrange um espectro enorme de condições, desde complicações de doenças crônicas até acidentes e cirurgias complexas. O perfil padrão da população adulta, somado ao envelhecimento da população, faz com que seja a área com a maior pressão por vagas.

Acesso leitos em UTIs privadas e públicas
A disponibilidade de um leito de UTI, determinada muitas vezes pela gravidade clínica do paciente e pelo seu vínculo com o sistema de saúde, seja ele público ou privado. Em tempos de crise, não é um colapso "geral" de leitos. É, na verdade, um colapso seletivo do SUS. Enquanto os hospitais privados podem ainda ter vagas, a fila única do SUS, que centraliza a regulação de todos os pacientes não vinculados à rede privada, entra em paralisia. Manter uma rede robusta de leitos SUS não é investimento em resiliência sanitária e em soberania do acesso à saúde para a população.

´´Para o presidente do CFM, José Hiran Gallo, a diminuição no número de leitos de internação do Sistema Único de Saúde (SUS) em meio ao crescimento da população, que passou de 190 milhões, em 2010, para 203 milhões, em 2023, não é uma boa notícia para os brasileiros. A análise feita pelo CFM mostra que, entre 2010 e 2019, a queda do número de leitos de internação do SUS foi contínua e acentuada. Só houve aumento em 2020, primeiro ano da pandemia. Porém, desde então, o número vem caindo novamente. - “Vinte e cinco mil leitos a menos é um dado alarmante. Não tenha dúvida de que muitas pessoas, lá na ponta do sistema, serão prejudicadas por isso. Nas capitais, muitas vezes, encontramos hospitais públicos cheios, com gente espalhada pelo corredor sem ter acesso a um leito. É disso que estamos tratando aqui”, afirmou José Hiran Gallo´´

 
[referencias: CFM Portal conselho federal de medicina - https://portal.cfm.org.br/noticias/em-13-anos-brasil-perde-25-mil-leitos-de-internacao-do-sus]

Participação do SUS por estabelecimento hospitalar
Revela de estabelecimento a estabelecimento, quanto da oferta a leito está efetivamente disponível ao público via SUS. Um tema central para a compreensão da rede de comunicação públicas e hospitalares. Essa aliança é essencial para suprir a demanda por serviços, especialmente os de média e alta complexidade, que não podem ser inteiramente cobertos pela rede própria do governo.

Hospitais públicos:
Gestão estatal de hospitais geridos por esferas federais, estaduais ou municipais, com financiamento e administração públicos, muitos hospitais públicos, como os universitários, são centros de ensino e pesquisa, contribuindo para a formação de profissionais de saúde.

Hospitais privados:
A Constituição Federal e a LEI Nº 8.080 prevê que a iniciativa privada pode atuar de forma complementar no SUS, quando a rede pública não é suficiente para atender a demanda. Essa participação é formalizada por meio de contratos, obedecendo às normas de direito público e priorizando hospitais filantrópicos.
´´O presente artigo teve como ponto de partida os dispositivos constitucionais que tratam da participação de instituições privadas de forma complementar no Sistema Único de Saúde e os artigos 24 a 26 da Lei nº 8.080/90, que traçam as diretrizes gerais sobre a matéria, com o objetivo de apresentar as possibilidade, exigências e vedações legais gerais a serem observadas pelos gestores do SUS na solução das insuficiências verificadas nas redes públicas de saúde. ´´
[referências: Site Presidência da República Casa Civil - https://www.planalto.gov.br/ccivil_03/leis/l8080.htm e PDF Tribunal de Contas do Estado de São Paulo - https://share.google/1kzDzVhBd0vS1rJfH ]

Hospitais filantrópicos:
Instituições privadas sem fins lucrativos, muitas vezes sendo os únicos hospitais disponíveis em municípios menores. A colaboração com o SUS se dá por meio de contratos ou convênios de direito público. Veja a citação de 2024, noticiando que milhares de unidades filantrópicas prestam serviços ao SUS;

´´Essas entidades são de direito privado, porém sem fins lucrativos, e prestam grandes serviços aos 900 municípios brasileiros que não são atendidos por nenhuma esfera governamental na saúde e na educação, segundo dados do Fórum Nacional das Instituições Filantrópicas (FONIF)´´
[referências: FBH federação brasileira de hospitais - https://fbh.com.br/o-papel-das-instituicoes-filantropicas-na-transformacao-da-saude-no-pais.]

tópico 3: Código e funcionalidades script

Aplicação arquivos JSON para: os, Matplotlib pyplot, Numpy e Pandas:
O script realiza uma análise de dados sobre a disponibilidade de leitos hospitalares no Brasil, diferenciando entre leitos regulares e do SUS e exibe os resultados em gráficos. 
Processamento dos dados implementados com OS e Pandas arquivo JSON
A biblioteca OS abre a interação com o sistema operacional limpando o terminal e manipulando os caminhos de arquivos.
A biblioteca JSON é usada para trabalhar com dados no formato JSON, que é uma forma de armazenar e transmitir dados.
A biblioteca Pandas analisa e manipulação de dados em Python. No código, ele é usado para organização e o acesso aos dados coletados.

Depois de ter todos os dados organizados, temos informações de algumas perguntas importantes:
•	Quais hospitais das regiões Norte, Sul, Sudeste, Nordeste e Centro Oeste tem mais UTIs? O script analisa os hospitais e calcula o total de UTIs de cada um e informa qual é o maior.
•	Qual hospital tem a maior diferença entre leitos regulares e SUS? O script calcula a diferença entre os dois tipos de leitos para todos os hospitais e encontra aquele com a maior diferença.
•	Qual hospital tem a maior capacidade total de leitos? O script soma todos os leitos de cada hospital e identifica o que tem a maior capacidade do país.
•	Qual hospital tem a maior capacidade total de leitos? O script soma todos os leitos de cada hospital e identifica o que tem a maior capacidade do país.

Exibição dos dados com Matplotlib e Numpy
Numpy é usado para gerar arrays de valores numéricos que servem como posições para as barras nos gráficos. Isso é mais eficiente do que usar listas Python para a mesma tarefa
Matplotlib cria visualizações estáticas, animadas e interativas em Python, também é possível adiciona títulos, rótulos e legendas.

O gráfico de barras gerado compara a quantidade de leitos regulares e leitos SUS em cada região. É fácil ver a diferença entre os dois tipos de leitos em cada parte do Brasil. Já o gráfico de pizza é criado para mostrar a quantidade total de leitos do SUS está distribuída entre as regiões. Os arquivos podem ser salvos como imagens, se solicitado salva também a tabela completa de dados em um arquivo de texto. 

Encerramento:
Em resumo, o script automatiza uma tarefa de pesquisa e visualização de dados, transformando uma grande quantidade de informações em resumos e gráficos fáceis de entender.

A utilidade de tais dados no sistema é múltipla: permitem mapear disponibilidade física de vagas, identificar desigualdades territoriais, quantificar participação do SUS em diferentes estabelecimentos e tipos de UTI, e gerar insumos para modelagens de contingência (por exemplo, cenários de aumento de demanda). Entretanto, convém enfatizar que os valores correspondem principalmente à infraestrutura declarada — a conversão desses leitos em atendimento efetivo depende de fatores operacionais (dotação de pessoal, insumos, habilitação de leitos) que complementam, mas não substituem, o inventário. Esses arquivos são tratados aqui como estimativas referentes ao período 2024–2025; ou seja, constituem um retrato administrativo recente, mas sujeito a atualizações institucionais e a diferenças entre capacidade nominal e capacidade efetivamente operada.

