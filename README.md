# Readme

This is a project to read messages automatically from whatsapp(web only) and send replies with the help of a pre-trained chat bot.

Unlike the auto reply feature in business version of whatsapp, where only a pre-recorded message is sent everytime, this automation offers many possibilities. You can read messages from a particular user and send intelligent replies. Application of text to speech and vice versa would take the game to next level.

*please respect the privacy of others as much as yours!*

## Usage

1. Download the __.bat__ file and make the neccessary changes. The purpose of this script is to open chrome in debugger mode in the given port, as well to create a chrome profile so we dont have to login to whatsapp everytime(to preserve user data a.k.a cache).

    ###### Syntax
    >chrome.exe –remote-debugging-port=any-free-port –user-data-dir=directory path where you need to store data

    ###### Example
    >chrome.exe –remote-debugging-port=9222 –user-data-dir=E:\chromeData

2. Run the __Automation_Script.py__, which contains the main code and all the automation processes.

    Before running please ensure that you are updating the path to the .bat file. Yes, the .bat file is also invoked from the python script just to reduce the overhead.

3. Once everything is working fine, train the bot with __Training_chat_bot.py__.

    Note that you can do this in any order. I suggest taking a demo run of __Automation_Script.py__ first(comment out the automatic reply part) and see if everything is working fine. Then, train the bot and run the entire script.