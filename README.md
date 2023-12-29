# Documento para a primeira avaliação
[Exercício - Avaliação primeiro App](https://docs.google.com/document/d/1YZgQtNitdb2HWEyY9F3xybii-mjl0Vf2DLhTlyCR1Cc/edit?usp=sharing)

# Código com a implementação dos scripts de testes
[ProjetoMobile](https://github.com/anielleCassiano/ProjetoMobile)

# Setup
* Instalar [Java v11 ou superior](https://www.oracle.com/br/java/technologies/javase/jdk11-archive-downloads.html)
* Instalar o [Android Studio](https://developer.android.com/studio?hl=pt-br)
  *  Como configurar o Android SDK, ADB, etc.. [Aqui!](https://appium.io/docs/en/2.3/quickstart/uiauto2-driver/)
* Instalar [NodeJs v20 ou superior](https://nodejs.org/en)
* Instalar [Python v10 ou superior](https://www.python.org/downloads/)
* Instalar o servidor Appium global
  * ```
    npm i -g appium
    ```
* Instale o driver UIAutomator2
  * ```
    appium driver install uiautomator2
    ```
* Clonar o repositório
  * ```
    git@github.com:anielleCassiano/ProjetoMobile.git
    ```
* Criar ambiente virtual
  * ```
    python -m venv .venv
    ```
* Executar
  * ```
    pip install -r /path/to/requirements.txt
    ```
* Iniciar o servidor appium
  * ```
    appium
    ```
* Rode os tests
  * ```
    python -m unintest
    ```
