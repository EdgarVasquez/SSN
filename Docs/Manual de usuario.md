# User Manual
## HOW TO INSTALL
the installation that we show next, is for linux ubuntu 64
### Install Python  
<p> We start by updating the list of packages and installing the prerequisite </p>
<p> $ sudo apt update </p>
<p>$ sudo apt install software-properties-common</p>
<p>Next, we'll add the deadsnakes PPA to your list of sources: </p>
<p>$ sudo add-apt-repository ppa:deadsnakes/ppa</p>
<p> Once the repository is enabled, install Python 3.7 with: </p>
<p> $ sudo apt install python3.7 </p>
<p> Finally, Python 3.7 is installed on your Ubuntu system and ready to be used. You can verify it typing: </p>
<p> $ python3.7 --version </p>

### Clone git
<p> Open the Ubuntu terminal window</p>
<p> Ensure an Ubuntu Git installation exists</p>
<p>Run the following commands:</p>
  <p>$ git clone https://github.com/EdgarVasquez/NumerosRomanos.git </p>
  <p>$ cd my-github-repo</p>

## HOW IT IS EXECUTED
<p>Open the terminal pressing Ctrl + Alt + T.</p>
<p> Navigate the terminal to the directory where the script is located using the cd command.</p>
<p> Type python main.py in the terminal to execute it.</p>
  <p> If the script is python3, use python3 in the terminal command:python3 main.py </p>
 
## HOW TO USE THE APP
<p>When entering the app, it will launch a message that says: "Enter your Social Security Number", you will have to press a key, and it will ask you for the social security number, the number you are going to must be 9 digits, separated into 3 parts by hyphens, the first part must contain 3 digits, these must not be: "000","666" nor be between
"900" and "999", the second part must be two digits and must be between "01" and "99", and the third and last part must be 4 digits between "0001" and "9999", since otherwise it will not process the request, once the correct number has been entered, it will return a message saying: "Valid SSN number", otherwise it will return the reason why it is invalid</p>
