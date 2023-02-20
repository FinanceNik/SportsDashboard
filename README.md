# SportsDashboard
This dashboard serves as a non-commercial, open-source alternative to a well-known sports application. 
With this dashboard, you can visualize your sports data and do some basic analysis. Furthermore, you can use 
the presented information in order to track your sports progress and set new goals.

---
## Version: 0.1.0
### Author: Finance Nik 
#### Date: 20.02.2023

---

## Prerequisites 
This section briefly describes the prerequisites for this project. You need to have Python3, PIP, necessary libraries
and the Strava data export in order to run the dashboard.

### Python 3 
You need to have Python 3 installed, preferrably a version >3.6 due to compatability.
Checkable via:
```bash
python --version
```
If Python is not installed, you can do so in the terminal:
```bash
sudo apt-get install python3
```

### PIP 
You need to have Python's package manager named PIP:
```bash
pip --version
```
If PIP is not installed, you can do so in the terminal:
```bash
sudo apt-get install pip3
```

### Strava Data Export 
To be able to use the dashboard, you need to export your data from Strava. 
This can be a bit of a cumbersome task and hence, this guide shall guide you through the process. 

1. log into your Strava account: https://www.strava.com/login
2. Once logged in, go to your account settings: https://www.strava.com/settings/profile
3. Click on the second tab named "My Account"
4. Scroll down to the bottom of the page to the section named "Download or Delete Your Account"
5. Click on "Get Started"
6. Scroll to the second option of the page and click on "Request Your Archive"
7. You will receive an email with a link to download your data. Click on the link and download the zip file.
8. Unzip the file and go into the folder to get the "activities.csv" file.
9. Move the "activities.csv" file into the "assets" folder of this project.
10. You are ready to go!

---
