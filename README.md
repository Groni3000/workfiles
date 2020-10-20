# workfiles
In trying to learn django | update_1

I created this "project" in trying to learn Django. 
This "project" is mainly just to make some testing code and possibilities of django. 
I don't have any ideas for this "project" so I used some ideas from: testing task, my friends and I've created a <<food_calculator>> (my poor idea). Ye, pretty common idea, but I want to make relationship between this <<food_calculator>> and 'user model'. Well, those models (more presicly - apps) I've created. The only thing - connect them. Still don't know what connection it has to be: one-to-one, or many-to-one? 

--------------------------------------------------------------------------------------------------------------------------
In the first case I MUST create some kind of 'object-diary' that will include program-menu that user have chosen in <<food_calculator>> (ye, there will be a "add to menu" option with "menu for week"-model, I guess) and in this case there will be possibility to include other objects into 'object-diary'. Pretty and some kind of "I'm gonna put all objects into containers and that containers into bigger containers and so on ... With a big one in the end.". And I'll be able to reference to objects in 'object-diary' just by name of object. Pretty sure that this possibility realized in Django. Still, don't know a lot about Django and it's possibilities.

--------------------------------------------------------------------------------------------------------------------------
In the second case I CAN (get attension on 'MUST-CAN options'! CAN option - is easier to make but harder in the future make complicated stuff, at least - I think so...) create separated objects-models and just connect them. So there will be some kind of "spider web" between models. Seems to be really complicated in the future.

--------------------------------------------------------------------------------------------------------------------------

What can do this project right now?
1) First thing i made here:
https://jsonplaceholder.typicode.com/todos/{id}, where type({id})=int in range(1,101). For each id between 1-100 checked the “userId” and “completed” fields.
If the status “completed” is “true” I did insert the “title”, “titleId”, “stampdate” (I did fault by naming it as pub_time) and “userId”  into SQLite table “stories”. And created a webpage where I present all stories (webpage named as "completed stories")

--------------------------------------------------------------------------------------------------------------------------
To do this I wrote a custom manage-command named "rundb.py" in "mainpages/managment/commands". For my big surprise, it didn't autofill 'id autofield' and I had to make stories with increment-parametr 'i' ... Any suggestions? Maybe it's just because it's manage-command? But in further commands I didn't have this problem... 

Well, I will test this file another time TODO :)

2) Second thing I made:
I asked friend for any idea for this project. He wanted me to write some kind of search paint for cars by its vendor code. I thought that was a good practice idea. But I don't wanna to type all info for model 'paintforcar' by my own hands, so... I thought that it's another good practice idea: learn how to get information from web-pages run info to DB and search for certain objects. Ye, I know, it's kinda similar to first thing i made, but i wanted to do this with a 'real' web-page with a lot of tags, with a lot of attributes in them, etc. So I installed bs4 and used it. It was really easy to get info from certain web-site. For this task I created a custom manage-command named "rundbwithpaint.py" and it works perfectly without problem like in 1st 'paragraph'.

TODO write exactly the same command with attribures 


(


'url_of_site', 


(allowed_part_of_url_1, ..., allowed_part_of_url_m),


{tag_I_search_1 : attrs_in_that_tag,..., tag_I_search_n : attrs_in_that_tag}, 


(name_of_model_1, ..., name_of_model_k) 


)

And figure out how to make a certain search... But this requires to make a good think about models fields: what fields are #mandatory,  how can i store that is not provided in the mandatory fields and use it with good (at least not bad) efficacy

As I tested 2) a lot, I got a problem with deleting data from table. Django allows to delete <1000 object at once, but i got much more and supposed to delete data by 100 objects to reach 1000 objects that I can delete byt once. So I did write a custom manage-command named "delete_data_in_table_named.py" with parametrs. So u can type 'python manage.py delete_data_in_table_named name_of_my_table' and it will delete all data. I didn't try to delete data from unexisting table, so ... it wasn't good idea to let all this custom manage-commands without Exception catcher...

3) I made a search by category and tried to define functions that process data outside of view.py file. I stored them in 'services.py'. So code in 'view.py' looks really short and pretty (I tried to name functions in way to easily understand what this function's doing). But I described func-based view so detailed ... too detailed. 

TODO Think about 'how can I describe function within 4-5 string... maybe I should look for extension for VScode that allows #me to hide strings with comments but still have access when I'm trying to find text by Ctrl+F'

In 'services.py' I thought that I should make something ... Interactive. That I should make functions usable in other pages, not only "result_of_search_page", so i added some parametrs in this functions that can allow us to control behavior of function (controlling a number of objects on page that i found by search, controlling 'What fields should I allow to show on the web-page, in html doc?')

TODO and I'm gonna try to make 'controllable' function that defines parts of url for paginator. That would be REALLY useful, I guess.

--------------------------------------------------------------------------------------------------------------------------
UPDATE_1

--------------------------------------------------------------------------------------------------------------------------

4) Created <<food_calculator>>. You can find it inside dropdown menu ("evaluate for me" - link) of navbar. For future: 

4.1) Create menu for a week

4.2) Create a 'progress bar' for autheticated users (using his values: height, weight, age and something else?) that accumulates all values of calories, proteins, etc ... and change colour (green for slimming, yellow for optimal and red for <<DANGER, you will be a fat person!>>). Need some iformation about diets, tips for slimming or for gain muscles and use this info not only in logic of programm but ... Maybe show "random tips" for user's focus (on slimming or getting muscles).
