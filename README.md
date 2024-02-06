# Caffeine
Caffeine is a simple python application that prevents the Windows lock screen from activating when the computer is left idle. 

It achieves this by simulating keyboard or mouse activity at predetermined intervals. The primary goal is to ensure that users can maintain their workflow or presentation without interruptions due to the system locking automatically. The program will offer customizable settings to allow users to specify the frequency of simulated input, ensuring it can be tailored to individual needs and preferences. Additionally, the application will be developed with user safety and system security in mind, ensuring that it does not interfere with the overall performance of the system or present any security vulnerabilities.

## How to run
Follow the steps below:

step 1: Clone the repository
```bash
git clone https://github.com/cleitonsouza01/caffeine-python
```

step 2: Install the dependencies
```bash
pip install -r requirements.txt
```

step 3: Run the application
```bash 
python caffeine-python.py
```

## How to convert in .exe file
Follow the steps below:

```bash	
pyinstaller --onefile --upx-dir C:\upx .\caffeine-python.py
```
UPX helps to reduce the size of the executable file. You can download it [here](https://upx.github.io/)

