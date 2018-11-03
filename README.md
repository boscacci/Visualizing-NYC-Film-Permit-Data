# Visualizing NYC Open Film Permit Data

Tl;dr: Just me tinkering with kepler.gl.

## Basically

This .py script draws from NYC's open film and TV production permit records. It cross-references each permit's zip code against a Census Bureau directory of all USA zip codes, and provides its corresponding geographic coordinates. It then writes out a .csv with all the rough permit coordinates, which can in turn be uploaded to kepler.gl — to see a fun heatmap or hex-bin visualization of high-profile NYC film production activity!

## Thought Process

[NYC Open Data](https://opendata.cityofnewyork.us/) has an API that provides records of film permits filed between 2012 and 2016. Each record in this list includes information about start date, zip code, and the names of streets reserved by the production.

I wanted to visualize this temporal/geographic data with Kepler. I wanted to see all the film productions as chicken pox on the map of the greater NYC area. 

Unfortunately, Kepler won't accept this text string: "Broadway between 24th and 26th streets" — as a valid geographic coordinate. I think one could figure it out with a tool like [Google's Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro), but I was on a deadline to make something presentable, so I just used the zip codes.

## Extra Backstory

A while back my best friend Mike who happens to be a data scientist told me about Uber's nifty new open-source tool, kepler.gl. It offers super easy data visualization, he said. No programming experience needed, he said. Without any dev skills I was able to check out the demos and do little else.

Now I'm doing the [Flatiron School](https://flatironschool.com/)'s [Data Science Bootcamp](https://flatironschool.com/career-courses/data-science-bootcamp/). I've felt comfortable using computers to create since I was like 8, but only with pre-built GUI apps. Only after focusing this hard on Python for a number of weeks with actual instructors am I starting to feel the beginnings of an infantile competence playing with code.

The "filmdata_to_csv.py" in this repo is my first attempt at tossing around data in a fun creative way.

## References:

### Data:
[NYC Film Permits](https://data.cityofnewyork.us/City-Government/Film-Permits/tg4x-b46p)

[US Census Bureau zip codes](https://gist.github.com/erichurst/7882666)

### Kepler:
[Kepler.gl Main Demo Site](https://kepler.gl/#/)

[Uber engineering blog](https://eng.uber.com/keplergl)

[Third-party hype re: Kepler.gl](https://opensource.com/article/18/8/keplergl)

[Deeper-ish dive on guts of Kepler](https://medium.com/vis-gl/how-sometimes-assuming-the-earth-is-flat-helps-speed-up-rendering-in-deck-gl-c43b72fd6db4)

### Python:
[API Requests](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)

[CSV Parsing](https://stackoverflow.com/questions/39704096/parse-online-comma-delimited-text-file-in-python-3-5)

[CSV Writing](https://docs.python.org/2/library/csv.html)
