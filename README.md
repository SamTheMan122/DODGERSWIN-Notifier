# DODGERSWIN-Notifier

## About the Project
The new 2025 MLB season has started! Everytime the Los Angeles Dodgers win at home, you can use promo code 'DODGERSWIN' to get a $6 2 entree plate at Panda Express. This python-based applicatio/script will send a text message whenever this code is valid for the day.
I utilized web scraping to extract the table cells that contained the information for day of the game, home/away status, and win/loss.

## Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project uses Python and requires the use of certain modules, libraries, and packages.
1. Make sure Python is installed. Install [here](python.org):
2. This program used Selenium and webdeiver-manager for web scraping. Run these to install on your device
```bash
py -m pip install selenium
py -m pip install webdriver-manager
```
### Supported Carriers
| Carrier Type         | Carrier Name              |
|----------------------|---------------------------|
| **Major Carrier**     | VERIZON                   |
|                      | ATT                       |
|                      | T-MOBILE                  |
|                      | SPRINT                    |
| **Verizon MVNOs**     | VISIBLE                   |
|                      | XFINITY MOBILE            |
|                      | SPECTRUM MOBILE           |
|                      | PAGE PLUS                 |
|                      | STRAIGHT TALK VERIZON     |
|                      | TOTAL WIRELESS            |
|                      | TRACFONE VERIZON          |
| **AT&T MVNOs**        | CRICKET                   |
|                      | H2O WIRELESS              |
|                      | FREEUP MOBILE             |
|                      | STRAIGHT TALK ATT         |
|                      | NET10 ATT                 |
|                      | RED POCKET ATT            |
| **T-Mobile MVNOs**    | METROPCS                  |
|                      | MINT MOBILE               |
|                      | ULTRA MOBILE              |
|                      | TING T-MOBILE             |
|                      | TALKATONE                 |
|                      | TRACFONE T-MOBILE         |
|                      | NET10 T-MOBILE            |
|                      | RED POCKET T-MOBILE       |
| **Sprint MVNOs**      | BOOST MOBILE              |
|                      | VIRGIN MOBILE             |
|                      | FREEDOMPOP                |
|                      | TEXTNOW                   |
| **Other / Hybrid**    | GOOGLE FI                 |


<!-- Installation -->
### Installation

To automatically have texts sent, set a task schedule on your Windows PC.

1. Download the DODGERSWIN.exe file from the [latest release](https://github.com/SamTheMan122/DODGERSWIN-Notifier/releases/tag/v1.0.0)
2. Open the Task Scheduler (Ex: use Win + S and type in 'Task Scheduler'
3. Select **Create Task**
4. Add a name and a description
5. Navigate to the **Actions** tab and select **New**
6. Under **Actions**, make sure to select **Start a program**
7. Enter the path for the **DODGERSWIN.exe** file or alternatively, browse and look for the application
8. Under **Add arguments**, type in your phone number and your carrier in the following format: 1234567890 carrier (ex: 1234567890 Verizon)
   - For list of supporteed characters, see [Supported Carriers](#supported-carriers)
   - Please type in the carrier as shown in [Supported Carriers](#supported-carriers)
10. Click Ok
11. Navigate to the **Triggers** tab and select **New**
12. Select the desired frequency of notifications. For daily notifications, my configurations were:
    - Daily
    - 7AM
    - Recur every 1 day
13. Select Ok when done

<!-- Contributing -->
## Contributing
- @SamTheMan122

<!-- Contact -->
## Contact

Samuel Barcarse - samuel.barcarse01@gmail.com

Project Link: [https://github.com/SamTheMan122/DODGERSWIN-Notifier](https://github.com/SamTheMan122/DODGERSWIN-Notifier)
