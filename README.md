# finanzreport
Name not final. Possible candidates:
1. Capital F
2. Save me
3. Pecunia

Apple changed the way we use technology

Amazon changed the way we shop

**We want to change the way you look at finances.**
## Description
Finances are essential to everyone in modern society and there are already a few things managed by tech:
* Online Banking is used widely
* There are a lot of mobile paying apps. One could say too many.

**Where is room for improvement?**

There is no widely used app to manage your finances as a private citizen.
We think you should always be able to see how much money you have.
You have two bank accounts?
Even with online banking you need to log in to both of them and manually combine the data.

Then there is Cash, your Paypal Account, maybe you own shares, etc.
Ask someone on the street how much they own right now. They probably won't know for sure.
Knowing how much there is, opens up many possibilities to make the lives of our users easier.
* Create your tax return automatically
* Set goals for saving
* Can I afford it?
* Breakdown: Where is my money going?
* Predictions of end of year balance
* investment options
* ...and much more

Our app should be the center of all things finance for the user.

**How do we create revenue?**

Finance data is one of the most valuable and sensitive information.
That's why we are not going to use it to make money.
The user should always have the option to save their data securely on their own machine without advertisers seeing it.
Our revenue will entirely consist of financial services we provide our customers.
Creating your tax return automatically is going to cost you a bit.
Saving your data securely in our cloud will not be free.
And there are many possibilities to offer services to our users that will be worth the money they pay for it.

**We won't and we can't use the data for directly creating revenue as a trustworthy image is one of the cornerstones of this app.**

## Technical stuff
How will it work?
###High-level
Without going into details. What do we need to achieve?
####Features to incorporate:
#####Short term:
* __Working web server__
    * import data
    * create user
    * download data
* __Web app__
    * login
    * look at data
    * add/edit data
#####Mid term:
* __Implementation of machine learning/artificial intelligence for predictions and importing data__
    * take a photo of money and get the sum
* Open up project and pay workers for added features
#####Long term
* Allow users to use the product
* Open up platform to plugins


#####Ideas
* Integrated unified OPEN mobile paying app (no more Google Pay, Samsung Pay, Apple Pay etc.)

###Specifics
In its full form it should be a cloud-based webapplication with a dedicated mobile app.
In the beginning data has to be added by hand.
The Columns:
- Transaction-ID (internal - not visible/editable by user)
- Date (with time?, maybe seperated in year, month, day)
- Value (currency?)
- product (e.g. laptop, groceries, rent, ...)
- category (e.g. tech, food, cost of living, ...)
- vendor (e.g. amazon, shop, none, ...)

This python application should function as the webserver with an API that the webapplication and mobile client can use.

The client could be a whole seperate project, which could kickstart as a machine learning application.
Users could make photographs of their money and the app would run a machine learning algorithm, which would tell them the value of the money in the foto.
