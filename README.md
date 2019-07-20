# nerevu-interview
1) Write a Python script that fetches holiday data and saves it as a csv file named "holidays.csv".​ To obtain the data, you can either screen scrape the Time and Date​ site, or parse the API (free trial​ account required).

2) Using the csv file from 1), write a​ Python​ function that returns a list of dictionaries of the next 10 upcoming U.S. holidays and dates. E.g.

def holidays​():​
    pass


holidays​()​

[
    {
        "name​": "Bastille Day​",
        "date": "Sunday, July 14, 2019",
        "type": "Observance",
        "details​": ""
    },
    ...
]

Note: If you are unable to complete step 1), you can manually create the file by copying the data from the website and pasting it into Excel.​ ​  

3) Add a keyword argument "holidayType​"​ to the function from 2) such that it only returns holidays matching the given type, e.g., 

def holidays​(holidayType​​=None​):​
    pass

holidays​​(holidayType​​​="federal")    

[
   {
       "name​": "Labor​ Day​",
       "date": "Monday​, September 2, 2019",
       "type": "Federal Holiday​",
       "details​": ""
   },
   ...
]

4) Create a Python powered API that exposes the endpoint, "/holidays". A call to this endpoint should return a JSON response with a list of the next 10 upcoming U.S. holidays and dates. E.g.

[
    {
        "name​": "Bastille Day​",
        "date": "Sunday, July 14, 2019",
        "type": "Observance",
        "details​": ""
    },
    ...​
] 

5) Extend the API from step 4) to optionally take a query parameter "holidayType" and only return holidays matching the given type, e.g., A call to "/holidays?holidayType​=federal"​ should have "Labor Day" as the first returned holiday.