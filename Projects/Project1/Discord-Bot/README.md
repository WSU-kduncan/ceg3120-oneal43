- Setup
    - dependencies (what packages need to be installed to run the project)
	- pip install -U discord.py
	- pip install -U python-dotenv
    - how to get an API token
	- Select OAuth2 from the developer portal in discord
	- Select the drop down for Authorization Method and select "In-App Authorization"
	- Designate general permissions
    - where to put it to work with the code
	- In a .env file
  - Usage
    - with your changes to the code in place, describe
      - what commands you can type in your Discord server
	- ring!
      - what response this will provide (from your bot)
	- My bot will respond with Smeagol quotes
    - ![Smeagol Quotes](Smeagol.png)
  - Research
    - you may have realized that it is lame that the bot only runs when you run the program - it turns off if you disconnect or need to switch tasks.
    - In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running.
    - **Research** some possible solutions that would solve this, and discuss why you think it would work.
	- To solve the issue of not having the bot run 24/7, one could opt to leave their pc running 24/7 without exiting the script. Othr options that are more proper would be running it on a dedicate server or hosting it on a VPS. 
