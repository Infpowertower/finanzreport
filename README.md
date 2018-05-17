# finanzreport
This is supposed to be a simple to use but still powerful app to manage personal finances.

What is it for?
Users should have more control over their finances.
They should see at a glance what their current balance is, where their money is coming from and where it's going to.
For example the app should help users who overspent on a regular basis figure out what they could save on.
It is also for users with different bankaccounts to have all their finances in one place.

It should be possible to add saving goals. The app can give tips if the goals aren't met in which category spending was too high.

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
