# vpi
It is a tiny library for students of computation vision and image processing use in theirs exercises.

# VPI - Visão e Processamento de Imagens

VPI é um conjunto de modulos de Python desenvolvido como apoio as atividades práticas da disciplina MAC0471/MAC5768 - Visão e Processamento de Imagens (https://uspdigital.usp.br/janus/componente/catalogoDisciplinasInicial.jsf?action=3&sgldis=MAC5768). A VPI utiliza as bibliotecas Numpy (http://www.numpy.org/), Scipy (https://www.scipy.org/) e Pillow (https://pypi.python.org/pypi/Pillow) para fornecer as funcionalidades básicas de processamento de imagens. Varias funcionalidades da biblioteca VPI foram baseadas na implementação das funcionalidades do curso adessowiki (http://adessowiki.fee.unicamp.br/).

## Modulo io

O modulo io fornece funcionalidades de exibir e ler imagens.

* Leitura de imagens
    * **read_image(filename)**: lê imagem apartir do arquivo "filename"
    * **read_gray_image(filename)**: lê imagem apartir do arquivo "filename" e a converte para níveis de cinza
    * **read_binary_image(filename, thres = lambda g: g > 127)**: lê imagem apartir do arquivo "filename" e a converte para imagem binaria usanda a função de limiar thres
    * **pil2array(pil)**: converte imagem da biblioteca PIL para o ndarray do numpy.
* Exibição de imagens
    * **display_image(ima, width=None, height=None)**: exibe imagem no ipython notebook
    * **display_binary_image(ima, width=None, height=None)**: exibe binária imagem no ipython notebook 
* Armazenamento de imagem
    * **save_binary_image(filename, ima)**: Recebe um ndarray binário do numpy e salva um arquivo de imagem indicado por filename.

## Modulo binary_morphology

O Modulo binary_morphology possuí funções de morfologia matématica para imagens binárias, geramente os parâmetros que representam imagens (sempre binária) são chamados "f", e o elemento estruturante "b", o modulo binary_morphology consiste das seguintes funções:

* Criação de elementos estruturante:
    * **create_structure_element_disk(r=3)**: Função que cria um elemento estruturante em formato de disco com raio "r" (com uma    aproximação discreta do disco euclidiano).
    * **create_structure_element_cross(r=1)**: Função que cria um elemento estruturante em formato de cruz com tamanho "r" (cruz dilatado por uma cruz "r" vezes).
    * **create_structure_element_box(r=1)**: Função que cria um elemento estruturante em formato de caixa (quadrado) de lado "r".

* Funções úteis na criação de operadores morfologia
    * **sub_with_saturation(f1, f2)**: subtração de imagens binárias com saturação (mantém resultado entre 1 e 0).
    * **calculate_connected_components_area(f, conectivity=None)**: Calcula a área dos componentes conexos da imagem binária "f" utilizando a conexidade "conectivity". Quando a conectivity é None os componentes conexos são 4-conexos (conectivity = np.array([[0,1,0],[1,1,1],[0,1,0]])).
    * **neighbourhood_lut(s, offset)**: Função que calcula os vizinhos de todos os pixels de uma imagem com shape "s" por meio do "offset" (deslocamento em relação ao pixel, por exemplo, para 4-conexos offset consiste do vetor: [(-1,0), (0,-1), (1,0), (0,1)] e retorna uma lista onde cada linha representa um pixel e cada coluna a coordenada de um vizinho do pixel representado pela linha.

* Operadores Morfologicos: Note que as imagens resultates possuí o mesmo shape da imagem de entrada de maior shape, fazendo um corte na imagem o preenchendo a imagem com valores Falses.
   * **dilation(f, b=create_structure_element_cross(), iterations=1)**: dilata imagem binária "f" pelo elemento estruturante "b" por "iterations" vezes.
   * **erosion(f, b=create_structure_element_cross(), iterations=1)**: erode imagem binária "f" pelo elemento estruturante "b" por "iterations" vezes.
   * **opening(f, b=create_structure_element_cross())**: abertura da imagem binária "f" pelo elemento estruturante "b".
   * **closing(f, b=create_structure_element_cross())**: fechamento da imagem binária "f" pelo elemento estruturante "b".
   * **fill_holes(f, b=create_structure_element_cross())**: preechimento de buraco da imagem binária "f" pelo elemento estruturante "b".
   * **opening_top_hat(f, b=create_structure_element_cross())**: abertura top hat da imagem "f" pelo elemento estruturante "b".
   * **morphological_external_boundary(f, b=create_structure_element_cross())**: Calcula borda externa morfológica utilizando conectividade "b".
   * **morphological_internal_boundary(f, b=create_structure_element_cross())**: calcula borda interna morfológica utilizando conectivadade "b".
   * **morphological_gradient(f, b=create_structure_element_cross())**: calcula gradiente morfológica utilizando conectividade "b".
   * **area_opening(f, thres_area, conectivity=None)**: calcula abertura por área da imagem "f", pelo valor de limiar thres_area e conectividade "conectivity". Se conectivity for None, então é utilizado 4-conectividade (elemento estruturante cruz).
   * **inf_reconstruction(markers, f, bc=create_structure_element_cross())**: calcula inf-reconstrução dos marcadores "markers" da imagem "f" utilizando o elemento estruturante "bc".


## Modulo grayscale_morphology

O Modulo grayscale_morphology possuí funções de morfologia matématica para imagens em níveis de cinza, geramente os parâmetros que representam imagens (sempre em níves de cima) são chamados "f", e o elemento estruturante "b", o modulo grayscale_morphology consiste das seguites biblioteca.

* Operadores Morfologicos: Note que as imagens resultates possuí o mesmo shape da imagem de entrada de maior shape.

    * **dilation(f,b=create_structure_element_cross(), iterations=1)**: dilata imagem em níveis de cinza "f" pelo elemento estruturante "b" por "iterations" vezes.
    * **erosion(f,b=create_structure_element_cross(), iterations=1)**: Erode imagem em níveis de cinza "f" pelo elemento estruturante "b" por "iterations" vezes.
    * **opening(f, b=create_structure_element_cross())**: Abertura da imagem em nível de cinza "f" pelo elemento estruturante "b". 
    * **closing(f, b=create_structure_element_cross())**: Fechamento da imagem em nível de cinza "f" pelo elemento estruturante "b".
    * **opening_top_hat(f, b=create_structure_element_cross())**: Abertura top hat da imagem "f" pelo elemento estruturante "b".
    * **closing_top_hat(f, b=create_structure_element_cross())**: Fechamento top hat da imagem "f" pelo elemento estruturante "b".
    * **morphological_external_boundary(f, b=create_structure_element_cross())**: Calcula a borda externa morfólogica utilizando a conectividade "b".
    * **morphological_internal_boundary(f, b=create_structure_element_cross())**: Calcula a borda interna morfológica utilizando a conectividade "b".
    * **morphological_gradient(f, b=create_structure_element_cross())**: Calcula gradiente morfológico utilizando conectividade "b".
    * **inf_reconstruction(markers, f, bc=create_structure_element_cross())**: Calcula inf-reconstrução dos marcadores "markers" da imagem "f" utilizando o elemento estruturante "bc"  
    
    
    
forked from https://github.com/dennisjosesilva/vpi/
