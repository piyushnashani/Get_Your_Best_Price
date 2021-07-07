# Get_Your_Price
Amazon Price tracker

Hey! Do you wanna purchase your favorite item from a popular e-commerce website like Amazon, but still waiting for the best price? Getting tired of opening and monitoring prices manually again and again? Here comes Get_Your_Price to your rescue by automating this boring process of manually opening and checking prices repeatedly. This application will not only monitor and plot beautiful price plots but also will take your desired value of the product, also your minimum and maximum price ,and will send you an email notification whenever the price falls below that desired value. It can even be deployed on cloud platforms. Crazy? Let's get started

# Installation
You will require Python3 for building this source code on your local machine. You can download the source code and install the dependencies given in requirement.txt, make sure to place your chrome driver file with these files and you can download your chrome driver file by following the steps: go to your browser-> settings -> about chrome -> check your chrome version-> go to https://chromedriver.chromium.org/downloads -> click on the link that defines you chrome version -> click on the file that defines your Operation system e.g.for windows it can be named as "	chromedriver_win32.zip"-> it will download a file -> unzip the file and place it with the files as shown in the picture below -> rename that file as "chromedriver" -> Place this file with these files. You may use pip to install this dependencies. Recommended operating system: It works fine on the Windows Operating system. You are good to go!

![image](https://user-images.githubusercontent.com/63044831/124708398-da05ff00-df17-11eb-8c96-6b2805206053.png)


# One Time Configuration
You can use Pyhcarm, Visual Studio Code ,or any other source code editor to run the program. 
To get started with the program and choose your desired product from the list of products, max and min range ,and the Desired price: follow the steps below

## step1 
Go to the Amazon_config.py, in line-5 Enter the name of the product you want to search for. In line-7, enter the minimum price range for the product ,and in line-8 enter the maximum price range for the product. e.g. in the below picture, I have added "vivo phones as my product search and min and max price range as "10000" and "60000". The currency is in "Rupees"

![image](https://user-images.githubusercontent.com/63044831/124705543-711c8800-df13-11eb-88ce-bea189db9855.png)


## step2
Go to google or any browser on your local machine and search for "my user agent" and you will get your user agent for example shown in the picture below is my user agent. Now copy-paste this in your Amazon_Config.py and in line-12, paste it inside the header after your user agent that is inside the second single inverted commas and your 
configuration file that is Amazon_Confi.py is ready. e.g. In the below picture, I have added my user agent on my browser inside the single inverted commas.

![image](https://user-images.githubusercontent.com/63044831/124705860-f56f0b00-df13-11eb-9995-2a8a7e8a49fc.png)


## step3
Go to google and enable your two-step verification and also set your google app password. This is how you enable two-step verification, go to "https://bit.ly/36fvASY" and enter your google account's password, click on continue by choosing your device linked with your phone number with google account, then enter your phone number for verification and choose text message/phone call according to your convenience and enter the verification code and then turn on your 2-step verification. 
For setting google app password, go to "https://bit.ly/3xmw6dX" and sign in to your google account then select app as "mail" and select your device as your local machine e.g. windows PC users select windows computer and then generate the password. Copy that password and go to your Main.py and in line-221, the second single inverted commas and inside the first single inverted commas on the same line, enter your Gmail id and then go to line 226 inside the single inverted commas type your Gmail id and also write the same Gmail id in line 227 inside the single inverted commas.
e.g. In the first picture below, inside the first single inverted commas, I have added a random Gmail id and inside the second single inverted commas, a random 16 letters password as you will get a 16 letters password. In the second picture below, I have added the same Gmail ids in both lines.

![image](https://user-images.githubusercontent.com/63044831/124706157-76c69d80-df14-11eb-9d51-641ac41b91aa.png)

![image](https://user-images.githubusercontent.com/63044831/124706500-08360f80-df15-11eb-98f3-babdabc2a59f.png)


## Note
This code is safe as you will be sending mail to yourself while checking for the product and when the price fell according to your data provided. Also note that you are giving your mail id in the from section (from where the mail will come) i.e. line-226 and to section (to whom the mail will go) and hence your data is safe and not shared with anyone, especially your password.
## step4
Open your terminal and run the Main.py file e.g. in Pycharm just typing Main.py will run your file and then wait for the file to run, it will open your browser in incognito and will collect the data for all the list of products for your searched one, you can minimize that browser screen as it will automatically run your browser and don't close it otherwise it will fail to collect the data. Note that it depends on your internet connection that how fast the program runs.
## step5
As the browser closes, in your terminal, it will give you the list of products along with some information regarding the product e.g. the product name, its seller, its price ,and id. Then just input the number (i.e. index) of your desired product from the list (no. in front of your desired product from the list) and then enter your desired price for the product. Also, it will ask you to give you the price tracking of that product with the help of a graph. And it will keep checking the price of your product after every 7200 seconds (i.e. 2 hours). If the desired price for the product you mentioned is above or equal to the price of the product then it will send you the mail.

![image](https://user-images.githubusercontent.com/63044831/124706969-c9548980-df15-11eb-973b-b2cabfb8cd5c.png)


## Note
You have to re-run the program whenever you will be restarting your PC, to keep a price tracking of your product. Also, your internet connection should be available all the time, unless and until your desired price is reached and you get a mail. 

## Errors? Crashes?
Filling wrong information can cause the program to crash. In such cases, delete the folder where you have kept this source code and then download and copy the fresh code and configure it again.
