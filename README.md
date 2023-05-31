# Devasc_Skills

naam: Lander Mertens

Klas: 2SNEa

Beschrijving en resultaten van Lab 1-7.

Lab1

1.1	Install different tools/packages on Ubuntu DEVASC-LABVM:

Uitleg: het instaleren van de tools op de DEVASC-LABVM

- Task preparation and implementation:
  - DEVASC-LABVM 
- Task troubleshooting:
  - Tijdens het instaleren van de Jupyter noteBook kreeg ik een error. Heb dit opgelost door pip install markupsafe==2  te gebruiken
- Task verification:
  - Jupyter NoteBook  = Lab1\notebook_DEVASC_LABVM.png
  - Visual studio code = Lab1\VSC_DEVASC_LABVM.png
  - Python IDLE = Lab1\IDLE_DEVASC_LABVM.png
  - Python 3.8 and PIP = Lab1\Python _LABVM.png

1.2	Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (1.1):

Uitleg: Het runnen van de scripts met de nieuw gedownloade tools op je DEVASC_LABVM
 
- Task preparation and implementation:
  -Visual studio code
  - scripts downloaden van https://github.com/wleppens/PythonExperiments
- Task troubleshooting:
  - In  Visual studio code kreeg ik een error maar na de commands pip install geopy en pip install folium in te geven niet meer.
- Task verification:
  - Voorbeeld dat de scripts werken = Lab1/1.2_voorbeeld.png 

1.3	Install different tools/packages on Windows OS (deep dive exercise) ++

Uitleg: het instaleren van de tools op een Windows device

- Task preparation and implementation:
  - een Windows device   

- Task troubleshooting:
- Task verification:
  - python3 = Lab1/python3_windows.png
  - Visual studio code =Lab1/VSC_windows.png
  - pythons IDLE= Lab1/idle_Windows.png
  - Jupyter NoteBook = Lab1/notebook_windows.png

1.4	Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++

Uitleg: het instaleren van de tools op een Ubuntu 20.04.01 machine.

- Task preparation and implementation:
  - ubuntu22.04.01 virtuele machine 
- Task troubleshooting:
  - De terminal wou niet openen dus heb ik in de Ubuntu software app de app Terminator gedownload en het werkte terug 
  - Je wordt root door de commando su -
  - Jupyter notebook geïnstalleerd via de website: https://linuxhint.com/install-jupyter-notebook-on-ubuntu-20-04/
- Task verification:
  - Python 3 = Lab1/python3_ubuntu.png
  - PIP = Lab1/pip_ubuntu.png 
  - Visual studio code = Lab1/VSC_ubuntu.png
  - Jupyter notebook = Lab1/notebook_ubuntu.png


Lab2

Part 2 :Explore API Documentation Using the API Simulator

Uitleg:  Het maken van REST API’s aan de hand van de API-documentatie.

- Task preparation and implementation:
  - DEVASC-LABVM 
  - Chromium Web Browser (automatisch aanwezig op de DEVASC-LABVM)
- Task troubleshooting: 
  - Geen problemen tegen gekomen.
- Task verification:
  - Get command = Lab2/Get_command.png
  - token aanmaken = Lab2/Token.png
  - post command = Lab2/Post_command.png
  - Get command met parameters = Lab2/Get_command_parameters.png
  - Delete command = Lab2/Delete_command.png

Part 3 :Use Postman to Make API Calls to the API Simulator

uitleg:   Het maken van API calls met Postman.

- task preparation and implementation:
  - DEVASC-LABVM
  - Postman (aanwezig op de DEVASC-LABVM)
- Task troubleshooting:
- Task verification:
  - Get command zonder parameters =Lab2/Get_command_postman.png
  - Token maken via postman = Lab2/token_postman.png
  - Get command met parameters = Lab2/Get_command_parameters_postman.png

Part 4 :Use Python to Add 100 Books to the API Simulator

Uitleg : Het toevoegen van 100 boeken via een python script met gebruik van de Python faker library

- Task preparation and implementation:
  - DEVASC-LABVM
  - Visual stuio code (aanwezig op de DEVASC-LABVM)
- Task troubleshooting:
  - Tijdens het runnen van het python script gaf het script een foutmelding. Dit kwam omdat ik de Faker library niet had toegevoegd. Dit doe je door pip install faker in te geven in je terminal.
- Task verification:
  - Combinatie van de faker labrary = Lab2/Faker_Part4_step3.py + Lab2/Faker_resultaat.png
  - Add 100 RandomBooks = Lab2/add100RandomBooks.py  +  Lab2/Books100.png
  - Add 100 new books = Lab2/addNewBooks.png

Lab3

Uitleg: Uitleg over de basis commands en de belangrijkste commands van Python

Part 1 :

- Document your findings and important commands.
- commands
  - type(”…”)
  - Lists= [“..”,”...”,”..”]
  - input= input(“wat je wil weten”)
  - file=open("devices.txt","r") 
  - gelijk is == en niet =
- results
  - personal-info = Lab3/personal-info.py
  - if-vlan= Lab3/if-vlan.py
  - if-acl=Lab3/if-acl.py
  - while-loop = Lab3/while-loop.py
  - file-access = Lab3/file-access.py
  - file-access-input= Lab3/ file-access-input

Part 2 :

- Document your findings and important commands.
  - environment aanmaken : python3 -m venv defun
  - environment starten: source devfun/bin/activate
  - environment stoppen: deactivate
  - voor python te kunnen gebruiken in je environment : pip3 install requests
  - Je packages wegschijven zo dat deze kunnen gebruikt worden in een ander environment= pip3 freeze > requirements.txt

Part 3 :

- Document your findings and important commands.
  - Een functie is een stukje code dat je apart zet omdat je dit veel gebruikt. Een class wordt aan gestuurd via methodes.
  - wel goed opletten met de inspringen. 
- Results:
  - myCity = Lab3/myCity.py
  - myLocation =Lab3/myLocation.py
  - circleClass = Lab3/circleClass.py

Lab4

Uitleg: het configureer van de switch en de router zo dat deze kunnen connecteren met de FTP-server. Uitzoeken hoe je rap een restore uitvoert.

- Task preparation and implementation:
  - Netwerkplan = Lab4/PE4.nvdx
  - switch config = Lab4/LAB-A07-A-SW03
  - router config = Lab4/LAB-A07-A-R03
  - FTP_restore = Lab4/FTP_restore.txt
- Task troubleshooting:
  - De ssh functie wil niet altijd op mijn switch werken en wel op mijn router. Na opzoekingswerk de fout nog niet gevonden. Ook na aanpassing van de ssh versie geen verschil.
- Task verification:
  - Staat op de ftp server.

Lab5

Uitleg: het werken met github, het maken van Unit-tests en het werken met andere data vormen

- Task preparation and implementation:
  - DEVASC-LABVM
  - Visual stuio code (aanwezig op de DEVASC-LABVM)
  - github
- Task troubleshooting:
  - Met het verbinden van de github repository krijg ik een foutmelding. Dit kon ik oplossen door een Authentication key te laten generen.
- Task verification:
  - File met screenshots over 3.3.11 = 3.3.11
  - File met screenshots over 3.5.7 = 3.5.7
  - File met screenshots over 3.6.6 = 3.6.6

Lab6

Uitleg: Netmiko scirpts maken aan de hand van commands op single IOS device en multiple IOS devices

- Task preparation and implementation:
  - Lab4 (de router en de switches)
  - DEVASC-LABVM
  - Visual studio code (aanwezig op de DEVASC-LABVM)
- Task troubleshooting:
  - Ik had de fout gemaakt door geen paswoord op mijn machines te zetten waardoor ik geen connectie kon maken. Ook doet mijn switches soms moeilijk met de SSH connectie/
- Task verification:
  - Sending single show command = Lab6/Send_multiple_configuration_commands.py
  - Sending multiple show commands = Lab6/Send_multiple_show_commands.py
  - Send multiple configuration commands to a single device = Lab6/Send_single_show_command.py
  - Send show commands to multiple devices = Lab6/Send_show_commands_to_multiple_device.py
  - Send configuration commands to multiple devices = Lab6/Send_configuration_commands_to_multiple_devices.py
  - Run show commands and save the output = Lab6/Run_show_commands_and_save_the_output.py
  - Backup the device configurations = Lab6/Backup_the_device_sonfigurations.py
  - Configure a subset of Interfaces = Lab6/Configuer_a_subset_of_interfaces.py
  - Send device configuration using an external file = Lab6/Send_device_configuration_using_an_external_file.py
  - Connect using a Python Dictionary = Heb ik niet.
  - Execute a script with a Function or classes = Lab6/execute_a_script_with_a_function_or_classes.py
  - Execute a script with a statements (if, ifelse, else) = Lab6/Execute_a_script_with_a_statements.py

Lab7

Uitleg: Het installeren van de CSR100v VM en het gebruik maken van het ynag model,netconf,restconf

- Task preparation and implementation:
  - CSR100v VM
  - DEVASC-LABVM
  - Visual studio code (aanwezig op de DEVASC-LABVM)
  - postman (aanwezig op de DEVASC-LABVM)
- Task troubleshooting:
  - Buiten dat mijn licentie van mijn VMware was verlopen geen problemen gehad.
- Task verification:
  - Kan een ssh verbinding maken = Lab7/ssh.png
  - kan via de webbrowser op de interface van het apperaat= Lab7/webbrowser_eigen_VM.png, Lab7/webbrowser_eigen_laptop.png
  - Het instaleren van het Yang model = Lab7/install _yang_model.png
  - Het ietf-interfaces.yang model in een tree format = Lab7/tree_format.png
  - ncclient-netetconf.py = Lab7/ ncclient-netetconf.png , Lab7/ ncclient-netetconf.py
  - creëer een loopback interface : Lab7/Loopback.png
  - Use Postman to Send a GET Request = Lab7/postman_Get_request.png
  - Use Postman to Send a GET Request via GigaBit 1 = Lab7/postman_Get_request_G1.png
  - Use Postman to Send a PUT Request = lab7/postman_put_request.png
  - GET request script = Lab7/restconf-get.py + Lab7/ restconf-get_result.png
  - PUT request script = Lab7/restconf-put.py + Lab7/ restconf-
